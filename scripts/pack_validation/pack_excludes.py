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

# De-governed process memory: review scaffolding is NOT product spec and is
# excluded from the frozen pack (build-prep freeze-state cleanup). Files stay
# in-repo, ungoverned. Re-govern by removing entries from this set.
EXCLUDE_DEGOVERNED_DIRS = {"_review_control"}


def should_exclude(rel_path: str) -> bool:
    """rel_path: POSIX-style path (forward slashes) relative to the pack root."""
    parts = rel_path.split("/")
    if any(part in EXCLUDE_DIRS or part in EXCLUDE_DEGOVERNED_DIRS for part in parts):
        return True
    if any(rel_path.endswith(suf) for suf in EXCLUDE_FILE_SUFFIXES):
        return True
    return False
