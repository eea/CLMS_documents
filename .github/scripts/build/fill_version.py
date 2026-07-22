#!/usr/bin/env python3
"""Fill the version field on every qmd before the render.

Bumps (minor vs patch) only happen on main/test, in update_versions_and_changelogs.py.
The field still has to be present on every render or the index shows a blank
version, so we fill it each build, like intros and changelogs.

The value is the tracked version from .llm_cache/versions.json, looked up via the
original-filename field. The doc's own `version:` frontmatter is never trusted as
input - it is output we overwrite. No record yet -> seed one (max(major,1).0.0,
so a _v0 or a name without _vN starts at 1.0.0) so the doc becomes tracked. No
bump is computed here.
"""

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))  # .github/scripts
from helpers.json_io import load_json_or_empty
from helpers.doc_types import element_off

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

    filled = baseline = seeded = 0
    today = date.today().isoformat()
    for qmd in sorted(Path(args.docs_dir).rglob("*.qmd")):
        if {"_site", ".quarto", "_meta"} & set(qmd.parts):
            continue
        lines = qmd.read_text(encoding="utf-8").splitlines(keepends=True)
        bounds = frontmatter_bounds(lines)
        if not bounds:
            continue
        _, end = bounds

        # version-off types keep their own `version:` header, if any; don't touch.
        if element_off(fm_value(lines, end, "type"), "version"):
            continue

        src = fm_value(lines, end, "original-filename")
        mj = major_from_name(src) if src else None
        if mj is None:
            mj = major_from_name(qmd.name)
        # First published version is 1.0.0: a _v0 or a name without _vN starts
        # at 1.0.0, while _v4 etc. keep their filename major.
        baseline_major = max(mj, 1) if mj is not None else 1

        key = f"DOCS/{src}" if src else None
        tracked = None
        if key:
            entry = versions.get(key) or versions.get(src)
            tracked = (entry or {}).get("current_version")

        if tracked and (mj is None or tracked.split(".")[0] == str(mj)):
            version = tracked
        else:
            version = f"{baseline_major}.0.0"
            baseline += 1
            # No record yet: seed one so the doc becomes tracked, rather than
            # re-deriving the fallback every build. Keyed by original-filename.
            if key and key not in versions:
                versions[key] = {
                    "current_version": version,
                    "last_bump": "initial",
                    "last_bump_reason": "First release",
                    "last_release_tag": "initial",
                    "last_updated": today,
                    "major_from_filename": baseline_major,
                }
                seeded += 1

        if set_version(lines, end, version):
            qmd.write_text("".join(lines), encoding="utf-8")
            filled += 1

    if seeded:
        vf.parent.mkdir(parents=True, exist_ok=True)
        with vf.open("w", encoding="utf-8") as f:
            json.dump(versions, f, indent=2, sort_keys=True)

    print(
        f"[fill_version] set version on {filled} files "
        f"({baseline} used max(major,1).0.0 baseline, {seeded} new cache entries)"
    )


if __name__ == "__main__":
    main()
