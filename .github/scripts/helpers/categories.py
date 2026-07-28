"""Single-source-of-truth loader for DOCS document categories.

Reads .github/scripts/categories.yml and exposes the category data to the
scripts that need it (validate_qmd_files.py, group_docs_by_category.py). Edit
categories only in categories.yml — never hardcode the list in a script.

Fails loud (sys.exit) on a missing, empty, or malformed file so a broken config
can't silently pass an empty allow-list. Category names are validated to be
lowercase kebab-case and to not collide with reserved/managed directories — a
category routes docs to a folder named after it, so an unchecked name like
`assets` or `_meta` would land documents inside a managed build directory.
"""

import re
import sys
from pathlib import Path

import yaml

CATEGORIES_FILE = Path(__file__).resolve().parent.parent / "categories.yml"

# Category names become output folder names, so they must be safe kebab-case
# tokens and must not collide with the pipeline's managed/excluded directories.
NAME_RE = re.compile(r"^[a-z][a-z0-9-]*$")
RESERVED_DIRS = {"_meta", "assets", "_site", ".quarto", "templates", "theme", "includes"}

_cache = None


def _validate_entries(entries: list) -> list:
    """Validate parsed category entries; raise ValueError on any problem."""
    if not entries:
        raise ValueError("no categories defined")
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError(f"each category must be a mapping, got: {entry!r}")
        name = entry.get("name")
        if not isinstance(name, str) or not NAME_RE.match(name):
            raise ValueError(
                f"category name must be lowercase kebab-case ([a-z][a-z0-9-]*), got: {name!r}"
            )
        if name in seen:
            raise ValueError(f"duplicate category name: {name!r}")
        seen.add(name)
        if "browsable" in entry and not isinstance(entry["browsable"], bool):
            raise ValueError(f"'browsable' must be true/false for {name!r}")
        directory = entry.get("directory", name)
        if not isinstance(directory, str) or not NAME_RE.match(directory):
            raise ValueError(f"invalid 'directory' for {name!r}: {directory!r}")
        if directory in RESERVED_DIRS:
            raise ValueError(
                f"category {name!r} routes to reserved directory {directory!r}"
            )
    return entries


def load_categories() -> list:
    """Return the validated list of category entries (cached)."""
    global _cache
    if _cache is not None:
        return _cache

    if not CATEGORIES_FILE.exists():
        sys.exit(f"❌ categories file not found: {CATEGORIES_FILE}")

    try:
        data = yaml.safe_load(CATEGORIES_FILE.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        sys.exit(f"❌ could not parse {CATEGORIES_FILE}: {e}")

    if not isinstance(data, dict) or not isinstance(data.get("categories"), list):
        sys.exit(f"❌ {CATEGORIES_FILE} must define a 'categories:' list")

    try:
        _cache = _validate_entries(data["categories"])
    except ValueError as e:
        sys.exit(f"❌ {CATEGORIES_FILE}: {e}")
    return _cache


def allowed_names() -> set:
    """Set of category values accepted in `category:` frontmatter."""
    return {e["name"] for e in load_categories()}


def directory_for(category) -> str:
    """Output directory for a category.

    Empty/None -> 'uncategorized' (defensive default; `category` is a required
    frontmatter field, so this rarely fires). Explicit `directory:` wins;
    otherwise the directory is the category name (unknown values pass through).
    """
    if not category:
        return "uncategorized"
    for e in load_categories():
        if e["name"] == category:
            return e.get("directory", category)
    return category


def non_browsable_names() -> set:
    """Categories flagged `browsable: false` (hidden from indexes/sitemaps)."""
    return {e["name"] for e in load_categories() if e.get("browsable", True) is False}


if __name__ == "__main__":
    names = allowed_names()
    assert "products" in names, names
    assert "reports" in names, names
    assert non_browsable_names() == {"non-browsable"}, non_browsable_names()
    assert directory_for("") == "uncategorized"
    assert directory_for("guidelines") == "guidelines"
    assert directory_for("non-browsable") == "non-browsable"

    # The guard must reject bad configs: bad format, reserved dir, duplicate.
    for bad in (
        [{"name": "Bad Name"}],
        [{"name": "assets"}],
        [{"name": "x", "directory": "_meta"}],
        [{"name": "x"}, {"name": "x"}],
    ):
        try:
            _validate_entries(bad)
            raise AssertionError(f"should have rejected {bad!r}")
        except ValueError:
            pass

    print(f"✅ categories.yml OK — allowed: {sorted(names)}")
    print(f"   non-browsable: {sorted(non_browsable_names())}")
