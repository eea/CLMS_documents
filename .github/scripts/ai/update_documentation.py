#!/usr/bin/env python3
"""Unified documentation updater: runs the versions/changelogs and intros/keywords
tasks (sharing one rate-limit budget), then writes results back to .qmd frontmatter.

All file writes are deferred until both tasks finish, so the git working tree stays
clean during analysis, each file is written once, and the version task sees the true
pre-update state."""

from __future__ import annotations

import argparse
import json
import sys
import os
import time
import traceback
from pathlib import Path

# Add scripts directories to path
SCRIPT_DIR = Path(__file__).resolve().parent          # .github/scripts/ai
SCRIPTS_ROOT = SCRIPT_DIR.parent                      # .github/scripts
sys.path.insert(0, str(SCRIPT_DIR))
sys.path.insert(0, str(SCRIPTS_ROOT))

from helpers.gemini_client import setup_gemini, rate_limit_state, RPD_LIMIT, TPM_SAFE  # noqa: E402
from helpers.qmd_utils import print_mode_banners, find_qmd_files  # noqa: E402
from helpers.file_updater import apply_all_updates, get_intro_cache_path  # noqa: E402
from tasks import generate_intros  # noqa: E402


# Repo-relative path constants (resolved once at import time).
# SCRIPT_DIR is .github/scripts/ai, so the repo root is three levels up.
ROOT_DIR = (SCRIPT_DIR / "../../..").resolve()
INPUT_DIR = (ROOT_DIR / "DOCS").resolve()
CACHE_DIR = (ROOT_DIR / ".llm_cache").resolve()
BLACKLISTED_DIRS = {
    "templates",
    "includes",
    "theme",
    "_meta",
    "assets",
    "_site",
    ".quarto",
}


def run_intros_task(
    model,
    modified_files_path: Path,
    dry_run: bool,
    testing: bool,
    bump_levels: dict | None = None,
) -> set:
    """Generate intros/keywords for the modified files and return the set of files
    that ended up with a cache entry. bump_levels is handed over in-memory from the
    versioning task so it doesn't have to re-read versions.json."""
    modified_files = []
    if modified_files_path and modified_files_path.exists():
        with modified_files_path.open() as f:
            modified_files = [line.strip() for line in f if line.strip()]

    if not modified_files and not testing:
        print("\n⚠️  No modified files to process for intros")
        return set()

    CACHE_DIR.mkdir(exist_ok=True)

    generate_intros.run(
        model=model,
        modified_files_list=modified_files,
        input_dir=INPUT_DIR,
        root_dir=ROOT_DIR,
        cache_dir=CACHE_DIR,
        blacklisted_dirs=BLACKLISTED_DIRS,
        dry_run=dry_run,
        testing=testing,
        max_files_for_testing=3,
        bump_levels=bump_levels,
    )

    all_files = set()
    for full_doc_path in find_qmd_files(INPUT_DIR, BLACKLISTED_DIRS):
        doc_path = full_doc_path.relative_to(ROOT_DIR)
        cache_path = get_intro_cache_path(doc_path, CACHE_DIR)
        if cache_path.exists():
            all_files.add(doc_path)

    return all_files


def run_versions_task(dry_run: bool, testing: bool) -> tuple[set, dict]:
    """Run the version/changelog analysis. Returns (files_to_update, bump_levels),
    where bump_levels maps filepath → "minor"/"patch". Both are read from
    versions.json in one pass so the intros task doesn't have to re-read it."""
    # Cache-only mode: analyse and write versions.json, but skip the inline .qmd writes.
    os.environ["SKIP_FILE_WRITES"] = "true"
    if dry_run:
        os.environ["DRY_RUN"] = "true"
    if testing:
        os.environ["TESTING_MODE"] = "true"

    try:
        # Import and run the versions script.
        # It saves results to .llm_cache/versions.json but does NOT write .qmd files
        # (SKIP_FILE_WRITES gates the inline qmd writes — Phase 2 owns the writes).
        import update_versions_and_changelogs

        update_versions_and_changelogs.main()

        # Read versions.json once — extract both the file set and bump levels
        versions_file = CACHE_DIR / "versions.json"

        files_to_update: set = set()
        bump_levels: dict = {}

        if versions_file.exists():
            with versions_file.open() as f:
                versions_metadata = json.load(f)

            for filepath_str, meta in versions_metadata.items():
                files_to_update.add(Path(filepath_str))
                level = meta.get("last_bump", "").lower()
                if level in ("minor", "patch"):
                    bump_levels[filepath_str] = level

        if bump_levels:
            print(f"[INFO] Extracted bump levels for {len(bump_levels)} file(s)")

        return files_to_update, bump_levels

    finally:
        os.environ.pop("SKIP_FILE_WRITES", None)
        if dry_run:
            os.environ.pop("DRY_RUN", None)
        if testing:
            os.environ.pop("TESTING_MODE", None)


def main():
    """Main entry point for unified documentation updates."""
    parser = argparse.ArgumentParser(
        description="Update CLMS documentation metadata (intros, keywords, versions, changelogs)"
    )
    parser.add_argument(
        "--intros",
        metavar="FILE",
        type=Path,
        help="Generate intros/keywords for files listed in FILE (one path per line)",
    )
    parser.add_argument(
        "--versions",
        action="store_true",
        help="Update versions and changelogs based on git history",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without making API calls or modifying files",
    )
    parser.add_argument(
        "--testing",
        action="store_true",
        help="Enable testing mode (process only first 3 files)",
    )
    parser.add_argument(
        "--skip-file-updates",
        action="store_true",
        help="Skip Phase 2 (file write-back) - useful for testing LLM tasks only",
    )

    args = parser.parse_args()

    if not args.intros and not args.versions:
        print("❌ Error: Must specify at least one of --intros or --versions")
        parser.print_help()
        sys.exit(1)

    print_mode_banners(
        testing_mode=args.testing,
        dry_run=args.dry_run,
        testing_extra_lines=[
            "Max files to process: 3 per task",
            "⚠️  WARNING: Only a subset of files will be processed!",
        ],
        dry_run_extra_lines=[
            "Will show mock results but NOT make API calls",
            "No files will be modified",
        ],
    )

    _t_total_start = time.perf_counter()

    api_key = os.getenv("GEMINI_API_KEY")
    model = setup_gemini(api_key, dry_run=args.dry_run)

    CACHE_DIR.mkdir(exist_ok=True)

    files_needing_updates = set()

    try:
        # PHASE 1: LLM Analysis (saves to .llm_cache/ only)
        print("\n" + "=" * 70)
        print("PHASE 1: LLM Analysis (No .qmd File Modifications)")
        print("=" * 70)

        # Task 1: Versions (must run BEFORE intros so bump levels are available)
        bump_levels: dict = {}
        if args.versions:
            print("\n" + "-" * 70)
            version_files, bump_levels = run_versions_task(args.dry_run, args.testing)
            files_needing_updates.update(version_files)
            print(
                f"\n[INFO] Version task cached results for {len(version_files)} files"
            )

        # Task 2: Intros (receives bump levels in-memory — no extra file I/O)
        if args.intros:
            intro_files = run_intros_task(
                model,
                args.intros,
                args.dry_run,
                args.testing,
                bump_levels=bump_levels if bump_levels else None,
            )
            files_needing_updates.update(intro_files)
            print(f"\n[INFO] Intro task cached results for {len(intro_files)} files")

        # PHASE 2: Apply All Updates
        if not args.skip_file_updates and files_needing_updates:
            print("\n" + "=" * 70)
            print("PHASE 2: Applying All Updates to .qmd Files")
            print("=" * 70)

            # Resolve relative paths (e.g. DOCS/...) against the repo root
            resolved_files = {
                ROOT_DIR / fp if not Path(fp).is_absolute() else Path(fp)
                for fp in files_needing_updates
            }
            apply_all_updates(
                resolved_files,
                CACHE_DIR,
                dry_run=args.dry_run,
                root_dir=ROOT_DIR,
            )

        print("\n" + "=" * 70)
        print("📊 SESSION SUMMARY")
        print("=" * 70)
        print(
            f"Total API requests: {rate_limit_state['requests_today']}/{RPD_LIMIT:,} daily limit"
        )
        print(
            f"Total tokens: {rate_limit_state['tokens_minute']:,}/{TPM_SAFE:,} per-minute capacity"
        )

        _t_total_end = time.perf_counter()
        print(f"Total time: {_t_total_end - _t_total_start:.2f}s")

    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
        sys.exit(1)
    except Exception:
        print("\n\n❌ Error:")
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
