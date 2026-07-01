#!/usr/bin/env python3
"""Strip residual block-level HTML wrappers from generated .llms.md sidecars.

The gfm writer + the simplify_tables_gfm.lua filter already linearize tables and
remove styling, but Quarto injects crossref float wrappers (`<div id="tbl-…">` …
`</div>`) and the occasional layout `<div style="overflow-x:…">` AFTER the pandoc
filters run, so they can't be removed at filter level. These bare wrapper lines are
pure noise in the plain-text companion the RAG ingests. This post-render pass removes
standalone block-level `<div>`/`</div>` lines (inline tags like <sub>/<sup> in prose
are left intact).

Idempotent. Usage:
    python3 clean_llms_md.py _site            # walk *.llms.md under a directory
    python3 clean_llms_md.py a.llms.md b.md    # specific files
"""

import re
import sys
from pathlib import Path

# A line that is ONLY an opening/closing <div …> (optionally indented). Block-level
# wrapper noise — never matches inline tags mid-prose.
_BARE_DIV = re.compile(r"^[ \t]*</?div\b[^>]*>[ \t]*$")


def clean_text(text: str) -> str:
    out = [ln for ln in text.split("\n") if not _BARE_DIV.match(ln)]
    cleaned = "\n".join(out)
    # collapse the blank-line runs a removed wrapper can leave behind (3+ → 2)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned


def clean_file(path: Path) -> bool:
    original = path.read_text(encoding="utf-8")
    cleaned = clean_text(original)
    if cleaned != original:
        path.write_text(cleaned, encoding="utf-8")
        return True
    return False


def _iter_targets(args):
    for a in args:
        p = Path(a)
        if p.is_dir():
            yield from p.rglob("*.llms.md")
        elif p.exists():
            yield p


def main(argv) -> int:
    if not argv:
        print(__doc__)
        return 1
    changed = 0
    for path in _iter_targets(argv):
        if clean_file(path):
            changed += 1
    print(f"clean_llms_md: cleaned {changed} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
