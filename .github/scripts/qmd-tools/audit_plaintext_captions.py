#!/usr/bin/env python3
"""
Audit for table/figure captions rendered as plain body text (read-only).

A caption is BROKEN when a bare `Table N:` / `*Table N:*` / `Figure N:` paragraph
sits adjacent to a float but is not annotated as that float's caption. A float is
a markdown pipe table, a `{=html}` table block, or a standalone `![](...)` image
(table-as-image / figure). Runs of 3+ consecutive caption paragraphs are treated
as a "List of Tables/Figures" index and skipped.

This is the verification companion to promote_bare_captions.py: after promotion it
should report 0 (any remainder is an ambiguous cluster left for manual fixing).
Exit code is non-zero when findings remain, so it can gate a build.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

_TBL = re.compile(r"^\s*\*{0,2}\s*Table\s+\d+\s*[.:]", re.I)
_FIG = re.compile(r"^\s*\*{0,2}\s*Figure\s+\d+\s*[.:]", re.I)
_IMG = re.compile(r"^\s*!\[(?P<alt>.*?)\]\(")
_EMPTY_IMG = re.compile(r"^\s*!\[\s*\]\(")
_ROW = re.compile(r"^\s*\|.*\|\s*$")
_HTML_OPEN = re.compile(r"^\s*```\{=html\}\s*$")
_FENCE = re.compile(r"^\s*```\s*$")
_CAPDIV = re.compile(r"^\s*:::\s*\{\.tbl-caption\}")
_DIVCLOSE = re.compile(r"^\s*:::\s*$")


def _nb(lines, k, step):
    j = k + step
    while 0 <= j < len(lines) and not lines[j].strip():
        j += step
    return j


def _is_float(lines, k):
    if k < 0 or k >= len(lines):
        return False
    s = lines[k]
    return bool(_ROW.match(s) or _HTML_OPEN.match(s) or _FENCE.match(s)
                or _IMG.match(s) or s.lstrip().startswith("</table"))


def _in_capdiv(lines, i):
    for k in range(i - 1, -1, -1):
        if _CAPDIV.match(lines[k]):
            return True
        if _DIVCLOSE.match(lines[k]):
            return False
    return False


def _index_lines(lines):
    out = set()
    i = 0
    while i < len(lines):
        if (_TBL.match(lines[i]) or _FIG.match(lines[i])) and not _IMG.match(lines[i]):
            members, j = [], i
            while j < len(lines):
                if (_TBL.match(lines[j]) or _FIG.match(lines[j])) and not _IMG.match(lines[j]):
                    members.append(j)
                    j += 1
                elif not lines[j].strip():
                    j += 1
                else:
                    break
            if len(members) >= 3:
                out.update(members)
            i = j
        else:
            i += 1
    return out


def audit_file(path: Path):
    lines = path.read_text(encoding="utf-8").split("\n")
    idx = _index_lines(lines)
    rows = []
    for i, ln in enumerate(lines):
        if i in idx or _IMG.match(ln):
            continue
        if _TBL.match(ln) and not _in_capdiv(lines, i):
            p, n = _nb(lines, i, -1), _nb(lines, i, 1)
            if _is_float(lines, n) or _is_float(lines, p):
                rows.append((i + 1, "TABLE", ln.strip()[:70]))
        elif _FIG.match(ln):
            p, n = _nb(lines, i, -1), _nb(lines, i, 1)
            if (n < len(lines) and _IMG.match(lines[n])) or (p >= 0 and _IMG.match(lines[p])):
                rows.append((i + 1, "FIGURE", ln.strip()[:70]))
    return rows


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("root", nargs="?", default="DOCS", help="dir scanned recursively for *.qmd")
    args = ap.parse_args()
    root = Path(args.root)
    total = 0
    for qmd in sorted(root.rglob("*.qmd")):
        rows = audit_file(qmd)
        if rows:
            print(f"\n### {qmd}")
            for line_no, kind, txt in rows:
                print(f"  L{line_no}  {kind:6}  {txt}")
            total += len(rows)
    print(f"\nplain-text captions found: {total}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main())
