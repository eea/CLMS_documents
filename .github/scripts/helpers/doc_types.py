"""Loads doc-types.yml. Same shape as categories.py.

Read by validate_qmd_files, strip_unknown_frontmatter, fill_version and
strip_llms_sidecars. Edit types in the yaml, not here. Bad config sys.exit()s
rather than passing silently, so a typo like `tocc: false` fails the build.

The `document` type is all-on, which matches the existing pipeline defaults,
so untyped docs render exactly as before.
"""

import re
import sys
from pathlib import Path

import yaml

DOC_TYPES_FILE = Path(__file__).resolve().parent.parent / "doc-types.yml"

DEFAULT_TYPE = "document"
NAME_RE = re.compile(r"^[a-z][a-z0-9-]*$")

# Element toggles. On == current pipeline default; a new one does nothing until
# some step actually reads it.
KNOWN_TOGGLES = {
    "toc",
    "keywords",
    "description",
    "version",
    "changelog",
    "contact",
    "code",
    "number-sections",
    "llms",
}
KNOWN_FORMATS = {"html", "typst", "gfm"}
DEFAULT_FORMATS = ["html", "typst", "gfm"]

_cache = None


def _validate_entries(entries: list) -> list:
    """Validate parsed type entries; raise ValueError on any problem."""
    if not entries:
        raise ValueError("no types defined")
    seen = set()
    for entry in entries:
        if not isinstance(entry, dict):
            raise ValueError(f"each type must be a mapping, got: {entry!r}")
        name = entry.get("name")
        if not isinstance(name, str) or not NAME_RE.match(name):
            raise ValueError(
                f"type name must be lowercase kebab-case ([a-z][a-z0-9-]*), got: {name!r}"
            )
        if name in seen:
            raise ValueError(f"duplicate type name: {name!r}")
        seen.add(name)

        elements = entry.get("elements", {})
        if not isinstance(elements, dict):
            raise ValueError(f"'elements' must be a mapping for {name!r}")
        for key, val in elements.items():
            if key not in KNOWN_TOGGLES:
                raise ValueError(
                    f"unknown element toggle {key!r} in {name!r}; known: {sorted(KNOWN_TOGGLES)}"
                )
            if not isinstance(val, bool):
                raise ValueError(f"toggle {key!r} in {name!r} must be true/false, got {val!r}")

        formats = entry.get("formats")
        if formats is not None:
            if not isinstance(formats, list) or not formats:
                raise ValueError(f"'formats' must be a non-empty list for {name!r}")
            bad = [f for f in formats if f not in KNOWN_FORMATS]
            if bad:
                raise ValueError(
                    f"unknown format(s) {bad!r} in {name!r}; known: {sorted(KNOWN_FORMATS)}"
                )

        style = entry.get("style")
        if style is not None and not isinstance(style, dict):
            raise ValueError(f"'style' must be a mapping for {name!r}")

    if DEFAULT_TYPE not in seen:
        raise ValueError(f"a type named {DEFAULT_TYPE!r} (the default) must be defined")
    return entries


def load_types() -> list:
    """Return the validated list of type entries (cached)."""
    global _cache
    if _cache is not None:
        return _cache

    if not DOC_TYPES_FILE.exists():
        sys.exit(f"❌ doc-types file not found: {DOC_TYPES_FILE}")

    try:
        data = yaml.safe_load(DOC_TYPES_FILE.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        sys.exit(f"❌ could not parse {DOC_TYPES_FILE}: {e}")

    if not isinstance(data, dict) or not isinstance(data.get("types"), list):
        sys.exit(f"❌ {DOC_TYPES_FILE} must define a 'types:' list")

    try:
        _cache = _validate_entries(data["types"])
    except ValueError as e:
        sys.exit(f"❌ {DOC_TYPES_FILE}: {e}")
    return _cache


def allowed_names() -> set:
    """Set of values accepted in `type:` frontmatter."""
    return {e["name"] for e in load_types()}


def config_for(name) -> dict:
    """Resolved config: {name, elements(all bools), formats, style}.

    Unknown/None falls back to the default type (bad names are caught earlier by
    validate_qmd_files). Toggles not listed default to True.
    """
    entries = {e["name"]: e for e in load_types()}
    entry = entries.get(name) or entries[DEFAULT_TYPE]
    elements = {t: True for t in KNOWN_TOGGLES}
    elements.update(entry.get("elements", {}))
    return {
        "name": entry["name"],
        "elements": elements,
        "formats": list(entry.get("formats", DEFAULT_FORMATS)),
        "style": dict(entry.get("style", {})),
    }


def element_off(name, toggle) -> bool:
    """True iff `toggle` is OFF for type `name` (default type -> everything on)."""
    if toggle not in KNOWN_TOGGLES:
        raise KeyError(f"unknown toggle {toggle!r}")
    return config_for(name)["elements"][toggle] is False


if __name__ == "__main__":
    names = allowed_names()
    assert DEFAULT_TYPE in names, names
    assert "dashboard" in names, names

    doc = config_for("document")
    assert all(doc["elements"].values()), doc  # default type: everything on
    assert doc["formats"] == DEFAULT_FORMATS, doc
    assert doc["style"] == {}, doc

    dash = config_for("dashboard")
    assert dash["elements"]["toc"] is False, dash
    assert dash["elements"]["llms"] is False, dash
    assert dash["formats"] == ["html"], dash
    assert dash["style"] == {"page-layout": "full"}, dash

    # Unknown / missing name falls back to the default type (all on).
    assert config_for("nope")["name"] == DEFAULT_TYPE
    assert config_for(None)["name"] == DEFAULT_TYPE
    assert element_off("dashboard", "version") is True
    assert element_off("document", "version") is False
    assert element_off("nope", "version") is False

    # Validation must reject bad configs.
    for bad in (
        [],
        [{"name": "Bad Name"}],
        [{"name": "x"}, {"name": "x"}],
        [{"name": "x", "elements": {"tocc": False}}],       # unknown toggle
        [{"name": "x", "elements": {"toc": "no"}}],          # non-bool
        [{"name": "x", "formats": ["pdf"]}],                 # unknown format
        [{"name": "x", "formats": []}],                      # empty formats
        [{"name": "notdefault"}],                            # missing 'document'
    ):
        try:
            _validate_entries(bad)
            raise AssertionError(f"should have rejected {bad!r}")
        except ValueError:
            pass

    print(f"✅ doc-types.yml OK — types: {sorted(names)}")
