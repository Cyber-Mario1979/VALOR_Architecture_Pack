#!/usr/bin/env python3
"""
apply.py — Phase A / A1 mode rename for the VALOR Architecture Pack.

Renames the engine-authority mode VALUES across the pack, freeing M1-M4
for the Phase-B runtime layer (gap assessment v0.3, G-16):

    M1  ->  DESIGN
    M2  ->  EXECUTION

The match is WORD-BOUNDARY only (\\bM1\\b / \\bM2\\b), so:
  - error codes like MODE_VIOLATION / WRONG_MODE_FOR_COMMIT are untouched
    (they contain no M1/M2 token),
  - tokens such as M10 / M1A are NOT matched,
  - binary files (e.g. architecture_blueprint.png) are skipped.

USAGE
    python3 apply.py              # apply in current dir (must be pack root)
    python3 apply.py --path /repo # apply against a given pack root
    python3 apply.py --dry-run    # show what WOULD change, write nothing
    python3 apply.py --verify     # only check residual state, change nothing

AFTER RUNNING (your steps, per the Phase-A plan):
    git add -A && git commit -m "A1: rename mode values M1/M2 -> DESIGN/EXECUTION (G-16)"
    <regenerate manifest>  &&  <verify manifest>   # expect clean full-tree pass

The manifest WILL mismatch until you regenerate it — that is the designed
pre-freeze state, not an error.
"""

import argparse
import re
import sys
from pathlib import Path

# --- rename rule -------------------------------------------------------------
RENAMES = [
    (re.compile(r"\bM1\b"), "DESIGN"),
    (re.compile(r"\bM2\b"), "EXECUTION"),
]
RESIDUAL = re.compile(r"\bM1\b|\bM2\b")

# Directories never walked into.
SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", ".pytest_cache",
             ".mypy_cache", ".ruff_cache", ".idea", ".vscode", "node_modules"}

# Extensions treated as binary / non-editable up front.
BINARY_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".pdf", ".zip",
              ".gz", ".tar", ".whl", ".ico", ".pyc", ".pyo", ".pyd"}


def is_text(path: Path) -> bool:
    """Skip declared-binary extensions and any file with a NUL byte."""
    if path.suffix.lower() in BINARY_EXT:
        return False
    try:
        chunk = path.read_bytes()[:4096]
    except Exception:
        return False
    return b"\x00" not in chunk


def iter_files(root: Path):
    self_path = Path(__file__).resolve()
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        if p.resolve() == self_path:          # never walk/edit this script itself
            continue
        if any(part in SKIP_DIRS for part in p.relative_to(root).parts):
            continue
        yield p


def apply_to_text(text: str):
    """Return (new_text, total_hits)."""
    hits = 0
    for pat, repl in RENAMES:
        text, n = pat.subn(repl, text)
        hits += n
    return text, hits


def main() -> int:
    ap = argparse.ArgumentParser(description="A1 mode rename: M1->DESIGN, M2->EXECUTION")
    ap.add_argument("--path", default=".", help="pack root (default: current dir)")
    ap.add_argument("--dry-run", action="store_true", help="report only; write nothing")
    ap.add_argument("--verify", action="store_true", help="check residual M1/M2; write nothing")
    args = ap.parse_args()

    root = Path(args.path).resolve()
    if not root.is_dir():
        print(f"ERROR: not a directory: {root}", file=sys.stderr)
        return 2

    # sanity: looks like the pack?
    if not (root / "contracts").is_dir() or not (root / "schemas").is_dir():
        print(f"WARNING: {root} doesn't look like the pack root "
              f"(no contracts/ or schemas/). Continuing anyway.", file=sys.stderr)

    # ---- verify-only mode ----
    if args.verify:
        residual = []
        for p in iter_files(root):
            if not is_text(p):
                continue
            try:
                if RESIDUAL.search(p.read_text(encoding="utf-8")):
                    residual.append(p.relative_to(root))
            except (UnicodeDecodeError, OSError):
                continue
        if residual:
            print(f"RESIDUAL M1/M2 found in {len(residual)} file(s):")
            for r in residual:
                print(f"  {r}")
            return 1
        print("OK: no residual M1/M2 word-boundary tokens in pack text assets.")
        return 0

    # ---- apply / dry-run ----
    changed, total_hits, skipped_binary = [], 0, 0
    for p in iter_files(root):
        if not is_text(p):
            skipped_binary += 1
            continue
        try:
            original = p.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        new, hits = apply_to_text(original)
        if hits:
            total_hits += hits
            changed.append((p.relative_to(root), hits))
            if not args.dry_run:
                p.write_text(new, encoding="utf-8")

    mode = "DRY-RUN (no files written)" if args.dry_run else "APPLIED"
    print(f"== A1 mode rename — {mode} ==")
    print(f"pack root      : {root}")
    print(f"files changed  : {len(changed)}")
    print(f"token replaces : {total_hits}  (M1->DESIGN, M2->EXECUTION)")
    print(f"binaries skipped: {skipped_binary}")
    print("-" * 60)
    for rel, hits in sorted(changed):
        print(f"  {hits:>3}  {rel}")

    # post-apply residual check (skipped on dry-run since nothing was written)
    if not args.dry_run:
        residual = [p.relative_to(root) for p in iter_files(root)
                    if is_text(p) and RESIDUAL.search(p.read_text(encoding="utf-8", errors="ignore"))]
        print("-" * 60)
        if residual:
            print(f"!! RESIDUAL M1/M2 still present in {len(residual)} file(s) — investigate:")
            for r in residual:
                print(f"   {r}")
            return 1
        print("VERIFY: zero residual M1/M2 in pack text assets.")
        print("\nNext: commit, then regenerate + verify the manifest.")
        print("(manifest WILL mismatch until you regenerate it — expected, not an error.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
