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
"""

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
SCRIPTS_ROOT = SCRIPT_DIR.parent  # .github/scripts
sys.path.insert(0, str(SCRIPTS_ROOT))

from helpers.qmd_utils import read_qmd_frontmatter, write_qmd_frontmatter  # noqa: E402
from helpers.doc_types import config_for, DEFAULT_FORMATS  # noqa: E402


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
    # Kept (not stripped) so fill_version / inject_changelog / strip_llms can
    # read it downstream.
    "type",
}

EXCLUDED_DIRS = {"templates", "theme", "includes", "_meta", "_site", ".quarto"}


def is_excluded(qmd_path: Path, source_root: Path) -> bool:
    rel_parts = qmd_path.relative_to(source_root).parts
    return any(part in EXCLUDED_DIRS for part in rel_parts)


def apply_doc_type(fm: dict) -> None:
    """Apply the type config to `fm` in place.

    Only OFF toggles do anything (ON == the default), so an untyped doc is
    untouched. The frontmatter toggles are done here; version/changelog/llms are
    handled later by fill_version / inject_changelog / strip_llms_sidecars, which
    read `type` themselves.
    """
    cfg = config_for(fm.get("type"))
    els = cfg["elements"]

    # OFF actions only (ON == existing default == leave frontmatter untouched).
    if els["toc"] is False:
        fm["toc"] = False
    if els["number-sections"] is False:
        fm["number-sections"] = False
    if els["code"] is False:
        fm["echo"] = False  # hides code source; Quarto tags the cell .hidden
    if els["contact"] is False:
        fm["contact"] = False  # honoured by filters/inject_contact_info.lua
    if els["keywords"] is False:
        fm.pop("keywords", None)  # no project-level keywords default to leak now
    if els["description"] is False:
        fm.pop("description", None)

    # style keys + code-fold off when code is off (project defaults it on, which
    # would leave fold triangles on hidden cells).
    html_opts = dict(cfg["style"])
    if els["code"] is False:
        html_opts["code-fold"] = False

    # A doc `format:` block replaces the project's whole format list (Quarto's
    # one non-merging key), so only write it when we're restricting formats or
    # setting html options — never for the default.
    formats = cfg["formats"]
    if formats != DEFAULT_FORMATS or html_opts:
        fm["format"] = {
            f: (dict(html_opts) if f == "html" and html_opts else "default")
            for f in formats
        }


def strip_one(qmd_path: Path) -> tuple[bool, list[str]]:
    """Return (changed, dropped_field_names)."""
    yaml_data, lines = read_qmd_frontmatter(qmd_path)
    if not yaml_data or not lines:
        return False, []

    dropped = sorted(k for k in yaml_data.keys() if k not in ALLOWLIST)
    cleaned = {k: v for k, v in yaml_data.items() if k in ALLOWLIST}
    apply_doc_type(cleaned)

    if cleaned == yaml_data:  # nothing dropped and no type deviations -> no-op
        return False, []

    write_qmd_frontmatter(qmd_path, cleaned, lines)
    return True, dropped


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
        was_changed, dropped = strip_one(qmd)
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
