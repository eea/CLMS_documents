"""Deterministic table rewrites the LLM output needs before Typst render.

All transforms are idempotent and HTML/llms.md-safe (raw-typst goes to Typst only).
"""

import re
from collections import Counter
from html.parser import HTMLParser

from ..resolve import build_tbl_caption

A3_FONT_PT = 8       # font size on A3-landscape tables
A3_XL_FONT_PT = 6    # very wide tables: A3-landscape + smaller font
A3_XXL_FONT_PT = 5   # extreme width: A3-landscape + smallest legible font (the floor)
_CELL_PAD_CHARS = 3  # per-column char allowance for cell inset (left+right padding)

_HTML_FENCE_RE = re.compile(r"```\{=html\}\n(?P<inner>.*?)\n```", re.DOTALL)


# ── 0. broken-table grid normalization ──────────────────────────────────────────
# When the convert LLM emits an HTML table whose header column count (with colspan)
# disagrees with its data-row count, the grid stretches to the wider one and data
# cells shift into the wrong columns (e.g. a "Plausibility" half rendering under the
# "Blind" header). Data is correct, only the column structure is broken: keep every
# data row verbatim and rebuild the header to the data width.

def _cell_text(cell_html: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", cell_html)).strip()


def _row_width(tr_content: str) -> int:
    """Sum of colspan across a row's <td>/<th> cells (no colspan = 1)."""
    total = 0
    for m in re.finditer(r"<t[dh]\b([^>]*)>", tr_content, re.IGNORECASE):
        cs = re.search(r'colspan\s*=\s*["\']?(\d+)', m.group(1), re.IGNORECASE)
        total += int(cs.group(1)) if cs else 1
    return total


def html_table_consistency(table_html: str) -> dict:
    """Check one HTML table for header/data column-count consistency.

    A table is broken when its data rows are uniform but the header (or colgroup)
    disagrees with that width by more than 1, either direction. The uniform-data guard
    leaves legitimate rowspan tables alone.
    """
    thead_m = re.search(r"<thead\b[^>]*>(.*?)</thead\s*>", table_html, re.DOTALL | re.IGNORECASE)
    tbody_m = re.search(r"<tbody\b[^>]*>(.*?)</tbody\s*>", table_html, re.DOTALL | re.IGNORECASE)
    all_rows = re.findall(r"<tr\b[^>]*>(.*?)</tr\s*>", table_html, re.DOTALL | re.IGNORECASE)
    if thead_m:
        header_rows = re.findall(r"<tr\b[^>]*>(.*?)</tr\s*>", thead_m.group(1), re.DOTALL | re.IGNORECASE)
        body_rows = re.findall(r"<tr\b[^>]*>(.*?)</tr\s*>",
                               tbody_m.group(1) if tbody_m else "", re.DOTALL | re.IGNORECASE)
    else:
        header_rows = all_rows[:1]
        body_rows = all_rows[1:]

    header_widths = [_row_width(r) for r in header_rows if r.strip()]
    data_widths = [_row_width(r) for r in body_rows if r.strip()]
    max_header_width = max(header_widths, default=0)
    data_width = Counter(data_widths).most_common(1)[0][0] if data_widths else 0
    ncols_colgroup = len(re.findall(r"<col\b", table_html, re.IGNORECASE))
    uniform_data = len(set(data_widths)) == 1 if data_widths else False
    broken = (
        uniform_data and max_header_width > 0
        and (abs(max_header_width - data_width) > 1
             or (ncols_colgroup > 0 and abs(ncols_colgroup - data_width) > 1))
    )
    return {"max_header_width": max_header_width, "data_width": data_width,
            "consistent": not broken, "ncols_colgroup": ncols_colgroup,
            "uniform_data": uniform_data}


def _leaf_header_cells(thead_html: str) -> list:
    """Non-blank cell texts of the deepest header row (the leaf labels)."""
    rows = re.findall(r"<tr\b[^>]*>(.*?)</tr\s*>", thead_html, re.DOTALL | re.IGNORECASE)
    if not rows:
        return []
    cells = re.findall(r"<t[dh]\b[^>]*>.*?</t[dh]\s*>", rows[-1], re.DOTALL | re.IGNORECASE)
    return [_cell_text(c) for c in cells if _cell_text(c)]


def _top_groups(thead_html: str) -> list:
    """(label, colspan) per non-blank first-header-row cell: the top-level comparison
    groups (e.g. Blind, Plausibility)."""
    rows = re.findall(r"<tr\b[^>]*>(.*?)</tr\s*>", thead_html, re.DOTALL | re.IGNORECASE)
    if not rows:
        return []
    groups = []
    for m in re.finditer(r"<t[dh]\b([^>]*)>(.*?)</t[dh]\s*>", rows[0], re.DOTALL | re.IGNORECASE):
        text = _cell_text(m.group(2))
        cs = re.search(r'colspan\s*=\s*["\']?(\d+)', m.group(1), re.IGNORECASE)
        if text:
            groups.append((text, int(cs.group(1)) if cs else 1))
    return groups


def _data_cell_texts(tr_html: str) -> list:
    return [_cell_text(c) for c in
            re.findall(r"<t[dh]\b[^>]*>.*?</t[dh]\s*>", tr_html, re.DOTALL | re.IGNORECASE)]


def _is_symmetric(data_rows: list, data_width: int, ngroups: int) -> bool:
    """True when the table is `ngroups` side-by-side mirror halves, detected by the
    first cell of each segment repeating across most rows (e.g. EEA39 | … | EEA39 | …)."""
    if ngroups < 2 or data_width % ngroups:
        return False
    seg = data_width // ngroups
    total = matches = 0
    for tr in data_rows:
        cells = _data_cell_texts(tr)
        if len(cells) != data_width:
            continue
        total += 1
        firsts = [cells[g * seg] for g in range(ngroups)]
        if firsts[0] and len(set(firsts)) == 1:
            matches += 1
    return total > 0 and matches / total > 0.6


def _rebuild_header(thead_html: str, data_rows: list, data_width: int) -> str:
    """Build a `<thead>` of `data_width` columns from the original header. Only the
    header is synthesised; data is untouched.

    Symmetric comparison tables (Blind | Plausibility) get a two-row header: group
    labels on top (each colspan = half) and leaf labels below, padded per half. Else a
    flat leaf-label header padded/truncated to data_width (labels best-effort)."""
    leaf = _leaf_header_cells(thead_html)
    groups = _top_groups(thead_html)
    ng = len(groups)
    if (ng >= 2 and data_width % ng == 0 and leaf and len(leaf) % ng == 0
            and _is_symmetric(data_rows, data_width, ng)):
        seg = data_width // ng
        per = len(leaf) // ng
        if per <= seg:
            row1 = "".join(f'<th colspan="{seg}" style="font-weight:bold">{g}</th>'
                           for g, _ in groups)
            row2 = ""
            for gi in range(ng):
                pad = seg - per
                row2 += "<th></th>" * pad
                row2 += "".join(f"<th>{lbl}</th>" for lbl in leaf[gi * per:(gi + 1) * per])
            return f"<thead><tr>{row1}</tr><tr>{row2}</tr></thead>"
    # fallback: flat header at data width
    labels = (leaf + [""] * data_width)[:data_width]
    return "<thead><tr>" + "".join(f"<th>{x}</th>" for x in labels) + "</tr></thead>"


def _normalize_one_table(table_html: str) -> tuple:
    """Rebuild one broken table's header to data-width, data verbatim. Returns
    (new_html, fixed). Untouched if consistent or not safely rebuildable."""
    if html_table_consistency(table_html)["consistent"]:
        return table_html, False
    thead_m = re.search(r"<thead\b[^>]*>(.*?)</thead\s*>", table_html, re.DOTALL | re.IGNORECASE)
    tbody_m = re.search(r"<tbody\b[^>]*>(.*?)</tbody\s*>", table_html, re.DOTALL | re.IGNORECASE)
    if not thead_m or not tbody_m:
        return table_html, False        # need a clear thead/tbody to rebuild safely
    data_rows = re.findall(r"<tr\b[^>]*>.*?</tr\s*>", tbody_m.group(1), re.DOTALL | re.IGNORECASE)
    if not data_rows:
        return table_html, False
    data_width = Counter(_row_width(re.search(r"<tr\b[^>]*>(.*?)</tr\s*>", r, re.DOTALL | re.IGNORECASE).group(1))
                         for r in data_rows).most_common(1)[0][0]
    new_thead = _rebuild_header(thead_m.group(1), data_rows, data_width)
    tattrs = (re.match(r"<table\b([^>]*)>", table_html, re.IGNORECASE) or [None, ""])[1]
    new = f"<table{tattrs}>{new_thead}<tbody>{''.join(data_rows)}</tbody></table>"
    return new, True


def normalize_table_grid(text: str) -> tuple:
    """Fix HTML tables whose header/data column counts disagree, data cells verbatim.
    Idempotent. Returns (text, n_fixed).

    Only single (non-nested) `{=html}` tables with a clear `<thead>`/`<tbody>` and
    uniform data rows are touched: the safely-rebuildable case."""
    lines = text.split("\n")
    out, i, n = [], 0, 0
    while i < len(lines):
        if lines[i].strip().startswith("```{=html}"):
            j = i + 1
            while j < len(lines) and lines[j].strip() != "```":
                j += 1
            block = "\n".join(lines[i + 1:j])
            # single, non-nested table only (count of <table opens == closes == 1)
            if (len(re.findall(r"<table\b", block, re.IGNORECASE)) == 1
                    and len(re.findall(r"</table\s*>", block, re.IGNORECASE)) == 1):
                m = re.search(r"<table\b.*?</table\s*>", block, re.DOTALL | re.IGNORECASE)
                new_tbl, fixed = _normalize_one_table(m.group(0))
                if fixed:
                    block = block[:m.start()] + new_tbl + block[m.end():]
                    n += 1
            out.append(lines[i])
            out.extend(block.split("\n"))
            out.append(lines[j] if j < len(lines) else "```")
            i = j + 1
        else:
            out.append(lines[i])
            i += 1
    return "\n".join(out), n


# ── 1. pipe-table caption relocation ────────────────────────────────────────────

_CAP_RE = re.compile(r"^:\s+\S")
_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
_DIV_RE = re.compile(r"^\s*\|[:\-\s|]*-[:\-\s|]*\|\s*$")
_TBL_NUM_RE = re.compile(r"^Table\s+\d+\s*[:.]")     # "Table 2: …" caption text
_OLD_TBL_DIV_RE = re.compile(r"^::: +\{#tbl-[^}]*\}\s*$")
_CAP_DIV_RE = re.compile(r"^::: +\{\.tbl-caption\}\s*$")
_DIV_OPEN_RE = re.compile(r"^:::+ +\S")     # an opening fenced div (has attrs after :::)
_DIV_CLOSE_RE = re.compile(r"^:::+\s*$")     # a bare closing :::


def _extract_outer_caption(body: list) -> tuple:
    """From the body of a `#tbl-` crossref div, pull out the trailing top-level prose
    paragraph (the table caption).

    Returns (caption, kept_lines). caption is None when the body holds no `{=html}`
    table fence (not a table-figure to migrate). A caption is only taken at depth 0,
    so a nested `.tbl-caption` (a previously-lifted second table) is preserved."""
    if not any(b.strip().startswith("```{=html}") for b in body):
        return None, body
    fence, depth, toplevel = False, 0, []     # toplevel: indices of depth-0 prose lines
    for idx, ln in enumerate(body):
        s = ln.strip()
        if s.startswith("```{="):
            fence = True
        elif s == "```" and fence:
            fence = False
        elif not fence:
            if _DIV_OPEN_RE.match(s):
                depth += 1
            elif _DIV_CLOSE_RE.match(s):
                depth = max(0, depth - 1)
            elif s and depth == 0:
                toplevel.append(idx)
    if not toplevel:
        return "", _strip_blank_edges(body)
    # the caption is the trailing contiguous run of top-level prose lines
    run = [toplevel[-1]]
    for k in range(len(toplevel) - 2, -1, -1):
        if toplevel[k] == run[0] - 1:
            run.insert(0, toplevel[k])
        else:
            break
    caption = " ".join(body[k].strip() for k in run).strip()
    kept = [ln for idx, ln in enumerate(body) if idx not in set(run)]
    return caption, _strip_blank_edges(kept)


def _strip_blank_edges(lines: list) -> list:
    a, b = 0, len(lines)
    while a < b and not lines[a].strip():
        a += 1
    while b > a and not lines[b - 1].strip():
        b -= 1
    return lines[a:b]


def _ncols(row: str) -> int:
    """Number of cells in a pipe-table row (`| a | b |` = 2, `| a |` = 1)."""
    return len(row.strip().strip("|").split("|"))


def unwrap_pseudo_header_tables(text: str) -> tuple:
    """Unwrap a real table the converter mistakenly nested under a 1-column "title"
    header, which makes Pandoc render only the first column.

    The converter sometimes emits:

        | Riparian Zones Delivery Units |          <- bogus 1-col header (a title)
        | :---------------------------- |          <- 1-col divider
        | **Table 2: …** |                          <- the caption, as a 1-col row
        | No. | DU ID | … | … |                     <- the real header (4 cols)
        | 1 | DU001A | … | … |                      <- data (4 cols)

    Pandoc keys column count off the 1-col header, so every data column past the first
    is lost. Rewrite to a `.tbl-caption` div (when a `Table N:` row is present) plus a
    proper pipe table: first multi-column row becomes the header, a matching divider is
    inserted, bogus 1-col title rows dropped.

    Fires only when the header and divider are both 1 column yet a later row is
    multi-column and every row from there on is too — so a real 1-column table or a
    normal multi-column table never matches. Idempotent. Returns (text, count)."""
    lines = text.split("\n")
    out, i, n = [], 0, 0
    while i < len(lines):
        if (_ROW_RE.match(lines[i]) and _ncols(lines[i]) == 1
                and i + 1 < len(lines) and _DIV_RE.match(lines[i + 1]) and _ncols(lines[i + 1]) == 1):
            j = i
            while j < len(lines) and _ROW_RE.match(lines[j]):
                j += 1
            block = lines[i:j]
            hdr = next((k for k in range(2, len(block)) if _ncols(block[k]) > 1), None)
            if hdr is not None and all(_ncols(r) > 1 for r in block[hdr:]):
                caption = None
                for k in range(hdr):                 # a `Table N:` 1-col row -> caption
                    cell = block[k].strip().strip("|").strip().strip("*").strip()
                    if _TBL_NUM_RE.match(cell):
                        caption = cell
                if caption:
                    out.extend(build_tbl_caption(caption).split("\n"))
                    out.append("")
                out.append(block[hdr])               # the real header
                out.append("| " + " | ".join(["---"] * _ncols(block[hdr])) + " |")
                out.extend(block[hdr + 1:])
                n += 1
                i = j
                continue
        out.append(lines[i])
        i += 1
    return "\n".join(out), n


def normalize_table_captions(text: str) -> tuple:
    """Migrate legacy crossref table-figure divs to plain `.tbl-caption` divs, and
    de-orphan pipe captions stranded after an orientation reset block. Lets an
    already-processed .qmd render with consistent, un-doubled captions without a
    re-convert. Idempotent. Returns (text, count).

    1. `::: {#tbl-x}` … html-fence … caption … `:::`  ->  `::: {.tbl-caption}` div +
       html fence. No crossref means no auto-numbering, hence no "Table N: Table N:"
       doubling; the source's own number is kept.
    2. a `{=typst}` page-reset block immediately followed by a `: caption` (the wrap
       left the caption outside it): swap so the caption sits with its table.
    """
    lines = text.split("\n")
    out, i, n = [], 0, 0

    # pass A: migrate #tbl- crossref divs to .tbl-caption + table content. Depth-aware:
    # the outer close is matched by balancing nested fenced divs, so a nested
    # `.tbl-caption` (a previously-lifted second table) is preserved, not truncated.
    while i < len(lines):
        if _OLD_TBL_DIV_RE.match(lines[i]):
            depth, j = 1, i + 1
            while j < len(lines) and depth > 0:
                s = lines[j].strip()
                if _DIV_OPEN_RE.match(s):
                    depth += 1
                elif _DIV_CLOSE_RE.match(s):
                    depth -= 1
                    if depth == 0:
                        break
                j += 1
            caption, kept = _extract_outer_caption(lines[i + 1:j])
            if caption is not None:               # body holds a table
                if caption:
                    out.extend(build_tbl_caption(caption).split("\n"))
                    out.append("")
                out.extend(kept)
                n += 1
                i = j + 1
                continue
        out.append(lines[i])
        i += 1

    # pass B: de-orphan. Move a `: caption` that follows a typst reset block to
    # before it, so it re-attaches to its table inside the orientation wrap.
    lines, out, i = out, [], 0
    while i < len(lines):
        if (lines[i].strip().startswith("```{=typst}")
                and any("#set page(flipped: false" in lines[i + k]
                        for k in range(1, 5) if i + k < len(lines))):
            close = i
            while close < len(lines) and lines[close].strip() != "```":
                close += 1
            t = close + 1
            while t < len(lines) and not lines[t].strip():
                t += 1
            if t < len(lines) and _CAP_RE.match(lines[t]):
                out.append(lines[t])            # caption first
                out.append("")
                out.extend(lines[i:close + 1])  # then the reset block
                n += 1
                i = t + 1
                continue
        out.append(lines[i])
        i += 1
    return "\n".join(out), n


def pipe_captions_to_divs(text: str) -> tuple:
    """Convert pipe-table ': Caption' lines into `.tbl-caption` divs above the table.

    Quarto's Typst writer silently drops a `: caption` pipe-table caption (renders only
    in HTML), so the same table ends up captioned on the website but not in the PDF. A
    `.tbl-caption` div (see `build_tbl_caption`) renders identically in HTML, PDF, and
    gfm, with the source's own "Table N:" number kept (no crossref, no auto-numbering).
    Idempotent: once a caption is a div there is no ': caption' line left.

    Handles a caption either after its table (Pandoc's canonical spot) or before it; a
    ': ' line not adjacent to a pipe table is left alone. Returns (text, count).
    """
    lines = text.split("\n")
    out, i, n = [], 0, 0
    while i < len(lines):
        line = lines[i]
        if _CAP_RE.match(line):
            cap = line.lstrip()[1:].strip()           # drop the leading ':'
            # caption after its table: last emitted non-blank line is a pipe row
            p = len(out) - 1
            while p >= 0 and not out[p].strip():
                p -= 1
            if p >= 0 and _ROW_RE.match(out[p]):
                start = p
                while start - 1 >= 0 and _ROW_RE.match(out[start - 1]):
                    start -= 1
                div = build_tbl_caption(cap)          # "" for an attribute-only caption
                if div:
                    out[start:start] = div.split("\n") + [""]
                n += 1
                i += 1
                while i < len(lines) and not lines[i].strip():
                    i += 1                            # swallow blanks after the caption
                continue
            # caption before its table: the next source block is a pipe table
            q = i + 1
            while q < len(lines) and not lines[q].strip():
                q += 1
            if q + 1 < len(lines) and _ROW_RE.match(lines[q]) and _DIV_RE.match(lines[q + 1]):
                div = build_tbl_caption(cap)          # "" for an attribute-only caption
                if div:
                    out.extend(div.split("\n"))
                    out.append("")
                n += 1
                i = q                                 # resume at the table itself
                continue
        out.append(line)
        i += 1
    return "\n".join(out), n


def _grab_table(lines: list, t: int) -> tuple:
    """A pipe table or `{=html}` fence starting at line `t`: (table_lines, end_index),
    or (None, t) if no table starts there."""
    if t >= len(lines):
        return None, t
    if _ROW_RE.match(lines[t]):                       # pipe table — contiguous rows
        k = t
        while k < len(lines) and _ROW_RE.match(lines[k]):
            k += 1
        return lines[t:k], k
    if lines[t].strip().startswith("```{=html}"):     # raw-html table fence
        k = t + 1
        while k < len(lines) and lines[k].strip() != "```":
            k += 1
        return lines[t:k + 1], k + 1
    return None, t


def redistribute_stacked_captions(text: str) -> tuple:
    """Spread a run of >=2 stacked `.tbl-caption` divs back across the tables that
    follow, one caption per table.

    The converter sometimes drops two `: Table N:` captions between two tables; the
    first table then takes both (pipe_captions_to_divs lifts each onto the nearest
    table above), leaving the second table un-captioned.

    Only fires when the count of immediately-following tables exactly equals the count
    of stacked captions (contiguous, blanks only). A genuinely missing table (2
    captions, 1 table) is left for the operator. Idempotent. Returns (text, n)."""
    lines = text.split("\n")
    out, i, n = [], 0, 0
    while i < len(lines):
        if _CAP_DIV_RE.match(lines[i]):
            divs, j = [], i
            while j < len(lines) and _CAP_DIV_RE.match(lines[j]):
                k = j
                while k < len(lines) and lines[k].strip() != ":::":
                    k += 1
                divs.append(lines[j:k + 1])
                j = k + 1
                while j < len(lines) and not lines[j].strip():
                    j += 1                            # skip blanks between stacked divs
            if len(divs) >= 2:
                tables, t = [], j
                while len(tables) < len(divs):
                    while t < len(lines) and not lines[t].strip():
                        t += 1
                    tbl, t2 = _grab_table(lines, t)
                    if tbl is None:
                        break
                    tables.append(tbl)
                    t = t2
                if len(tables) == len(divs):          # exact pairing
                    for d, tb in zip(divs, tables):
                        out.extend(d)
                        out.append("")
                        out.extend(tb)
                        out.append("")
                    n += len(divs) - 1
                    i = t
                    continue
        out.append(lines[i])
        i += 1
    return "\n".join(out), n


def _ensure_blank_after_captions(text: str) -> str:
    """Guarantee a blank line after every ': Caption'. A caption abutting the next
    block (especially a pipe-table header) makes Pandoc fail to parse it — needs a
    preceding blank line — so the table renders as literal `| … |` text. Idempotent."""
    lines = text.split("\n")
    out = []
    for i, line in enumerate(lines):
        out.append(line)
        if _CAP_RE.match(line):
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if nxt.strip():
                out.append("")
    return "\n".join(out)


# ── HTML table column analysis ──────────────────────────────────────────────────

class _TableAnalyzer(HTMLParser):
    """Walk one html table; report top-level column count + per-column text length.

    Only the outermost table is measured (nested tables flagged, not counted). colspan
    is honored for the column count; for width estimation colspan>1 cells are skipped
    (they'd smear across columns) and single-span text lengths accumulate per column.
    """

    def __init__(self):
        super().__init__()
        self.depth = 0
        self.has_nested = False
        self.in_cell = False
        self.cur_span = 1
        self.col_cursor = 0
        self.max_cols = 0
        self.row_span_sum = 0
        self.col_len = {}          # col index -> max single-span cell text length
        self.col_tok = {}          # col index -> longest unbreakable token (word) length
        self._buf = []

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            self.depth += 1
            if self.depth > 1:
                self.has_nested = True
            return
        if self.depth != 1:
            return
        if tag == "tr":
            self.row_span_sum = 0
            self.col_cursor = 0
        elif tag in ("td", "th"):
            d = dict(attrs)
            try:
                self.cur_span = max(1, int(d.get("colspan", "1")))
            except ValueError:
                self.cur_span = 1
            self.in_cell = True
            self._buf = []

    def handle_data(self, data):
        if self.in_cell and self.depth == 1:
            self._buf.append(data)

    def handle_endtag(self, tag):
        if tag == "table":
            self.depth -= 1
            return
        if self.depth != 1:
            return
        if tag in ("td", "th") and self.in_cell:
            text = " ".join("".join(self._buf).split())
            if self.cur_span == 1:
                c = self.col_cursor
                self.col_len[c] = max(self.col_len.get(c, 0), len(text))
                longest = max((len(w) for w in text.split()), default=0)
                self.col_tok[c] = max(self.col_tok.get(c, 0), longest)
            self.col_cursor += self.cur_span
            self.row_span_sum += self.cur_span
            self.in_cell = False
        elif tag == "tr":
            self.max_cols = max(self.max_cols, self.row_span_sum)


def _analyze_html_table(inner: str):
    a = _TableAnalyzer()
    try:
        a.feed(inner)
    except Exception:
        return None
    if a.max_cols <= 0:
        return None
    return {"ncols": a.max_cols, "has_nested": a.has_nested,
            "col_len": a.col_len, "col_tok": a.col_tok}


def _colgroup_for(ncols: int, col_len: dict, col_tok: dict) -> str:
    """Build a <colgroup> with width:N% per column.

    weight = longest token + cell-inset allowance + a capped content bonus, clamped to
    3% min and renormalized to 100%. The inset allowance is a hard floor: a column must
    fit its widest word plus left/right padding, else with hyphenation off the word
    fills into the inset and visually crosses the cell border. The bonus cap (<=3x the
    token) stops a long-text column (e.g. a 200-char "Catchment Name") from hogging
    width and starving short columns like "DU ID"/"SC01-02"."""
    weights = []
    for c in range(ncols):
        tok = max(1, col_tok.get(c, 0))
        ln = max(1, col_len.get(c, 0))
        weights.append((tok + _CELL_PAD_CHARS) + 0.3 * min(ln, 3 * tok))
    s = sum(weights) or 1.0
    pct = [max(3.0, w * 100.0 / s) for w in weights]
    s = sum(pct)
    pct = [p * 100.0 / s for p in pct]
    cols = "".join(f'<col style="width: {p:.1f}%">\n' for p in pct)
    return f"<colgroup>\n{cols}</colgroup>"


# ── 2. stamp <colgroup> on raw-HTML tables ──────────────────────────────────────

def stamp_html_colgroups(text: str) -> tuple:
    """Inject a computed <colgroup> into each raw-HTML table that lacks one.

    Skips nested-table cases (column model too ambiguous to size safely); those still
    get orientation help. Idempotent."""
    stamped = 0

    def _fence(m):
        nonlocal stamped
        inner = m.group("inner")
        if "<table" not in inner or "<colgroup" in inner:
            return m.group(0)
        info = _analyze_html_table(inner)
        if not info or info["has_nested"] or info["ncols"] < 2:
            return m.group(0)
        colgroup = _colgroup_for(info["ncols"], info["col_len"], info["col_tok"])
        # insert right after the first opening <table ...> tag
        new_inner, n = re.subn(r"(<table[^>]*>)", r"\1\n" + colgroup, inner, count=1)
        if not n:
            return m.group(0)
        stamped += 1
        return "```{=html}\n" + new_inner + "\n```"

    return _HTML_FENCE_RE.sub(_fence, text), stamped


# ── 3. orient wide tables (landscape / A3) ───────────────────────────────────────

def _pipe_table_ncols(lines, idx):
    """If a pipe table starts at/just after idx, return its column count, else 0."""
    if (idx + 1 < len(lines) and _ROW_RE.match(lines[idx])
            and _DIV_RE.match(lines[idx + 1])):
        return lines[idx].strip().strip("|").count("|") + 1
    return 0


# Orientation uses raw `{=typst}` page-set rules (dropped from HTML/llms.md). A
# `.landscape` div only flips when standalone — added to a `::: {#tbl}` crossref div
# it's a no-op (verified), so bracket the whole region with set rules instead, which
# does flip/resize a crossref table. Reset restores A4 portrait. Treatment chosen by
# estimated content width (see `_decide`).
_PAGE_RULES = {
    # A4-landscape tables are still column-dense, hence a modest font shrink; A3-land
    # (the widest matrices) needs the most.
    "A4-land": '#set page(flipped: true)\n#set text(size: 9pt)',
    "A3-port": '#set page(paper: "a3")',           # retained; not currently selected
    "A3-land": f'#set page(flipped: true, paper: "a3")\n#set text(size: {A3_FONT_PT}pt)',
    # Wider tables (e.g. a 25-col confusion matrix) overflow A3-land at 8pt; step the
    # font down so all columns fit rather than break.
    "A3-xl": f'#set page(flipped: true, paper: "a3")\n#set text(size: {A3_XL_FONT_PT}pt)',
    "A3-xxl": f'#set page(flipped: true, paper: "a3")\n#set text(size: {A3_XXL_FONT_PT}pt)',
}
_RESET = ('```{=typst}\n#set page(flipped: false, paper: "a4")\n'
          '#set text(size: 11pt)\n```')


def _wrap(block: list, treat: str) -> list:
    """Bracket a table block with the page-set rules for its treatment."""
    return ["```{=typst}\n" + _PAGE_RULES[treat] + "\n```", ""] + block + ["", _RESET]


# Page chosen by estimated min width (Σ per-column longest unbreakable token, chars) —
# the narrowest the table renders with headers/cells wrapping — picking the smallest
# page that fits. Beats replicating source geometry, which over-escalated: the author
# used A3 for tables wide only because headers sat on one line; wrapped, they fit A4.
# Calibrated on the reference doc (A4-portrait usable ~90 char at 10pt, A4-land ~698pt,
# A3-land ~1047pt), with margin.
_A4_PORTRAIT_MAX_CHARS = 75
_A4_LANDSCAPE_MAX_CHARS = 110
# A3-land at 8pt holds ~125 char-widths (measured: 116 fits, 137 overflows). Wider
# tables step the font down; capacity scales ~inversely with font size (125 × 8/6 ≈
# 165 at 6pt). Beyond that, 5pt floor.
_A3_LANDSCAPE_MAX_CHARS = 125
_A3_XL_MAX_CHARS = 165


def _table_min_width(info, block, ncols):
    """Σ per-column longest unbreakable token (+ separators) for an HTML (info) or
    pipe (block) table: the narrowest width the table needs to avoid word-breaks."""
    if info:
        toks = [info["col_tok"].get(c, 1) for c in range(ncols)]
    else:
        toks = _pipe_col_tokens(block, ncols)
    return sum(toks) + ncols


def _decide(width_chars: int):
    """Smallest page treatment that fits the estimated width (None = A4-portrait)."""
    if width_chars <= _A4_PORTRAIT_MAX_CHARS:
        return None
    if width_chars <= _A4_LANDSCAPE_MAX_CHARS:
        return "A4-land"
    if width_chars <= _A3_LANDSCAPE_MAX_CHARS:
        return "A3-land"
    if width_chars <= _A3_XL_MAX_CHARS:
        return "A3-xl"
    return "A3-xxl"


_TBL_DIV_RE = re.compile(r"^(::: +\{)(#tbl-[^}]*)\}\s*$")


def _scan_div_block(lines, start):
    """From a '::: {#tbl-…}' opening at `start`, find the matching ':::' close.
    Returns (end_idx, table_info|None), where info has ncols/col_len/col_tok."""
    inner_html, j, in_fence, end = [], start + 1, False, start
    while j < len(lines):
        s = lines[j].strip()
        if s.startswith("```{=html}"):
            in_fence = True
        elif s == "```" and in_fence:
            in_fence = False
        elif in_fence:
            inner_html.append(lines[j])
        elif s == ":::":
            end = j
            break
        j += 1
    return end, (_analyze_html_table("\n".join(inner_html)) if inner_html else None)


def _scan_bare_fence(lines, start):
    """From a '```{=html}' opening at `start`, return (end_idx, table_info|None)."""
    inner, j = [], start + 1
    while j < len(lines) and lines[j].strip() != "```":
        inner.append(lines[j])
        j += 1
    joined = "\n".join(inner)
    info = _analyze_html_table(joined) if "<table" in joined else None
    return j, info


def _pipe_col_tokens(block, ncols):
    """Per-column longest unbreakable token across a pipe table's rows."""
    tok = [0] * ncols
    for r in block:
        s = r.strip()
        if not s.startswith("|") or set(s) <= set("|-: "):
            continue
        cells = [c.strip().strip("*") for c in s.strip("|").split("|")]
        for i, c in enumerate(cells[:ncols]):
            tok[i] = max(tok[i], max((len(w) for w in c.split()), default=0))
    return tok


def orient_wide_tables(text: str, src_index: list = None) -> tuple:
    """Give each table the smallest page that fits its estimated content width,
    bracketing the table region with raw-typst page-set rules so the caption travels
    with the table. Narrow tables stay A4-portrait. Idempotent.

    `src_index` is accepted for backward compatibility but unused (decision is now
    content-width-driven, see `_decide`).
    """
    lines = text.split("\n")
    out, i, oriented, in_special = [], 0, 0, False
    while i < len(lines):
        line = lines[i]

        # idempotency: skip tables already inside a page-set region; the reset line
        # turns it back off.
        if "#set page(flipped: false" in line:
            in_special = False
            out.append(line)
            i += 1
            continue
        if "#set page(" in line:
            in_special = True
        if in_special:
            out.append(line)
            i += 1
            continue

        # region kind 0: `.tbl-caption` div immediately followed by an HTML table.
        # Wrap caption + table so the caption travels with its table.
        if _CAP_DIV_RE.match(line):
            cend = i + 1
            while cend < len(lines) and lines[cend].strip() != ":::":
                cend += 1
            t = cend + 1
            while t < len(lines) and not lines[t].strip():
                t += 1
            if t < len(lines) and lines[t].strip().startswith("```{=html}"):
                tend, info = _scan_bare_fence(lines, t)
                if info and info["ncols"] >= 2:
                    block = lines[i:tend + 1]
                    treat = _decide(_table_min_width(info, lines[t:tend + 1], info["ncols"]))
                    out.extend(_wrap(block, treat) if treat else block)
                    oriented += 1 if treat else 0
                    i = tend + 1
                    continue
            # …or a pipe table: wrap caption + table so the caption flips with it.
            pcols = _pipe_table_ncols(lines, t) if t < len(lines) else 0
            if pcols >= 2:
                k = t + 1
                while k + 1 < len(lines) and _ROW_RE.match(lines[k + 1]):
                    k += 1
                block = lines[i:k + 1]
                treat = _decide(_table_min_width(None, lines[t:k + 1], pcols))
                out.extend(_wrap(block, treat) if treat else block)
                oriented += 1 if treat else 0
                i = k + 1
                continue

        # region kind 1: captioned table div, treat the whole div
        if _TBL_DIV_RE.match(line):
            end, info = _scan_div_block(lines, i)
            block = lines[i:end + 1]
            ncols = info["ncols"] if info else 0
            treat = _decide(_table_min_width(info, block, ncols)) if ncols >= 2 else None
            out.extend(_wrap(block, treat) if treat else block)
            oriented += 1 if treat else 0
            i = end + 1
            continue

        # region kind 2: bare HTML fenced table (not inside a tbl div)
        if line.strip().startswith("```{=html}"):
            end, info = _scan_bare_fence(lines, i)
            if info and info["ncols"] >= 2:
                block = lines[i:end + 1]
                treat = _decide(_table_min_width(info, block, info["ncols"]))
                out.extend(_wrap(block, treat) if treat else block)
                oriented += 1 if treat else 0
                i = end + 1
                continue

        # region kind 3: pipe table
        ncols = _pipe_table_ncols(lines, i)
        if ncols >= 2:
            k = i + 1
            while k + 1 < len(lines) and _ROW_RE.match(lines[k + 1]):
                k += 1
            treat = _decide(_table_min_width(None, lines[i:k + 1], ncols))
            # pull a trailing ': caption' inside the wrap, else the reset block
            # separates it from its table and it renders as a literal ": Table N" line.
            end = k
            t = k + 1
            while t < len(lines) and not lines[t].strip():
                t += 1
            if t < len(lines) and _CAP_RE.match(lines[t]):
                end = t
            block = lines[i:end + 1]
            out.extend(_wrap(block, treat) if treat else block)
            oriented += 1 if treat else 0
            i = end + 1
            continue

        out.append(line)
        i += 1
    return "\n".join(out), oriented
