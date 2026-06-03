#!/usr/bin/env python3
"""Fill the version field on every qmd before the render.

Bumps (minor vs patch) only happen on main/test, in update_versions_and_changelogs.py.
The field still has to be present on every render or the index shows a blank
version, so we fill it each build, like intros and changelogs.

The value is the tracked version from .llm_cache/versions.json, looked up via the
original-filename field. No record yet -> {major}.0.0 from the _vN.qmd name. No
bump is computed here.
"""

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # .github/scripts
from helpers.json_io import load_json_or_empty

VERSIONS_FILE = ".llm_cache/versions.json"


def major_from_name(name):
    m = re.search(r"_v(\d+)\.qmd$", name)
    return int(m.group(1)) if m else None


def frontmatter_bounds(lines):
    """(start, end) line indices of the --- ... --- block, or None."""
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return 0, i
    return None


def fm_value(lines, end, key):
    """Read a scalar frontmatter value (good enough for original-filename)."""
    for line in lines[1:end]:
        m = re.match(rf"\s*{re.escape(key)}\s*:\s*(.+?)\s*$", line)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    return None


def set_version(lines, end, version):
    """Replace or insert `version:` in the frontmatter. Returns True if changed."""
    new_line = f"version: {version}\n"
    for i in range(1, end):
        if re.match(r"\s*version\s*:", lines[i]):
            if lines[i] == new_line:
                return False
            lines[i] = new_line
            return True
    lines.insert(1, new_line)
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("docs_dir", help="Directory tree of .qmd files")
    ap.add_argument("--versions-file", default=None)
    args = ap.parse_args()

    repo_root = Path(__file__).resolve().parents[3]  # build -> scripts -> .github -> root
    vf = Path(args.versions_file) if args.versions_file else repo_root / VERSIONS_FILE
    versions = load_json_or_empty(vf, label="versions")

    filled = baseline = 0
    for qmd in sorted(Path(args.docs_dir).rglob("*.qmd")):
        if {"_site", ".quarto", "_meta"} & set(qmd.parts):
            continue
        lines = qmd.read_text(encoding="utf-8").splitlines(keepends=True)
        bounds = frontmatter_bounds(lines)
        if not bounds:
            continue
        _, end = bounds

        src = fm_value(lines, end, "original-filename")
        major = major_from_name(src) if src else None
        if major is None:
            major = major_from_name(qmd.name)
        if major is None:
            print(f"[fill_version] {qmd}: no _vN in filename, skipping")
            continue

        tracked = None
        if src:
            entry = versions.get(f"DOCS/{src}") or versions.get(src)
            tracked = (entry or {}).get("current_version")

        if tracked and tracked.split(".")[0] == str(major):
            version = tracked
        else:
            version = f"{major}.0.0"
            baseline += 1

        if set_version(lines, end, version):
            qmd.write_text("".join(lines), encoding="utf-8")
            filled += 1

    print(
        f"[fill_version] set version on {filled} files "
        f"({baseline} fell back to {{major}}.0.0)"
    )


if __name__ == "__main__":
    main()
