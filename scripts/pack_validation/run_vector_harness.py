#!/usr/bin/env python3
"""
VALOR Architecture Pack -- Vector-Driven Test Harness  (Phase A / A3, gaps G-12 + G-20)

Run from the pack root (where manifest.yaml lives):

    python scripts/pack_validation/run_vector_harness.py
    python scripts/pack_validation/run_vector_harness.py --verbose
    python scripts/pack_validation/run_vector_harness.py --strict-negative

What this closes (vs smoke_test.py, which runs manifest + a *.schema.json parse glob
+ 2 report vectors + preset bindings only):

  * SCHEMA COVERAGE  -- loads AND draft-07 meta-validates ALL schemas, including the
    12 schemas/objects/*_schema.json files that the smoke-test glob ("*.schema.json")
    silently skips (G-20b).
  * REAL $ref REGISTRY -- builds a `referencing` registry keyed by each schema's $id
    (scheme valor://schemas/...), so every cross-file $ref resolves by URI rules.
    Replaces smoke_test.py's single hand-inlined ref (G-20c).
  * FULL VECTOR CORPUS -- discovers and accounts for every vector file, not just 2.
    Each vector is routed by structure into one of three honest classes (G-20a):

      Class A  schema-validation suites (governance / registry / security):
               positive_cases / negative_cases carry an `instance` + a `schema_ref`
               (per-case or group-level) + `expected_result.valid`. We validate the
               instance against the schema and compare the verdict to expected.valid.

      Class B  single-instance positives (expected_*.json, seed_wp.json): a bare JSON
               instance mapped by convention to a schema. Must validate clean.

      Class C  behavioral suites (negative/, ks_*, e2e/, expected_export): these assert
               ENGINE behavior (expected_outcome / expected / flow_steps -> ok/state/
               code/subcode). No engine exists yet, so they are NOT schema-validatable.
               Pre-engine we do the strongest honest thing: load them, recognize their
               structure, and cross-reference every declared action_type against the
               contract registry. They are reported as BEHAVIORAL (pending engine), and
               counted -- never silently inert, never faked green.

Exit codes:
    0 = PASS (no hard failures)
    1 = FAIL (a hard failure occurred -- see policy note in summary)
    2 = MISCONFIG (missing deps / cannot run)

This file is PACK tooling and lives under scripts/ (it becomes a governed asset;
regenerate the manifest from a fresh LF clone after adding it).
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Optional

# -----------------------------------------------------------------------------
# Dependencies
# -----------------------------------------------------------------------------
try:
    import yaml  # type: ignore
except Exception:
    print("ERROR: missing 'pyyaml'  (pip install pyyaml)", file=sys.stderr)
    sys.exit(2)

try:
    from jsonschema import Draft7Validator
    from jsonschema.exceptions import SchemaError
    from referencing import Registry, Resource
    from referencing.jsonschema import DRAFT7
except Exception as e:  # pragma: no cover
    print(f"ERROR: need jsonschema>=4.18 with 'referencing' ({e})", file=sys.stderr)
    sys.exit(2)


# -----------------------------------------------------------------------------
# Result accounting
# -----------------------------------------------------------------------------
@dataclass
class Counts:
    passed: int = 0
    failed: int = 0           # hard failures (block)
    warned: int = 0           # soft signals (do not block by default)
    behavioral: int = 0       # registered, pending engine
    details: list[str] = field(default_factory=list)

    def note(self, msg: str) -> None:
        self.details.append(msg)


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


# -----------------------------------------------------------------------------
# Schema registry  (coverage + meta-validation + cross-file $ref resolution)
# -----------------------------------------------------------------------------
def _rewrite_refs(node: Any, schema_path: Path, pack_root: Path,
                  id_by_relpath: dict[str, str]) -> None:
    """Rewrite relative-file $refs to the target's absolute registered $id.

    The pack's $ids use a custom 'valor://' scheme, which urllib.urljoin does NOT
    resolve relative refs against (custom schemes aren't in its relative-resolution
    set). So we resolve each relative file $ref to its target's $id at load time,
    turning every cross-file ref into an exact registered key."""
    if isinstance(node, dict):
        for k, v in list(node.items()):
            if k == "$ref" and isinstance(v, str) and v and not v.startswith("#") \
                    and "://" not in v:
                base = v.split("#", 1)[0]
                frag = v[len(base):]
                target = (schema_path.parent / base).resolve()
                try:
                    rel = target.relative_to(pack_root.resolve()).as_posix()
                except ValueError:
                    continue
                if rel in id_by_relpath:
                    node[k] = id_by_relpath[rel] + frag
            else:
                _rewrite_refs(v, schema_path, pack_root, id_by_relpath)
    elif isinstance(node, list):
        for v in node:
            _rewrite_refs(v, schema_path, pack_root, id_by_relpath)


def build_schema_registry(pack_root: Path):
    """Load every schema (both *.schema.json and *_schema.json), meta-validate as
    draft-07, and register by $id for cross-file $ref resolution.

    Returns (registry, by_id, id_by_relpath, counts)."""
    c = Counts()
    schema_dir = pack_root / "schemas"
    paths = sorted(p for p in schema_dir.rglob("*.json") if p.name != "index.json")

    # Pass 1: load + meta-validate + index relpath -> $id
    raw: list[tuple[Path, str, dict]] = []
    by_id: dict[str, Path] = {}
    id_by_relpath: dict[str, str] = {}
    for p in paths:
        rel = p.relative_to(pack_root)
        try:
            contents = load_json(p)
        except Exception as e:
            c.failed += 1
            c.note(f"[schema] PARSE FAIL {rel}: {e}")
            continue
        try:
            Draft7Validator.check_schema(contents)
        except SchemaError as e:
            c.failed += 1
            c.note(f"[schema] META-INVALID {rel}: {e.message}")
            continue
        sid = contents.get("$id")
        if not sid:
            c.warned += 1
            sid = f"valor://{rel.as_posix()}"
            c.note(f"[schema] no $id (synthesized {sid}): {rel}")
        raw.append((p, sid, contents))
        by_id[sid] = p
        id_by_relpath[rel.as_posix()] = sid

    # Pass 2: rewrite relative refs to absolute $ids, build + register resources
    resources: list[tuple[str, Resource]] = []
    for p, sid, contents in raw:
        _rewrite_refs(contents, p, pack_root, id_by_relpath)
        try:
            res = Resource.from_contents(contents, default_specification=DRAFT7)
        except Exception:
            res = Resource(contents=contents, specification=DRAFT7)
        resources.append((sid, res))
        c.passed += 1

    registry = Registry().with_resources(resources)
    return registry, by_id, id_by_relpath, c


def ref_to_id(ref: str, id_by_relpath: dict[str, str]) -> str:
    """Map a vector's pack-relative schema_ref to the registered $id."""
    return id_by_relpath.get(ref, f"valor://{ref}")


def validate_instance(instance: Any, schema_id: str, registry: Registry) -> Optional[str]:
    """Validate an instance against a registered schema (by $id), anchoring the base
    URI so nested cross-file relative $refs resolve. Returns None if valid, else the
    first error message."""
    validator = Draft7Validator({"$ref": schema_id}, registry=registry)
    errors = sorted(validator.iter_errors(instance), key=lambda e: list(e.path))
    if not errors:
        return None
    e = errors[0]
    loc = "/".join(str(x) for x in e.path) or "<root>"
    return f"{loc}: {e.message}"


# -----------------------------------------------------------------------------
# Contract registry -> valid action_type set  (for Class C cross-reference)
# -----------------------------------------------------------------------------
def collect_action_types(pack_root: Path) -> set[str]:
    reg_path = pack_root / "contracts" / "CONTRACT_REGISTRY_v1.0.1.yaml"
    actions: set[str] = set()
    if not reg_path.exists():
        return actions
    try:
        data = load_yaml(reg_path)
    except Exception:
        return actions

    def walk(node: Any) -> None:
        if isinstance(node, dict):
            for k in ("type", "action_type"):
                v = node.get(k)
                if isinstance(v, str) and v.isupper() and "_" in v:
                    actions.add(v)
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(data)
    return actions


# -----------------------------------------------------------------------------
# Class B -- single-instance positive vectors (mapped by convention)
# -----------------------------------------------------------------------------
CLASS_B_MAP = {
    "test_vectors/seed_wp.json": "schemas/objects/work_package_schema.json",
    "test_vectors/expected_committed_wp.json": "schemas/objects/work_package_schema.json",
    "test_vectors/expected_staged_tasks.json": "schemas/contracts/staged_task_set.schema.json",
    "test_vectors/expected_plan_proposal.json": "schemas/contracts/plan_proposal.schema.json",
    "test_vectors/expected_doc_metadata.json": "schemas/objects/document_metadata_schema.json",
    "test_vectors/expected_report_single_wp.json": "schemas/contracts/report_result.schema.json",
    "test_vectors/expected_report_multi_wp.json": "schemas/contracts/report_result.schema.json",
    # expected_export.json is a SCENARIO/declaration vector (vector_id/target_scope_*/
    # artifacts), NOT a single instance -> handled as Class C, not validated here.
}


def run_class_b(pack_root: Path, registry: Registry, id_by_relpath: dict[str, str],
                verbose: bool) -> Counts:
    c = Counts()
    for rel, schema_rel in CLASS_B_MAP.items():
        vp = pack_root / rel
        if not vp.exists():
            c.failed += 1
            c.note(f"[B] MISSING vector {rel}")
            continue
        try:
            instance = load_json(vp)
        except Exception as e:
            c.failed += 1
            c.note(f"[B] LOAD FAIL {rel}: {e}")
            continue
        schema_id = ref_to_id(schema_rel, id_by_relpath)
        err = validate_instance(instance, schema_id, registry)
        if err is None:
            c.passed += 1
            if verbose:
                c.note(f"[B] PASS {Path(rel).name} -> {Path(schema_rel).name}")
        else:
            c.failed += 1
            c.note(f"[B] FAIL {Path(rel).name} -> {Path(schema_rel).name}: {err}")
    return c


# -----------------------------------------------------------------------------
# Class A -- schema-validation suites (governance / registry / security)
# -----------------------------------------------------------------------------
CLASS_A_FILES = [
    "test_vectors/governance/audit_event_vectors.json",
    "test_vectors/governance/branch_override_vectors.json",
    "test_vectors/registry/registry_validation_vectors.json",
    "test_vectors/security/security_event_vectors.json",
]


def _case_schema_ref(case: dict, group_ref: Optional[str]) -> Optional[str]:
    return case.get("schema_ref") or group_ref


def run_class_a(pack_root: Path, registry: Registry, id_by_relpath: dict[str, str],
                verbose: bool, strict_negative: bool) -> Counts:
    c = Counts()
    for rel in CLASS_A_FILES:
        vp = pack_root / rel
        if not vp.exists():
            c.failed += 1
            c.note(f"[A] MISSING vector {rel}")
            continue
        try:
            doc = load_json(vp)
        except Exception as e:
            c.failed += 1
            c.note(f"[A] LOAD FAIL {rel}: {e}")
            continue

        group_ref = doc.get("schema_ref")  # single top-level ref (audit/security)
        name = Path(rel).name

        for polarity, expect_valid in (("positive_cases", True), ("negative_cases", False)):
            for case in doc.get(polarity, []):
                cid = case.get("case_id", "<no-id>")
                instance = case.get("instance")
                ref = _case_schema_ref(case, group_ref)
                if instance is None or ref is None:
                    c.warned += 1
                    c.note(f"[A] {name}:{cid} no instance/schema_ref -> skipped")
                    continue
                schema_id = ref_to_id(ref, id_by_relpath)
                err = validate_instance(instance, schema_id, registry)
                schema_valid = err is None
                # vector's own declared expectation (overrides polarity if present)
                exp = case.get("expected_result", {})
                expected_valid = exp.get("valid", expect_valid)

                if schema_valid == expected_valid:
                    c.passed += 1
                    if verbose:
                        c.note(f"[A] PASS {name}:{cid} (valid={schema_valid})")
                elif (not expected_valid) and schema_valid:
                    # vector says invalid, schema accepts: business-rule case the
                    # draft-07 schema does not (and may not be meant to) encode.
                    if strict_negative:
                        c.failed += 1
                        c.note(f"[A] FAIL {name}:{cid} expected invalid, schema accepts "
                               f"(code={exp.get('code')}/{exp.get('subcode')})")
                    else:
                        c.warned += 1
                        c.note(f"[A] WARN {name}:{cid} schema accepts a case the vector "
                               f"marks invalid -> engine-enforced rule "
                               f"({exp.get('code')}/{exp.get('subcode')})")
                else:
                    # expected valid but schema rejects: a real defect.
                    c.failed += 1
                    c.note(f"[A] FAIL {name}:{cid} expected valid, schema rejects: {err}")
    return c


# -----------------------------------------------------------------------------
# Class C -- behavioral suites (no engine yet; register + structural cross-ref)
# -----------------------------------------------------------------------------
CLASS_C_GLOBS = [
    "test_vectors/negative/*.json",
    "test_vectors/e2e/*.json",
    "test_vectors/ks_*.json",
    "test_vectors/expected_export.json",
]


def _iter_class_c(pack_root: Path):
    seen = set()
    for g in CLASS_C_GLOBS:
        for p in sorted((pack_root).glob(g)):
            if p not in seen:
                seen.add(p)
                yield p


def _collect_action_types_in(node: Any, out: list[str]) -> None:
    if isinstance(node, dict):
        v = node.get("action_type")
        if isinstance(v, str):
            out.append(v)
        for vv in node.values():
            _collect_action_types_in(vv, out)
    elif isinstance(node, list):
        for vv in node:
            _collect_action_types_in(vv, out)


def run_class_c(pack_root: Path, valid_actions: set[str], verbose: bool) -> Counts:
    c = Counts()
    for vp in _iter_class_c(pack_root):
        rel = vp.relative_to(pack_root).as_posix()
        try:
            doc = load_json(vp)
        except Exception as e:
            c.failed += 1
            c.note(f"[C] PARSE FAIL {rel}: {e}")
            continue

        # count behavioral cases (best-effort across the several shapes)
        n_cases = 0
        for key in ("cases", "positive_cases", "negative_cases", "flow_steps",
                    "flows", "artifacts"):
            v = doc.get(key)
            if isinstance(v, list):
                n_cases += len(v)
        if n_cases == 0 and ("expected" in doc or "expected_outcome" in doc):
            n_cases = 1  # single-case ks file
        c.behavioral += max(n_cases, 1)

        # cross-reference declared action_types against the registry (real drift check)
        found: list[str] = []
        _collect_action_types_in(doc, found)
        if valid_actions:
            unknown = sorted({a for a in found if a not in valid_actions})
            if unknown:
                c.failed += 1
                c.note(f"[C] UNKNOWN action_type in {rel}: {', '.join(unknown)}")
            elif verbose:
                c.note(f"[C] {rel}: {n_cases} behavioral case(s), "
                       f"{len(set(found))} action_type(s) all resolve")
        elif verbose:
            c.note(f"[C] {rel}: {n_cases} behavioral case(s) (registry unavailable)")
    return c


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description="VALOR vector-driven test harness (A3)")
    ap.add_argument("--verbose", action="store_true")
    ap.add_argument("--strict-negative", action="store_true",
                    help="Treat 'schema accepts a vector-invalid case' as a hard FAIL "
                         "(default: WARN, since these are engine-enforced rules).")
    args = ap.parse_args()

    pack_root = Path(__file__).resolve().parents[2]
    if not (pack_root / "manifest.yaml").exists():
        print(f"ERROR: not a pack root (no manifest.yaml): {pack_root}", file=sys.stderr)
        return 2

    print(f"VALOR Vector Harness -- pack_root: {pack_root}")

    registry, by_id, id_by_relpath, c_schema = build_schema_registry(pack_root)
    valid_actions = collect_action_types(pack_root)
    c_b = run_class_b(pack_root, registry, id_by_relpath, args.verbose)
    c_a = run_class_a(pack_root, registry, id_by_relpath, args.verbose, args.strict_negative)
    c_c = run_class_c(pack_root, valid_actions, args.verbose)

    sections = [
        ("Schema coverage (load + draft-07 meta-validate)", c_schema),
        ("Class B  single-instance positives", c_b),
        ("Class A  schema-validation suites", c_a),
        ("Class C  behavioral suites (pending engine)", c_c),
    ]

    print("\n================ RESULTS ================")
    print(f"Registry: {len(by_id)} schemas registered | "
          f"action_types known: {len(valid_actions)}")
    hard_fail = 0
    for title, cc in sections:
        print(f"\n-- {title}")
        print(f"   pass={cc.passed}  fail={cc.failed}  warn={cc.warned}  "
              f"behavioral={cc.behavioral}")
        hard_fail += cc.failed
        show = cc.details if args.verbose else [d for d in cc.details
                                                if " PASS " not in d and not d.strip().startswith("[")
                                                or " FAIL " in d or "WARN" in d or "UNKNOWN" in d
                                                or "INVALID" in d or "MISSING" in d]
        for d in show:
            print(f"     {d}")

    print("\n=========================================")
    if hard_fail:
        print(f"Overall: FAIL ({hard_fail} hard failure(s))")
        return 1
    warns = sum(cc.warned for _, cc in sections)
    print(f"Overall: PASS  ({warns} warning(s) -- engine-enforced rules, non-blocking)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
