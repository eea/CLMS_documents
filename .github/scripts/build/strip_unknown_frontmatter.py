"""
Strip non-allowlisted YAML frontmatter from .qmd files in the build copy.

Runs after group_docs_by_category.py rebuilds DOCS/ and before quarto render.
Source files under origin_DOCS/ are not touched — we clean only the build copy
so Quarto sees a tidy frontmatter no matter what authors leave in source.

Allowlist (matches the PR-time validator in validate_qmd_files.py):
  - author-controlled: title, subtitle, category, date, description, author
  - tool-managed: version (set by ai/update_versions_and_changelogs.py),
    keywords (set by ai/tasks/generate_intros.py), original-filename (set by
    the technical-library scripts)

Anything else (toc/toc-depth/toc-title, deprecated fields, typos, external-
project metadata) gets dropped silently.

Type feature (TYPE_FEATURES):
  The `type` frontmatter field (default: "document") selects a per-document
  rendering profile. Each entry in TYPE_FEATURES may define:
    - extra_fields: additional frontmatter keys allowed for that type on top
      of ALLOWLIST (e.g. "dashboard" documents are allowed `format`, `echo`,
      `code-fold`, `toc`, `toc-depth`).
    - skip_intro / skip_keywords / skip_pdf: flags other pipeline steps can
      check to skip intro generation, keyword tagging, or PDF rendering for
      that type.
  Types not present in TYPE_FEATURES (including the default "document") get
  an empty features dict, i.e. no extra fields and no skip flags. The
  resolved features dict is returned from strip_one() alongside the dropped
  fields so callers can key other pipeline behavior off the same type.

  A `type` value that isn't a string (e.g. a YAML list) is invalid and can't
  be looked up in TYPE_FEATURES; it's dropped from the frontmatter and the
  document falls back to "document". A string value that isn't a key in
  TYPE_FEATURES (typo, unsupported type) triggers a warning and also falls
  back to "document", but the field itself is left in the frontmatter since
  it's still valid YAML.
"""

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent  # .github/scripts
sys.path.insert(0, str(SCRIPTS_ROOT))

from helpers.qmd_utils import read_qmd_frontmatter, write_qmd_frontmatter  # noqa: E402


ALLOWLIST = {
    "title",
    "subtitle",
    "category",
    "date",
    "description",
    "author",
    "version",
    "keywords",
    "original-filename",
    "type",
}

TYPE_FEATURES = {
    "dashboard": {
        "extra_fields": {"format", "echo", "code-fold", "toc", "toc-depth"},
        "skip_intro": True,
        "skip_keywords": True,
        "skip_pdf": True,
    },
    "table": {
        "extra_fields": set(),
        "skip_pdf": True,
    },
}

EXCLUDED_DIRS = {"templates", "theme", "includes", "_meta", "_site", ".quarto"}


def is_excluded(qmd_path: Path, source_root: Path) -> bool:
    rel_parts = qmd_path.relative_to(source_root).parts
    return any(part in EXCLUDED_DIRS for part in rel_parts)


def resolve_type_features(yaml_data: dict, qmd_path: Path) -> tuple[set[str], dict]:
    """Resolve the effective allowlist and TYPE_FEATURES entry for a document.

    Reads the `type` field from yaml_data (default: "document"). If the
    resolved type defines extra_fields, those are added to ALLOWLIST to form
    the effective allowlist. Returns (effective_allowlist, type_features).

    A non-string `type` (e.g. a YAML list) can't be looked up in
    TYPE_FEATURES, so it's treated as invalid: the field is dropped and the
    document falls back to "document". A string `type` that isn't a key in
    TYPE_FEATURES (typo, unsupported type) falls back to "document" too, but
    the field itself is left in place since it's still valid YAML.
    """
    doc_type = yaml_data.get("type", "document")

    if not isinstance(doc_type, str):
        print(f"⚠️  {qmd_path}: type field is not a string ({doc_type!r}); dropping, treating as 'document'")
        return ALLOWLIST - {"type"}, {}

    if doc_type not in TYPE_FEATURES and doc_type != "document":
        print(f"⚠️  {qmd_path}: unknown type '{doc_type}'; treating as 'document'")
        doc_type = "document"

    type_features = TYPE_FEATURES.get(doc_type, {})
    extra_fields = type_features.get("extra_fields", set())
    effective_allowlist = ALLOWLIST | extra_fields
    return effective_allowlist, type_features


def strip_one(qmd_path: Path) -> tuple[bool, list[str], dict]:
    """Return (changed, dropped_field_names, type_features)."""
    yaml_data, lines = read_qmd_frontmatter(qmd_path)
    if not yaml_data or not lines:
        return False, [], {}

    effective_allowlist, type_features = resolve_type_features(yaml_data, qmd_path)

    dropped = sorted(k for k in yaml_data.keys() if k not in effective_allowlist)
    if not dropped:
        return False, [], type_features

    cleaned = {k: v for k, v in yaml_data.items() if k in effective_allowlist}
    write_qmd_frontmatter(qmd_path, cleaned, lines)
    return True, dropped, type_features


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Strip non-allowlisted frontmatter fields from .qmd files"
    )
    parser.add_argument(
        "source",
        nargs="?",
        default=".",
        help="Directory to scan recursively for .qmd files (default: cwd)",
    )
    args = parser.parse_args()

    source_root = Path(args.source).resolve()
    if not source_root.exists():
        print(f"❌ Source directory not found: {source_root}")
        return 1

    qmd_files = [
        p
        for p in source_root.rglob("*.qmd")
        if not is_excluded(p, source_root)
    ]

    print(f"Scanning {len(qmd_files)} .qmd file(s) under {source_root}/")

    changed = 0
    all_dropped: dict[str, int] = {}
    for qmd in sorted(qmd_files):
        was_changed, dropped, _type_features = strip_one(qmd)
        if was_changed:
            changed += 1
            for field in dropped:
                all_dropped[field] = all_dropped.get(field, 0) + 1
            rel = qmd.relative_to(source_root)
            print(f"  • {rel}: stripped {dropped}")

    print(f"\n✅ Stripped frontmatter in {changed}/{len(qmd_files)} file(s)")
    if all_dropped:
        print("   Dropped fields (count across all files):")
        for field in sorted(all_dropped, key=lambda k: -all_dropped[k]):
            print(f"     {all_dropped[field]:3d}  {field}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
