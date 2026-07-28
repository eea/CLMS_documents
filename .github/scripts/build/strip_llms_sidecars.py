#!/usr/bin/env python3
"""Delete the .llms.md sidecar for docs whose type has `llms` off (dashboards).

`llms-txt: true` drops an <name>.llms.md next to every page and has no per-doc
opt-out, so we delete it after render. DOCS/<rel>.qmd -> _site/<rel>.llms.md.

Run before generate_llm_sitemap.py (it falls back to the HTML URL when the file
is gone). Non-browsable docs already lose their llms.txt/sitemap entry via
remove_non_browsable.py; this just clears the orphan file. A browsable llms-off
type would also need its llms.txt entry stripped — deal with that if it happens.

Usage: strip_llms_sidecars.py <docs_dir> <site_dir>   # e.g. . _site
"""

from __future__ import annotations

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR.parent))  # .github/scripts

from helpers.doc_types import element_off  # noqa: E402
from helpers.qmd_utils import read_qmd_frontmatter, find_qmd_files  # noqa: E402

SKIP_DIRS = {"_site", ".quarto", "_meta", "templates", "theme", "includes"}


def main() -> int:
    if len(sys.argv) != 3:
        print("usage: strip_llms_sidecars.py <docs_dir> <site_dir>", file=sys.stderr)
        return 2
    docs_dir = Path(sys.argv[1]).resolve()
    site_dir = Path(sys.argv[2]).resolve()

    removed = 0
    for qmd in find_qmd_files(docs_dir, SKIP_DIRS):
        fm, _ = read_qmd_frontmatter(qmd)
        if not element_off(fm.get("type"), "llms"):
            continue
        sidecar = site_dir / qmd.relative_to(docs_dir).with_suffix(".llms.md")
        if sidecar.exists():
            sidecar.unlink()
            removed += 1
            print(f"  • removed {sidecar.relative_to(site_dir)}")

    print(f"[strip_llms_sidecars] removed {removed} .llms.md sidecar(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
