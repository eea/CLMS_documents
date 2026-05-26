#!/usr/bin/env python3
"""
Set column widths on every pipe table from its content.

Per column we take the longest unbreakable token as a floor (so a cell
can't overflow its column unless the table just won't fit the page), then
hand out the leftover width in proportion to total content, clamped to
MIN_FLOOR/MAX_CEIL and renormalised to 100%.

The widths get written into the divider row (`|---|---|---|`) as
proportional dash counts — Pandoc reads those as relative column widths, so
it works whether or not the table has a caption. If a caption already
carries a `tbl-colwidths`, we update it too so it doesn't override the
divider with a stale value.

Deterministic, so re-running is a no-op once a table is balanced.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

CHAR_PCT = 100.0 / 70.0       # ~1.43% per char at 9pt over a ~70-char body width
MIN_FLOOR = 5
MAX_CEIL = 65
DIVIDER_TOTAL = 200           # dashes shared out across columns in the rewritten divider

ROW_RE = re.compile(r"^\s*\|(.+)\|\s*$")
DIVIDER_RE = re.compile(r"^\s*\|[-:|\s]+\|\s*$")
CAPTION_RE = re.compile(r"^\s*:\s")
ATTRS_RE = re.compile(r"\{([^}]*)\}\s*$")
COLWIDTHS_VAL_RE = re.compile(r'tbl-colwidths\s*=\s*"\[[^\]]*\]"')

# Characters that introduce a break opportunity in the rendered output.
# en-dash / em-dash included so "LC/LU change 2006–2012" tokenises properly.
TOKEN_SPLIT_RE = re.compile(r"[\s_/?&=\-–—]+")


def cells_of(line: str) -> list[str]:
    m = ROW_RE.match(line)
    return [c.strip() for c in m.group(1).split("|")] if m else []


def parse_pipe_tables(lines: list[str]):
    """Yield (header_idx, divider_idx, last_data_idx, header_cells, data_rows_cells)."""
    i = 0
    while i < len(lines):
        if (
            i + 1 < len(lines)
            and ROW_RE.match(lines[i])
            and DIVIDER_RE.match(lines[i + 1])
            and not DIVIDER_RE.match(lines[i])
        ):
            header_cells = cells_of(lines[i])
            j = i + 2
            data: list[list[str]] = []
            while j < len(lines) and ROW_RE.match(lines[j]) and not DIVIDER_RE.match(lines[j]):
                data.append(cells_of(lines[j]))
                j += 1
            yield (i, i + 1, j - 1, header_cells, data)
            i = j
        else:
            i += 1


def longest_token(text: str) -> int:
    if not text:
        return 0
    tokens = TOKEN_SPLIT_RE.split(text)
    return max((len(t) for t in tokens), default=0)


def compute_pcts(header: list[str], data: list[list[str]]) -> list[int] | None:
    ncols = len(header)
    if ncols < 2:
        return None

    min_tokens: list[int] = []
    weights: list[int] = []
    for c in range(ncols):
        longest = longest_token(header[c])
        total_chars = len(header[c]) + 1
        for row in data:
            cell = row[c] if c < len(row) else ""
            longest = max(longest, longest_token(cell))
            total_chars += len(cell) + 1
        min_tokens.append(max(longest, 1))
        weights.append(max(total_chars, 1))

    min_pcts = [t * CHAR_PCT for t in min_tokens]
    total_min = sum(min_pcts)

    if total_min >= 100:
        scale = 100.0 / total_min
        pcts_f = [p * scale for p in min_pcts]
    else:
        slack = 100.0 - total_min
        total_w = sum(weights)
        pcts_f = [m + slack * w / total_w for m, w in zip(min_pcts, weights)]

    pcts_f = [max(MIN_FLOOR, min(MAX_CEIL, p)) for p in pcts_f]
    pcts = [round(p) for p in pcts_f]
    diff = 100 - sum(pcts)
    if diff != 0:
        idx = pcts.index(max(pcts))
        pcts[idx] += diff
    return pcts


def make_divider(pcts: list[int]) -> str:
    """Rebuild a divider line with dash counts proportional to pcts.
       Pandoc reads dash counts as relative column widths."""
    total = sum(pcts)
    # Each column gets at least 3 dashes (Pandoc minimum); distribute the
    # remaining DIVIDER_TOTAL - 3*N proportionally.
    n = len(pcts)
    base = 3
    pool = max(DIVIDER_TOTAL - n * base, n * base)
    dashes_per_col = [base + round(pool * p / total) for p in pcts]
    return "|" + "|".join("-" * d for d in dashes_per_col) + "|"


def find_caption_idx(lines: list[str], end_idx: int) -> int | None:
    for off in range(1, 6):
        k = end_idx + off
        if k >= len(lines):
            return None
        s = lines[k].strip()
        if not s:
            continue
        if CAPTION_RE.match(lines[k]):
            return k
        return None
    return None


def update_caption_colwidths(caption: str, pcts: list[int]) -> str:
    """Update an existing tbl-colwidths attribute in the caption, if any.
       Does NOT add tbl-colwidths to captions that lack one — the divider
       carries the width info for those."""
    if "tbl-colwidths" not in caption:
        return caption
    new_attr = f'tbl-colwidths="{pcts}"'.replace(" ", "")
    return COLWIDTHS_VAL_RE.sub(new_attr, caption)


def process_file(qmd: Path, overwrite: bool) -> int:
    text = qmd.read_text(encoding="utf-8")
    lines = text.split("\n")
    changes = 0
    tables = list(parse_pipe_tables(lines))
    for _, divider_idx, end_idx, header, data in reversed(tables):
        pcts = compute_pcts(header, data)
        if pcts is None:
            continue

        new_divider = make_divider(pcts)
        # If the current divider already encodes these widths (within
        # rounding), skip — keeps the script idempotent.
        current_divider = lines[divider_idx]
        if not overwrite and current_divider.strip() == new_divider:
            continue
        lines[divider_idx] = new_divider

        cap_idx = find_caption_idx(lines, end_idx)
        if cap_idx is not None:
            new_caption = update_caption_colwidths(lines[cap_idx], pcts)
            if new_caption != lines[cap_idx]:
                lines[cap_idx] = new_caption

        changes += 1

    if changes:
        qmd.write_text("\n".join(lines), encoding="utf-8")
    return changes


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("root")
    ap.add_argument("--overwrite", action="store_true",
                    help="recompute dividers/widths even on already-matching tables")
    args = ap.parse_args()
    root = Path(args.root)
    total = 0
    for qmd in sorted(root.rglob("*.qmd")):
        n = process_file(qmd, args.overwrite)
        if n:
            print(f"  set widths on {n:3d} tables in {qmd.relative_to(root)}")
            total += n
    print()
    print(f"total tables modified: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
