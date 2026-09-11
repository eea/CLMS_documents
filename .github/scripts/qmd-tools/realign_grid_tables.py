#!/usr/bin/env python3
"""
Re-pad grid-table rows whose pipes drifted off the border columns.

Anything that edits text inside a grid cell without re-padding it - an upstream
media-path rewrite, group_docs_by_category's `{stem}-media/` rename, the
fig-alt that inject_image_descriptions bakes into images - leaves that row
wider than its border. Pandoc then mis-parses the whole table and Typst dies on
the stray empty cell ("error: unexpected comma"). We split drifted rows on
their pipes and re-pad every row to the border columns, widening a column when
a cell no longer fits. Tables with merged cells are left alone.

Run it last, after every other qmd rewrite. Idempotent: aligned tables are
never touched.
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

from fix_table_colwidths import _is_grid_border


def realign_block(block: list[str]) -> list[str]:
    """Return the grid block re-padded to its border columns, or unchanged."""
    borders = [ln.rstrip() for ln in block if _is_grid_border(ln)]
    plus = [i for i, ch in enumerate(borders[0]) if ch == "+"]
    if any([i for i, ch in enumerate(b) if ch == "+"] != plus for b in borders):
        return block  # merged cells split the borders - not ours to touch
    ncol = len(plus) - 1

    rows: list[list[str] | None] = []
    drifted = False
    for ln in block:
        ln = ln.rstrip()
        if _is_grid_border(ln):
            rows.append(None)
        elif [i for i, ch in enumerate(ln) if ch == "|"] == plus:
            rows.append([ln[a + 1 : b].rstrip() for a, b in zip(plus, plus[1:])])
        elif ln.count("|") == ncol + 1:
            rows.append([c.rstrip() for c in ln.strip().split("|")[1:-1]])
            drifted = True
        else:
            return block  # spanning cell or literal pipe - columns are ambiguous
    if not drifted:
        return block

    # ponytail: len() counts code points, pandoc counts display width - wide
    # (CJK) chars would still drift; use unicodedata.east_asian_width if needed.
    widths = [b - a - 1 for a, b in zip(plus, plus[1:])]
    need = [max([len(r[c]) for r in rows if r] + [0]) for c in range(ncol)]
    # When a cell outgrows its column (a long fig-alt), scale *every* column by
    # the same factor: Pandoc reads grid widths as ratios, so the PDF layout
    # stays as authored instead of squashing the other columns.
    scale = max([n / max(w, 1) for n, w in zip(need, widths)] + [1.0])
    widths = [max(n, math.ceil(w * scale)) for n, w in zip(need, widths)]

    indent = " " * plus[0]
    out = []
    for ln, row in zip(block, rows):
        if row is None:
            ln = ln.rstrip()
            segs = [ln[a + 1 : b] for a, b in zip(plus, plus[1:])]
            # Widen by repeating the rule char after the first char, so ':'
            # alignment markers stay at the ends.
            segs = [s[:1] + ("=" if "=" in s else "-") * (w - len(s)) + s[1:]
                    for s, w in zip(segs, widths)]
            out.append(indent + "+" + "+".join(segs) + "+")
        else:
            out.append(indent + "|" + "|".join(c.ljust(w) for c, w in zip(row, widths)) + "|")
    return out


def realign_text(text: str) -> tuple[str, int]:
    """Realign every grid table in text. Returns (text, tables_changed)."""
    lines = text.split("\n")
    changed = 0
    i = 0
    while i < len(lines):
        if not _is_grid_border(lines[i]):
            i += 1
            continue
        # Same block detection as fix_table_colwidths: border to last border.
        j, last = i, i
        while j < len(lines) and (
            _is_grid_border(lines[j]) or lines[j].lstrip().startswith("|")
        ):
            if _is_grid_border(lines[j]):
                last = j
            j += 1
        block = realign_block(lines[i : last + 1])
        if block != lines[i : last + 1]:
            lines[i : last + 1] = block
            changed += 1
        i = last + 1
    return "\n".join(lines), changed


def main() -> int:
    root = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
    total = 0
    for qmd in sorted(root.rglob("*.qmd")):
        text, n = realign_text(qmd.read_text(encoding="utf-8"))
        if n:
            qmd.write_text(text, encoding="utf-8")
            print(f"  realigned {n:3d} grid tables in {qmd.relative_to(root)}")
            total += n
    print(f"total grid tables realigned: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
