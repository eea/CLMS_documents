"""
Validate YAML frontmatter on source .qmd files (PR-time gate).

Checks:
  - required fields present: title, subtitle, category, date
  - category in {guidelines, products, uncategorized, non-browsable}
  - date is YYYY-MM-DD
  - title / subtitle are non-empty strings
  - description / author, if present, have the right types

Not checked:
  - version / keywords / original-filename — set by the build pipeline, not
    the author.
  - toc / toc-depth / toc-title — Quarto handles defaults; build phase strips
    them anyway.
  - unknown fields — ignored here. The render-time strip step drops them,
    so source files can carry extra metadata without breaking the build.
"""

import argparse
import datetime as _dt
import os
import re
import sys
from pathlib import Path
from typing import Dict, List

import yaml


# Run from repo root so default --source resolves correctly.
script_dir = Path(__file__).parent
root_dir = (script_dir / "../..").resolve()
os.chdir(root_dir)


DOCS_DIR = "DOCS"
EXCLUDED_DOCS_DIRS = {"templates", "theme", "includes", "_meta"}

ALLOWED_CATEGORIES = {"guidelines", "products", "uncategorized", "non-browsable"}
REQUIRED_FIELDS = ("title", "subtitle", "category", "date")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def extract_yaml_header(file_path: Path) -> Dict:
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return {"__error__": f"could not read file: {e}"}

    yaml_match = re.search(r"^---\s*\n(.*?)\n---", content, re.DOTALL | re.MULTILINE)
    if not yaml_match:
        return {"__error__": "no YAML frontmatter (missing --- delimiters)"}

    try:
        metadata = yaml.safe_load(yaml_match.group(1))
    except yaml.YAMLError as e:
        return {"__error__": f"YAML parse error: {e}"}

    if metadata is None:
        return {"__error__": "empty YAML frontmatter"}
    if not isinstance(metadata, dict):
        return {"__error__": f"frontmatter must be a mapping, got {type(metadata).__name__}"}

    return metadata


def validate_qmd(file_path: Path) -> List[str]:
    """Return a list of human-readable issues; empty list means valid."""
    metadata = extract_yaml_header(file_path)
    if "__error__" in metadata:
        return [metadata["__error__"]]

    issues: List[str] = []

    # Required fields present
    for field in REQUIRED_FIELDS:
        if field not in metadata:
            issues.append(f"missing required field: {field!r}")

    # Type / value checks for fields that ARE present
    title = metadata.get("title")
    if title is not None:
        if not isinstance(title, str) or not title.strip():
            issues.append("title must be a non-empty string")

    subtitle = metadata.get("subtitle")
    if subtitle is not None:
        if not isinstance(subtitle, str) or not subtitle.strip():
            issues.append("subtitle must be a non-empty string")

    category = metadata.get("category")
    if category is not None and category not in ALLOWED_CATEGORIES:
        issues.append(
            f"invalid category {category!r}; allowed: {sorted(ALLOWED_CATEGORIES)}"
        )

    date_v = metadata.get("date")
    if date_v is not None:
        if isinstance(date_v, _dt.date):
            # YAML parsed bare YYYY-MM-DD — fine.
            pass
        elif isinstance(date_v, str):
            if not DATE_PATTERN.match(date_v):
                issues.append(f"date must be YYYY-MM-DD, got {date_v!r}")
        else:
            issues.append(
                f"date must be YYYY-MM-DD string, got {type(date_v).__name__}"
            )

    description = metadata.get("description")
    if description is not None and not isinstance(description, str):
        issues.append("description, if present, must be a string")

    author = metadata.get("author")
    if author is not None and not isinstance(author, (str, list)):
        issues.append("author, if present, must be a string or list of strings")

    return issues


def find_qmd_files(source_path: Path) -> List[Path]:
    return [
        f
        for f in source_path.glob("**/*.qmd")
        if not any(
            part in EXCLUDED_DOCS_DIRS
            for part in f.relative_to(source_path).parent.parts
        )
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate .qmd frontmatter")
    parser.add_argument(
        "--source",
        "-s",
        default=DOCS_DIR,
        help=f"Source directory to scan (default: {DOCS_DIR})",
    )
    args = parser.parse_args()

    source_path = Path(args.source)
    if not source_path.exists():
        print(f"❌ Source directory not found: {source_path}")
        return 1

    qmd_files = find_qmd_files(source_path)
    if not qmd_files:
        print("No .qmd files found.")
        return 0

    print(f"Validating {len(qmd_files)} .qmd file(s) under {source_path}/")
    print(f"Required fields: {', '.join(REQUIRED_FIELDS)}")
    print(f"Allowed categories: {sorted(ALLOWED_CATEGORIES)}")
    print("-" * 60)

    invalid = 0
    for qmd in sorted(qmd_files):
        issues = validate_qmd(qmd)
        rel = qmd.resolve().relative_to(Path.cwd())
        if issues:
            invalid += 1
            print(f"❌ {rel}")
            for issue in issues:
                print(f"     • {issue}")
        # Silent on success to keep CI logs short.

    print("-" * 60)
    if invalid:
        print(f"❌ {invalid}/{len(qmd_files)} file(s) failed validation")
        return 1
    print(f"✅ All {len(qmd_files)} file(s) valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
