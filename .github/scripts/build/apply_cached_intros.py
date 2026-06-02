#!/usr/bin/env python3
"""Apply cached intros/keywords from .llm_cache/ into .qmd frontmatter (no API).

Run before group_docs_by_category - the cache is keyed by the original path.
Usage: apply_cached_intros.py [DOCS_DIR]   # default: DOCS
"""

from __future__ import annotations

import sys
from pathlib import Path

# repo root is three levels up from .github/scripts/build
SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPTS_ROOT))

from helpers.qmd_utils import find_qmd_files  # noqa: E402
from helpers.file_updater import apply_all_updates  # noqa: E402

ROOT_DIR = (SCRIPT_DIR / "../../..").resolve()
CACHE_DIR = (ROOT_DIR / ".llm_cache").resolve()
# skip non-doc dirs, same set as update_documentation.py
BLACKLISTED_DIRS = {
    "templates",
    "includes",
    "theme",
    "_meta",
    "assets",
    "_site",
    ".quarto",
}


def main() -> int:
    docs_arg = sys.argv[1] if len(sys.argv) > 1 else "DOCS"
    input_dir = Path(docs_arg).resolve()

    if not input_dir.is_dir():
        print(f"[apply_cached_intros] '{input_dir}' is not a directory - skipping")
        return 0

    if not CACHE_DIR.is_dir():
        print(f"[apply_cached_intros] no cache at {CACHE_DIR} - nothing to apply")
        return 0

    # cache keys start with the DOCS dir name, so resolve against its parent
    lookup_root = input_dir.parent

    qmd_files = set(find_qmd_files(input_dir, BLACKLISTED_DIRS))
    if not qmd_files:
        print(f"[apply_cached_intros] no .qmd files under {input_dir}")
        return 0

    stats = apply_all_updates(
        qmd_files,
        CACHE_DIR,
        dry_run=False,
        root_dir=lookup_root,
        apply_versions=False,
    )

    # don't fail the build over a frontmatter glitch
    if stats.get("errors"):
        print(f"[apply_cached_intros] done, with {len(stats['errors'])} error(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
