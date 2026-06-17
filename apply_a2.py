#!/usr/bin/env python3
"""
apply_a2.py — Phase A / A2 integrity-tooling fix for the VALOR Architecture Pack.

Closes G-19: generate_manifest.py and verify_manifest.py used DIFFERENT ignore
rules (different dir sets, different match depth, no suffix exclusion in the
verifier), so a routine .pytest_cache/ or stray .pyc made verify_manifest.py
FALSE-FAIL with "extra files". This:

  1. writes  scripts/pack_validation/pack_excludes.py  (single source of truth:
     excluded dirs matched at ANY depth + generated-file suffixes),
  2. patches generate_manifest.py to import that shared rule,
  3. patches verify_manifest.py to (a) use the shared rule for extras-detection
     and (b) hoist the loop-invariant `manifest_paths` out of the per-entry loop.

It applies SURGICAL string patches and ABORTS loudly if the source doesn't match
what it expects — so it won't silently corrupt a file it doesn't recognise.

USAGE
    python3 apply_a2.py            # apply in current dir (must be pack root)
    python3 apply_a2.py --path /repo
    python3 apply_a2.py --dry-run  # report only; write nothing

AFTER RUNNING (your steps):
    Move-Item apply_a2.py ..\\apply_a2.py        # keep the tool OUT of the pack
    git add -A
    git commit -m "A2: unify manifest exclude rules + hoist loop-invariant (G-19)"
    python scripts/pack_validation/generate_manifest.py   # new module is now tracked
    python scripts/pack_validation/verify_manifest.py     # expect clean PASS
"""

import argparse
import importlib.util
import sys
from pathlib import Path

PV = Path("scripts/pack_validation")
GEN = PV / "generate_manifest.py"
VER = PV / "verify_manifest.py"
EXC = PV / "pack_excludes.py"

# ---------------------------------------------------------------- new module --
PACK_EXCLUDES_SRC = '''\
"""Shared exclude rules for VALOR manifest tooling (G-19).

Single source of truth used by generate_manifest.py and verify_manifest.py so
they agree on what counts as a pack file. Excluded directories are matched at
ANY depth; generated-file suffixes are excluded everywhere.

NOTE: ".github" is intentionally NOT excluded — CI workflows live there.
"""

EXCLUDE_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".idea",
    ".vscode",
}

EXCLUDE_FILE_SUFFIXES = {".pyc", ".pyo", ".pyd"}


def should_exclude(rel_path: str) -> bool:
    """rel_path: POSIX-style path (forward slashes) relative to the pack root."""
    parts = rel_path.split("/")
    if any(part in EXCLUDE_DIRS for part in parts):
        return True
    if any(rel_path.endswith(suf) for suf in EXCLUDE_FILE_SUFFIXES):
        return True
    return False
'''

# ----------------------------------------------------- generate_manifest.py ---
GEN_OLD_CONSTANTS = '''# Exclude folders that are machine-specific / not part of the pack.
# IMPORTANT: We do NOT exclude ".github" because workflows live there.
EXCLUDE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".ruff_cache",
    ".idea",
    ".vscode",
}

# Exclude common junk / generated files (optional, safe)
EXCLUDE_FILE_SUFFIXES = {".pyc", ".pyo", ".pyd"}'''

GEN_NEW_CONSTANTS = '''# Shared exclude rules (G-19): single source of truth for both manifest scripts.
# IMPORTANT: ".github" is intentionally NOT excluded — workflows live there.
sys.path.insert(0, str(Path(__file__).resolve().parent))
from pack_excludes import should_exclude  # noqa: E402'''

GEN_OLD_FUNC = '''def should_exclude(rel_path: str) -> bool:
    """
    rel_path is POSIX style (forward slashes), relative to pack root.
    """
    parts = rel_path.split("/")
    if parts and parts[0] in EXCLUDE_DIRS:
        return True
    if any(part in EXCLUDE_DIRS for part in parts):
        return True
    if any(rel_path.endswith(suf) for suf in EXCLUDE_FILE_SUFFIXES):
        return True
    return False


'''
GEN_NEW_FUNC = ''  # removed — now imported from pack_excludes

# -------------------------------------------------------- verify_manifest.py --
VER_OLD_IMPORTS = '''import hashlib
import sys
from pathlib import Path'''

VER_NEW_IMPORTS = '''import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from pack_excludes import should_exclude  # noqa: E402'''

VER_OLD_BODY = '''    missing = []
    mismatched = []
    ok_count = 0

    for entry in files:
        rel = entry.get("path")
        expected = entry.get("sha256")
        if not rel or not expected:
            print("ERROR: manifest entry missing `path` or `sha256`.")
            return 2

        p = root / rel
        if not p.exists():
            missing.append(rel)
            continue

        actual = sha256_file(p)
        if actual.lower() != str(expected).lower():
            mismatched.append((rel, expected, actual))
        else:
            ok_count += 1

        manifest_paths = set(e.get("path") for e in files if e.get("path"))
    IGNORE_DIRS = {".venv", "venv", "__pycache__", ".vscode", ".git"}

    actual_paths = set()
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel_path = p.relative_to(root)
        if rel_path.parts and rel_path.parts[0] in IGNORE_DIRS:
            continue
        actual_paths.add(str(rel_path).replace("\\\\", "/"))

    # The manifest is the root of truth; do not treat it as an "extra" file.
    actual_paths.discard("manifest.yaml")
    extras = sorted(actual_paths - manifest_paths)'''

VER_NEW_BODY = '''    missing = []
    mismatched = []
    ok_count = 0

    # Loop-invariant: compute once, not inside the per-entry loop (G-19 smell).
    manifest_paths = set(e.get("path") for e in files if e.get("path"))

    for entry in files:
        rel = entry.get("path")
        expected = entry.get("sha256")
        if not rel or not expected:
            print("ERROR: manifest entry missing `path` or `sha256`.")
            return 2

        p = root / rel
        if not p.exists():
            missing.append(rel)
            continue

        actual = sha256_file(p)
        if actual.lower() != str(expected).lower():
            mismatched.append((rel, expected, actual))
        else:
            ok_count += 1

    # Detect extras using the SHARED exclude rules (any-depth dirs + suffixes),
    # so the verifier and generator agree on what is a pack file (G-19).
    actual_paths = set()
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        rel_posix = p.relative_to(root).as_posix()
        if should_exclude(rel_posix):
            continue
        actual_paths.add(rel_posix)

    # The manifest is the root of truth; do not treat it as an "extra" file.
    actual_paths.discard("manifest.yaml")
    extras = sorted(actual_paths - manifest_paths)'''


def patch(text: str, old: str, new: str, label: str) -> str:
    n = text.count(old)
    if n != 1:
        raise SystemExit(
            f"ABORT: anchor for '{label}' found {n} times (expected exactly 1). "
            f"Source is not the version this script expects — nothing written."
        )
    return text.replace(old, new)


def main() -> int:
    ap = argparse.ArgumentParser(description="A2 integrity-tooling fix (G-19)")
    ap.add_argument("--path", default=".", help="pack root (default: current dir)")
    ap.add_argument("--dry-run", action="store_true", help="report only; write nothing")
    args = ap.parse_args()

    root = Path(args.path).resolve()
    gen, ver, exc = root / GEN, root / VER, root / EXC
    for f in (gen, ver):
        if not f.is_file():
            raise SystemExit(f"ERROR: not found: {f}\n(Run from the pack root.)")

    # Build new contents (validates all anchors before any write).
    gen_text = gen.read_text(encoding="utf-8")
    gen_text = patch(gen_text, GEN_OLD_CONSTANTS, GEN_NEW_CONSTANTS, "generate: constants")
    gen_text = patch(gen_text, GEN_OLD_FUNC, GEN_NEW_FUNC, "generate: should_exclude()")

    ver_text = ver.read_text(encoding="utf-8")
    ver_text = patch(ver_text, VER_OLD_IMPORTS, VER_NEW_IMPORTS, "verify: imports")
    ver_text = patch(ver_text, VER_OLD_BODY, VER_NEW_BODY, "verify: body")

    print("== A2 integrity-tooling fix (G-19) ==")
    print(f"pack root : {root}")
    print(f"write new : {EXC}")
    print(f"patch     : {GEN}")
    print(f"patch     : {VER}")

    if args.dry_run:
        print("\nDRY-RUN: anchors all matched, nothing written.")
        return 0

    exc.write_bytes((PACK_EXCLUDES_SRC).encode("utf-8"))
    gen.write_bytes((gen_text).encode("utf-8"))
    ver.write_bytes((ver_text).encode("utf-8"))

    # ---- self-test: the shared rule now covers the previously-divergent cases
    spec = importlib.util.spec_from_file_location("pack_excludes", exc)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    cases = {
        ".pytest_cache/CACHEDIR.TAG": True,   # nested cache dir — verifier missed it before
        "stray.pyc": True,                    # suffix — verifier had no suffix rule before
        "a/b/c/__pycache__/x.pyc": True,      # deep nesting — top-level-only missed it
        "contracts/VALOR-contract-orch-wp.yaml": False,  # real pack file — must stay
        "schemas/contracts/action_block.schema.json": False,
    }
    bad = [k for k, want in cases.items() if mod.should_exclude(k) != want]
    print("-" * 60)
    if bad:
        print("!! SELF-TEST FAILED for:", bad)
        return 1
    print("SELF-TEST: shared exclude rule correct on all cases "
          "(false-FAIL sources now excluded; real pack files kept).")
    print("\nNext: move this script OUT of the repo, commit, then regenerate")
    print("+ verify the manifest. (pack_excludes.py is new → it will be tracked.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
