# VENDORED VERBATIM from .github/scripts/qmd-tools/fix_table_colwidths.py
# Copy kept in-tree so the standalone pdf_to_qmd tool stays decoupled from CI.
# If the production script changes, re-sync this copy (diff against source).
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
# A real divider must contain at least one dash. Without that, a blank grid-table
# continuation row (`|   |   |`) matches and gets mistaken for a pipe divider.
DIVIDER_RE = re.compile(r"^\s*\|[:|\s]*-[-:|\s]*\|\s*$")
CAPTION_RE = re.compile(r"^\s*:\s")
ATTRS_RE = re.compile(r"\{([^}]*)\}\s*$")
COLWIDTHS_VAL_RE = re.compile(r'tbl-colwidths\s*=\s*"\[[^\]]*\]"')

# Where the column-floor logic is allowed to split a token. Hyphens, dashes AND
# slashes are deliberately NOT here - Typst doesn't reliably break at them in
# narrow table cells, so we treat e.g. "2022-04-08", "14/05/2008", or
# "state-of-the-art" as one unbreakable token and size the column for the whole
# thing. (Slashes were splittable before, which under-sized date columns like
# "14/05/2008" — the cell rendered the full 10 chars and overflowed.)
TOKEN_SPLIT_RE = re.compile(r"[\s_?&=]+")


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


# ─────────────────────────────────────────────────────────────────────────
# Grid and multiline tables -> pipe tables
#
# The width logic above only understands pipe tables. docx imports also bring
# grid tables (+---+ borders) and multiline tables (dash-rule columns), whose
# widths come straight from the source dash runs and are usually lopsided. We
# convert the simple text ones to pipe tables so they get balanced too. Anything
# with a list, image, or other block content in a cell is left untouched - we
# can't flatten that into a pipe row without losing it.
# ─────────────────────────────────────────────────────────────────────────

# A list bullet inside a cell - can't flatten that into a pipe row.
LIST_BULLET_RE = re.compile(r"\|\s*([-*+]|\d+\.)\s")


def _is_grid_border(line: str) -> bool:
    s = line.strip()
    return len(s) >= 3 and s[0] == "+" and s[-1] == "+" and set(s) <= set("+-=: ")


def _esc_pipe(s: str) -> str:
    return s.replace("|", r"\|").strip()


def grid_block_to_pipe(block: list[str]) -> list[str] | None:
    """Convert a grid-table block to pipe lines, or None if too complex.

    Only regular text tables. Skip anything with an image, a list, or merged
    cells (a content row whose pipe count is off) - pipe tables can't hold those.
    Multi-paragraph cells are kept, with paragraphs joined by <br><br>.
    """
    borders = [i for i, ln in enumerate(block) if _is_grid_border(ln)]
    if len(borders) < 2:
        return None
    plus = [i for i, ch in enumerate(block[borders[0]]) if ch == "+"]
    ncol = len(plus) - 1
    if ncol < 2:
        return None
    if any("![" in ln or LIST_BULLET_RE.search(ln) for ln in block):
        return None

    border_set = set(borders)
    content = [i for i in range(len(block)) if i not in border_set and block[i].strip()]
    # A regular grid has exactly ncol+1 pipes on every content line. A different
    # count means a spanning/merged cell (or a literal | ) - skip the table.
    if any(block[i].count("|") != ncol + 1 for i in content):
        return None

    header_sep = next((b for b in borders if "=" in block[b]), None)
    rows: list[list[int]] = []
    cur: list[int] = []
    for idx, ln in enumerate(block):
        if idx in border_set:
            if cur:
                rows.append(cur)
                cur = []
        else:
            cur.append(idx)
    if cur:
        rows.append(cur)

    def merge(idxs: list[int]) -> list[str]:
        acc = [""] * ncol
        gap = [False] * ncol  # blank line since last text -> paragraph break
        for li in idxs:
            line = block[li]
            for c in range(ncol):
                seg = line[plus[c] + 1 : plus[c + 1]].strip() if plus[c] + 1 <= len(line) else ""
                if seg:
                    acc[c] = seg if not acc[c] else acc[c] + ("<br><br>" if gap[c] else " ") + seg
                    gap[c] = False
                elif acc[c]:
                    gap[c] = True
        return acc

    parsed = [(merge(r), r[-1]) for r in rows]
    if not parsed:
        return None
    if header_sep is not None:
        header = next((cells for cells, last in parsed if last < header_sep), None)
        data = [cells for cells, last in parsed if last > header_sep]
    else:
        header, data = parsed[0][0], [c for c, _ in parsed[1:]]
    if not header:
        return None

    out = ["| " + " | ".join(_esc_pipe(h) for h in header) + " |"]
    out.append("|" + "|".join("---" for _ in range(ncol)) + "|")
    for row in data:
        row = (row + [""] * ncol)[:ncol]
        out.append("| " + " | ".join(_esc_pipe(c) for c in row) + " |")
    return out


COLRULE_RE = re.compile(r"^\s*-{2,}(\s+-{2,})+\s*$")  # >=2 dash runs = column rule
ALLDASH_RE = re.compile(r"^\s*-{3,}\s*$")             # single run = top/bottom rule


def _dash_run_spans(rule: str) -> list[tuple[int, int]]:
    return [(m.start(), m.end()) for m in re.finditer(r"-+", rule)]


def multiline_block_to_pipe(block: list[str]) -> list[str] | None:
    """Convert a multiline/simple-table block to pipe lines, or None if complex."""
    colrule = next((i for i, ln in enumerate(block) if COLRULE_RE.match(ln)), None)
    if colrule is None or colrule == 0:
        return None
    spans = _dash_run_spans(block[colrule])
    ncol = len(spans)
    if ncol < 2:
        return None
    if any("![" in ln for ln in block):
        return None

    def slice_cells(line: str) -> list[str]:
        return [line[a:b].strip() if a < len(line) else "" for a, b in spans]

    # Header: the non-blank lines between the top rule (or start) and the colrule.
    head_start = colrule - 1
    while head_start > 0 and not ALLDASH_RE.match(block[head_start - 1]) and block[head_start - 1].strip():
        head_start -= 1
    header = [""] * ncol
    for li in range(head_start, colrule):
        if block[li].strip():
            for c, cell in enumerate(slice_cells(block[li])):
                if cell:
                    header[c] = (header[c] + " " + cell).strip()
    if not any(header):
        return None

    # Data rows: below colrule until a bottom all-dash rule; blank line splits rows.
    data: list[list[str]] = []
    acc = [""] * ncol
    for li in range(colrule + 1, len(block)):
        line = block[li]
        if ALLDASH_RE.match(line):
            break
        if not line.strip():
            if any(acc):
                data.append(acc)
                acc = [""] * ncol
            continue
        for c, cell in enumerate(slice_cells(line)):
            if cell:
                acc[c] = (acc[c] + " " + cell).strip()
    if any(acc):
        data.append(acc)
    if not data:
        return None

    out = ["| " + " | ".join(_esc_pipe(h) for h in header) + " |"]
    out.append("|" + "|".join("---" for _ in range(ncol)) + "|")
    for row in data:
        out.append("| " + " | ".join(_esc_pipe(c) for c in row) + " |")
    return out


def convert_block_tables(lines: list[str]) -> tuple[list[str], int]:
    """Replace simple grid/multiline tables with pipe tables. Returns (lines, count).

    We collect (start, end, pipe_lines) for each convertible table, then splice
    them back from the bottom up so earlier indices stay valid.
    """
    ranges: list[tuple[int, int, list[str]]] = []

    # Grid tables: a run from one grid border to the last consecutive border.
    i = 0
    while i < len(lines):
        if _is_grid_border(lines[i]):
            j, last = i, i
            while j < len(lines) and (
                _is_grid_border(lines[j]) or lines[j].lstrip().startswith("|")
            ):
                if _is_grid_border(lines[j]):
                    last = j
                j += 1
            pipe = grid_block_to_pipe(lines[i : last + 1])
            if pipe is not None:
                ranges.append((i, last, pipe))
            i = last + 1
        else:
            i += 1

    taken = {n for s, e, _ in ranges for n in range(s, e + 1)}

    # Multiline tables: a column-rule line, with the top all-dash rule a line or
    # two above (the header sits between them), down to the bottom all-dash rule.
    i = 0
    while i < len(lines):
        if i not in taken and COLRULE_RE.match(lines[i]):
            top = next((b for b in range(i - 1, max(-1, i - 4), -1)
                        if ALLDASH_RE.match(lines[b])), None)
            if top is not None and top not in taken:
                j = i + 1
                while j < len(lines) and not ALLDASH_RE.match(lines[j]):
                    j += 1
                if j < len(lines):
                    pipe = multiline_block_to_pipe(lines[top : j + 1])
                    if pipe is not None:
                        ranges.append((top, j, pipe))
                        i = j + 1
                        continue
        i += 1

    for s, e, pipe in sorted(ranges, key=lambda r: r[0], reverse=True):
        lines[s : e + 1] = pipe
    return lines, len(ranges)


def process_file(qmd: Path, overwrite: bool) -> int:
    text = qmd.read_text(encoding="utf-8")
    lines = text.split("\n")
    lines, converted = convert_block_tables(lines)
    changes = converted
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
