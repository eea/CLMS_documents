"""Applies all cached updates (intros, keywords, versions) to .qmd frontmatter
in a single write per file."""

from __future__ import annotations

from pathlib import Path
import json
from datetime import datetime

from .qmd_utils import read_qmd_frontmatter, write_qmd_frontmatter
from .json_io import load_json_or_empty


def get_intro_cache_path(qmd_path: Path, cache_dir: Path) -> Path:
    """Convert .qmd path to intro cache file path."""
    safe_path = "__".join(qmd_path.parts)
    return cache_dir / f"{safe_path}.json"


def load_intro_cache(cache_path: Path) -> dict:
    """Load cached intro/keywords."""
    return load_json_or_empty(cache_path, label="intro cache")


def save_intro_cache(cache_path: Path, data: dict) -> None:
    """Persist *data* (intro/keywords) to *cache_path* as indented JSON."""
    with cache_path.open("w") as f:
        json.dump(data, f, indent=2)


def load_versions_metadata(cache_dir: Path) -> dict:
    """Load version metadata from cache."""
    return load_json_or_empty(cache_dir / "versions.json", label="version metadata")


def apply_all_updates(
    files_to_update: set[Path],
    cache_dir: Path,
    dry_run: bool = False,
    root_dir: Path | None = None,
) -> dict:
    """Merge all cached updates into each .qmd's frontmatter, writing each file once.
    Returns a stats dict (files_updated, intros_applied, versions_applied, errors).

    root_dir matters: cache keys are repo-relative, so absolute paths in
    files_to_update are rewritten to that form before lookup — without it every
    lookup silently misses. dry_run shows the changes without writing."""
    print("\n" + "=" * 70)
    print("📝 Applying All Cached Updates to .qmd Files")
    print("=" * 70)

    if dry_run:
        print("[DRY RUN] Showing updates but NOT modifying files\n")

    versions_metadata = load_versions_metadata(cache_dir)

    stats = {
        "files_updated": 0,
        "intros_applied": 0,
        "versions_applied": 0,
        "errors": [],
    }

    for filepath in sorted(files_to_update):
        try:
            yaml_data, lines = read_qmd_frontmatter(filepath)
            if not lines or lines[0].strip() != "---":
                print(f"⚠️  Skipping {filepath.name}: Invalid frontmatter")
                stats["errors"].append(f"{filepath}: Invalid frontmatter")
                continue

            # Cache keys are repo-relative; rewrite absolute paths to match.
            if root_dir is not None and filepath.is_absolute():
                try:
                    lookup_path = filepath.relative_to(root_dir)
                except ValueError:
                    lookup_path = filepath
            else:
                lookup_path = filepath

            modified = False
            updates_desc = []

            # 1. Apply intro/keywords if available
            intro_cache_path = get_intro_cache_path(lookup_path, cache_dir)
            if intro_cache_path.exists():
                intro_data = load_intro_cache(intro_cache_path)
                if intro_data.get("intro"):
                    yaml_data["description"] = (
                        intro_data["intro"].replace("\n", " ").strip()
                    )
                    modified = True
                    updates_desc.append("description")
                if intro_data.get("keywords"):
                    yaml_data["keywords"] = intro_data["keywords"]
                    modified = True
                    updates_desc.append("keywords")
                if modified:
                    stats["intros_applied"] += 1

            # 2. Apply version updates if available
            filepath_str = str(lookup_path)
            if filepath_str in versions_metadata:
                version_data = versions_metadata[filepath_str]
                new_version = version_data.get("current_version")
                if new_version:
                    yaml_data["version"] = new_version
                    yaml_data["date"] = version_data.get(
                        "last_updated", datetime.now().strftime("%Y-%m-%d")
                    )
                    modified = True
                    updates_desc.append(f"version → {new_version}")
                    stats["versions_applied"] += 1

            # 3. Write once if any changes
            if modified:
                if not dry_run:
                    if write_qmd_frontmatter(filepath, yaml_data, lines):
                        stats["files_updated"] += 1
                        print(
                            f"  ✅ Updated {filepath.name} ({', '.join(updates_desc)})"
                        )
                    else:
                        print(f"  ❌ Failed to write {filepath.name}")
                        stats["errors"].append(f"{filepath}: Write failed")
                else:
                    print(
                        f"  [DRY RUN] Would update {filepath.name} ({', '.join(updates_desc)})"
                    )
                    stats["files_updated"] += 1

        except Exception as e:
            print(f"  ❌ Error updating {filepath.name}: {e}")
            stats["errors"].append(f"{filepath}: {e}")

    print("\n✅ File update complete")
    print(f"   Files updated: {stats['files_updated']}")
    print(f"   Intros applied: {stats['intros_applied']}")
    print(f"   Versions applied: {stats['versions_applied']}")
    if stats["errors"]:
        print(f"   ⚠️  Errors: {len(stats['errors'])}")

    return stats
