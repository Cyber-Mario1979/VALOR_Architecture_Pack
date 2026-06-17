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
