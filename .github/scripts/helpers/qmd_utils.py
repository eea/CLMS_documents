"""QMD helpers: frontmatter read/write, file discovery, prompt templating, banners."""

from __future__ import annotations

from pathlib import Path
from typing import Optional
import yaml


def read_qmd_frontmatter(path: Path) -> tuple[dict, list[str]]:
    """Parse a .qmd file's YAML frontmatter, returning (yaml_data, lines).
    yaml_data is {} if there's no valid frontmatter. Pass lines straight back
    to write_qmd_frontmatter with a modified yaml_data to rewrite the file."""
    lines = path.read_text(encoding="utf-8").splitlines()

    if not lines or lines[0].strip() != "---":
        return {}, lines

    try:
        end_idx = lines[1:].index("---") + 1
    except ValueError:
        return {}, lines

    yaml_block = "\n".join(lines[1:end_idx])
    yaml_data = yaml.safe_load(yaml_block) or {}
    return yaml_data, lines


def write_qmd_frontmatter(path: Path, yaml_data: dict, lines: list[str]) -> bool:
    """Write yaml_data back as path's frontmatter, keeping the body from lines.
    Returns False if lines has no recognizable frontmatter block."""
    if not lines or lines[0].strip() != "---":
        return False

    try:
        end_idx = lines[1:].index("---") + 1
    except ValueError:
        return False

    new_yaml_block = yaml.dump(yaml_data, sort_keys=False, allow_unicode=True).strip()
    new_lines = ["---"] + new_yaml_block.splitlines() + ["---"] + lines[end_idx + 1 :]
    path.write_text("\n".join(new_lines), encoding="utf-8")
    return True


def find_qmd_files(
    root_dir: Path, blacklisted_dirs: Optional[set] = None
) -> list[Path]:
    """Sorted list of .qmd files under root_dir, skipping any whose path contains
    a directory named in blacklisted_dirs (e.g. {"templates", "_meta"})."""
    blacklisted_dirs = blacklisted_dirs or set()
    results = []
    for path in sorted(root_dir.rglob("*.qmd")):
        if any(part in blacklisted_dirs for part in path.parts):
            continue
        results.append(path)
    return results


def load_and_fill_prompt_template(
    template_path: Path, num_files: int, file_list
) -> str:
    """Fill a prompt template's {{NUM_FILES}} and {{FILE_LIST}} placeholders.
    file_list becomes a numbered list ("1. name\\n2. ..."), using each item's
    .name attribute when it has one, else its str()."""
    template = template_path.read_text(encoding="utf-8")

    items = []
    for i, f in enumerate(file_list):
        name = f.name if hasattr(f, "name") else str(f)
        items.append(f"{i + 1}. {name}")
    file_list_text = "\n".join(items)

    prompt = template.replace("{{NUM_FILES}}", str(num_files))
    prompt = prompt.replace("{{FILE_LIST}}", file_list_text)
    return prompt


def print_mode_banners(
    testing_mode: bool,
    dry_run: bool,
    testing_extra_lines: Optional[list] = None,
    dry_run_extra_lines: Optional[list] = None,
):
    """Print the TESTING_MODE and/or DRY_RUN banners, each with any extra lines
    the caller wants shown inside it."""
    if testing_mode:
        print("=" * 70)
        print("⚠️  TESTING MODE ENABLED")
        for line in testing_extra_lines or []:
            print(f"   {line}")
        print("   To disable: Remove TESTING_MODE env var or set to 'false'")
        print("=" * 70)

    if dry_run:
        print("=" * 70)
        print("🔍 DRY RUN MODE ENABLED")
        for line in dry_run_extra_lines or []:
            print(f"   {line}")
        print("   To disable: Remove DRY_RUN env var or set to 'false'")
        print("=" * 70)
