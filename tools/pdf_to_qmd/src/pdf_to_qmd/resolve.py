"""Pass-2 post-processing on the converter's raw .qmd output.

Deterministic, local cleanup: resolve FIG_n tokens to real image paths, normalize
frontmatter to satisfy validate_qmd_files.py, and a handful of HTML-table fixes
for the HTML→Typst path.
"""

import logging
import re
from pathlib import Path

log = logging.getLogger(__name__)

# body figure: ![caption](FIG_3)
_FIG_IMG_RE = re.compile(r"!\[([^\]]*)\]\(\s*(FIG_(\d+))\s*\)")
# figure inside a raw-HTML table cell: <img src="FIG_3" …>
_FIG_HTML_RE = re.compile(r'(<img\b[^>]*\bsrc\s*=\s*["\'])\s*(FIG_(\d+))\s*(["\'])', re.IGNORECASE)


def _rel(file_name: str, qmd_path: Path, media_dirname: str) -> str:
    """Relative (Unix-style) path from the .qmd to a media file."""
    return f"{media_dirname}/{file_name}"


def resolve_fig_tokens(body: str, figures: list, qmd_path: Path, media_dirname: str) -> tuple:
    """Replace FIG_n image tokens with real media paths.

    figures is the detections.json "figures" list (dicts with fig_id + file).
    Returns (resolved_body, report); report keys: resolved (swapped to a real
    image), hallucinated (FIG_n with no matching crop), unreferenced (detected
    but never cited).
    """
    by_id = {f["fig_id"]: f for f in figures if f.get("fig_id")}
    resolved, hallucinated, referenced = [], [], set()

    def _sub(m):
        caption, token, _num = m.group(1), m.group(2), m.group(3)
        referenced.add(token)
        fig = by_id.get(token)
        if fig and fig.get("file"):
            resolved.append(token)
            rel = _rel(fig["file"], qmd_path, media_dirname)
            return f"![{caption}]({rel})"
        # referenced but no matching detection; leave a render-safe marker
        hallucinated.append(token)
        marker = f"figure not found: {caption}" if caption else f"figure not found ({token})"
        log.warning("Converter referenced %s with no matching detection; marker inserted", token)
        return f"*⚠ {marker}*"

    def _sub_html(m):
        prefix, token, _num, suffix = m.group(1), m.group(2), m.group(3), m.group(4)
        referenced.add(token)
        fig = by_id.get(token)
        if fig and fig.get("file"):
            resolved.append(token)
            return f"{prefix}{_rel(fig['file'], qmd_path, media_dirname)}{suffix}"
        hallucinated.append(token)
        log.warning("Converter referenced %s (in HTML) with no matching detection", token)
        return f'{prefix}{token}-NOT-FOUND{suffix}'

    new_body = _FIG_IMG_RE.sub(_sub, body)
    new_body = _FIG_HTML_RE.sub(_sub_html, new_body)

    # bare FIG_n still unresolved (odd spacing or unexpected form)
    leftover = re.findall(r"(?:\(\s*FIG_\d+\s*\)|src=[\"']\s*FIG_\d+)", new_body)
    if leftover:
        log.warning("Leftover FIG_ tokens after resolution: %s", leftover)

    unreferenced = [fid for fid in by_id if fid not in referenced]
    if unreferenced:
        log.warning(
            "%d detected figure(s) were NOT referenced by the converter: %s",
            len(unreferenced), unreferenced,
        )
        # Record in an HTML comment: visible in the .qmd source but never rendered
        # (Pandoc drops HTML comments). An unreferenced detection is often a false
        # positive (e.g. a cropped formula fragment); the verify report flags real misses.
        notes = ["<!-- figures detected in Phase 1 but not placed by the converter",
                 "     (review and place manually if any is a real figure):"]
        for fid in unreferenced:
            f = by_id[fid]
            rel = _rel(f["file"], qmd_path, media_dirname)
            cap = f.get("caption") or "(no caption)"
            notes.append(f"       {fid}: {cap} -> {rel}")
        notes.append("-->")
        new_body = new_body.rstrip() + "\n\n" + "\n".join(notes) + "\n"

    report = {
        "resolved": resolved,
        "hallucinated": hallucinated,
        "unreferenced": unreferenced,
    }
    log.info(
        "Figure tokens: %d resolved, %d unknown, %d unreferenced",
        len(resolved), len(hallucinated), len(unreferenced),
    )
    return new_body, report


# Zero/none border declaration in the forms the model emits, dropped from inline
# style="…". Quarto/Typst treats `border:0` inconsistently (thick black stroke,
# or "invalid border shorthand 0" warning + ignore). A borderless table is the
# ABSENCE of a border (Typst template defaults nested tables to stroke:none).
_STYLE_ATTR_RE = re.compile(r'style\s*=\s*(?P<q>["\'])(?P<body>.*?)(?P=q)', re.IGNORECASE | re.DOTALL)
_ZERO_BORDER_DECL_RE = re.compile(
    r"""
    \s*                                   # leading space
    border(?:-(?:top|right|bottom|left))? # border or border-<side>
    (?:-width)?                           # optional -width
    \s*:\s*                               # colon
    (?:                                   # a zero/none value:
        0(?:px|pt|em|rem|%)?              #   0, 0px, 0pt, …
      | none                              #   none
    )
    \s*;?                                 # optional trailing semicolon
    """,
    re.IGNORECASE | re.VERBOSE,
)


def sanitize_zero_borders(qmd_text: str) -> tuple:
    """Strip zero/`none` border declarations from inline HTML `style` attributes.

    The model emits `style="…; border:0"` on nested layout tables despite the
    prompt, and `border:0` is not a reliable "no border" in HTML→Typst. Removing
    it lets the table fall through to the template's `stroke: none` default.
    Idempotent. Returns (clean_text, count).
    """
    removed = 0

    def _clean_style(m):
        nonlocal removed
        quote, body = m.group("q"), m.group("body")
        new_body, n = _ZERO_BORDER_DECL_RE.subn("", body)
        removed += n
        new_body = re.sub(r"\s*;\s*;", ";", new_body)          # collapse double ;
        new_body = new_body.strip().strip(";").strip()
        if not new_body:
            return ""                                          # drop empty style=""
        return f"style={quote}{new_body}{quote}"

    out = _STYLE_ATTR_RE.sub(_clean_style, qmd_text)
    return out, removed


_CENTER_DECL_RE = re.compile(r"\s*text-align\s*:\s*center\s*;?", re.IGNORECASE)
_FIRST_TR_RE = re.compile(r"<tr\b.*?</tr\s*>", re.IGNORECASE | re.DOTALL)


def _top_level_table_spans(text: str) -> list:
    """(start, end) of each top-level <table>…</table>, depth-aware so a nested
    layout sub-table isn't treated as a separate table."""
    spans, depth, start = [], 0, None
    for m in re.finditer(r"<table\b|</table\s*>", text, re.IGNORECASE):
        if m.group().lower().startswith("<table"):
            if depth == 0:
                start = m.start()
            depth += 1
        else:
            depth = max(0, depth - 1)
            if depth == 0 and start is not None:
                spans.append((start, m.end()))
                start = None
    return spans


def neutralize_header_center(qmd_text: str) -> tuple:
    """Drop `text-align:center` from the first row of each top-level table.

    A centered first row (the model's header band, usually a colspan cell)
    makes pandoc push that center onto the whole HTML→Typst column-align tuple,
    centering EVERY body cell. The template already centers the header row
    (`show table.cell.where(y: 0): set align(center)`), so dropping the inline
    center lets Quarto emit `align: (auto, …)` — body cells fall back to left,
    header still centers. Nested layout tables untouched. Idempotent.
    Returns (clean_text, count).
    """
    removed = 0
    # Rewrite right-to-left so earlier spans' offsets stay valid as we mutate.
    out = qmd_text
    for start, end in reversed(_top_level_table_spans(qmd_text)):
        seg = out[start:end]
        tr = _FIRST_TR_RE.search(seg)            # first row only
        if not tr:
            continue
        new_tr, n = _CENTER_DECL_RE.subn("", tr.group(0))
        if not n:
            continue
        # tidy any style="" / "; ;" / leading-";" left behind
        new_tr = re.sub(r"\s*;\s*;", ";", new_tr)
        new_tr = re.sub(r'style\s*=\s*(["\'])\s*;?\s*\1', "", new_tr)
        removed += n
        out = out[:start] + seg[:tr.start()] + new_tr + seg[tr.end():] + out[end:]
    return out, removed


_HTML_BLOCK_RE = re.compile(r"```\{=html\}\n(?P<inner>.*?)\n```", re.DOTALL)
_CAPTION_EL_RE = re.compile(r"[ \t]*<caption\b[^>]*>(?P<text>.*?)</caption>\s*", re.DOTALL | re.IGNORECASE)

# Caption blue, matching the template's figure.caption show rule
# (`caption-blue = rgb("#3E6893")`). Hardcoded, not the template variable, so a
# bare `quarto render doc.qmd` without the _meta theme still compiles.
_TBL_CAPTION_FILL = '#3E6893'


def build_tbl_caption(caption_text: str) -> str:
    """Build a `.tbl-caption` div for `caption_text` (already whitespace-collapsed).

    Raw-HTML tables can't use Quarto's pipe `: caption` (doesn't attach to
    `{=html}` blocks) or `#tbl-` crossref (auto-numbering doubles the source's
    manual "Table N:"). This plain div renders the caption verbatim in HTML, PDF
    (raw-typst `#set text` scoped to the block), and gfm (raw-typst dropped,
    plain text remains). No `#tbl-` id, so the source's own number stays.
    """
    return (
        "::: {.tbl-caption}\n"
        "```{=typst}\n"
        f'#set text(size: 9pt, fill: rgb("{_TBL_CAPTION_FILL}"))\n'
        "```\n"
        f"{caption_text}\n"
        ":::"
    )


def lift_html_table_captions(qmd_text: str) -> tuple:
    """Lift an HTML `<caption>` out of each raw-HTML table into a `.tbl-caption` div.

    The converter keeps the caption inside the `<table>`, but Quarto's HTML→Typst
    writer silently discards `<caption>`. Move it to a `.tbl-caption` div above
    the table (see `build_tbl_caption`). Idempotent.

    When the converter packs MULTIPLE captioned tables into one `{=html}` fence,
    the fence is split into one per table so every caption sits with its own table
    — otherwise the Typst writer renders only the first and drops the rest. Nested
    tables fall back to stacking every caption at the top rather than risk an
    unsafe split. Returns (text, count).
    """
    lifted = 0

    def _lift_one(seg):
        """(div, seg_without_caption) for the FIRST <caption> in `seg`; else (None, seg)."""
        cap = _CAPTION_EL_RE.search(seg)
        if not cap:
            return None, seg
        text = re.sub(r"\s+", " ", cap.group("text")).strip()
        if not text:
            return None, seg
        return build_tbl_caption(text), _CAPTION_EL_RE.sub("", seg, count=1)

    def _fence(body):
        return "```{=html}\n" + body.strip("\n") + "\n```"

    def _repl(m):
        nonlocal lifted
        inner = m.group("inner")
        n_caps = len(_CAPTION_EL_RE.findall(inner))
        if n_caps == 0:
            return m.group(0)
        if n_caps == 1:
            div, new_inner = _lift_one(inner)
            if div is None:
                return m.group(0)
            lifted += 1
            return f"{div}\n\n{_fence(new_inner)}"
        # multiple captioned tables: split into one fence per table when flat
        # (each </table>-delimited segment holds a single table)
        segs = [s for s in re.split(r"(?<=</table>)", inner) if s.strip()]
        if all(s.count("<table") <= 1 for s in segs):
            out = []
            for s in segs:
                div, body = _lift_one(s)
                if div is not None:
                    lifted += 1
                    out.append(f"{div}\n\n{_fence(body)}")
                else:
                    out.append(_fence(body))
            return "\n\n".join(out)
        # nested/ambiguous: stack every caption at the top, keep one fence, so
        # none is dropped when clean pairing isn't possible
        divs, new_inner = [], inner
        for _ in range(n_caps):
            d, new_inner = _lift_one(new_inner)
            if d is None:
                break
            divs.append(d)
            lifted += 1
        return "\n\n".join(divs) + f"\n\n{_fence(new_inner)}"

    return _HTML_BLOCK_RE.sub(_repl, qmd_text), lifted


# A <tr> with no <td> (whitespace/comments only). The converter emits these to
# "account for" rows covered by a rowspan, but Pandoc turns a cell-less row into
# bare commas in the Typst table (`,\n,\n,`) — a hard compile error. The row is
# redundant (earlier rowspans already fill those positions), so drop it. Pattern
# is precise so a row with a nested <table>/<td> never matches.
_EMPTY_TR_RE = re.compile(
    r"[ \t]*<tr\b[^>]*>\s*(?:<!--.*?-->\s*)*</tr\s*>\s*\n?",
    re.DOTALL | re.IGNORECASE,
)


def drop_empty_table_rows(qmd_text: str) -> tuple:
    """Remove cell-less ``<tr>`` rows (whitespace/comments only) from HTML tables.

    Returns (clean_text, count). Idempotent.
    """
    out, n = _EMPTY_TR_RE.subn("", qmd_text)
    return out, n


# Invalid HTML entities LLMs invent, mapped to the Unicode glyph (renders in both
# the HTML and Typst writers). E.g. `&sqrt;` doesn't exist (valid is &radic;), so
# a transcribed formula would render the literal text "&sqrt;". Extend as needed.
_INVALID_ENTITIES = {
    "&sqrt;": "√",       # U+221A SQUARE ROOT (valid entity is &radic;)
}


def fix_invalid_entities(qmd_text: str) -> tuple:
    """Replace known-invalid HTML entities with their Unicode equivalent so
    formulas render in HTML and Typst. Idempotent. Returns (text, count)."""
    total = 0
    for bad, good in _INVALID_ENTITIES.items():
        c = qmd_text.count(bad)
        if c:
            qmd_text = qmd_text.replace(bad, good)
            total += c
    return qmd_text, total


# empty-alt image: `![](path)` (optional trailing `{attrs}`). The converter emits
# this and drops the caption on the next line as plain prose.
_EMPTY_ALT_IMG_RE = re.compile(r"^!\[\]\((?P<path>[^)]+)\)(?P<attr>\{[^}]*\})?\s*$")
# caption line: "Figure 12: …" or "Fig. 3. …"
_FIG_CAPTION_RE = re.compile(r"^(?:Figure|Fig\.?)\s+\d+\s*[:.]\s*\S")


def fold_figure_captions(qmd_text: str) -> tuple:
    """Fold a `Figure N: …` caption left on the line after an empty-alt image back
    into the image's alt text, so Quarto renders it as a figure caption.

        ![](img.png)
        Figure 2: Level of reporting

    →   ![Figure 2: Level of reporting](img.png)

    Fires only on an empty alt directly followed by a caption-pattern line, so it
    never swallows ordinary prose. Idempotent. Returns (text, count)."""
    lines = qmd_text.split("\n")
    out, i, n = [], 0, 0
    while i < len(lines):
        m = _EMPTY_ALT_IMG_RE.match(lines[i])
        if m and i + 1 < len(lines) and _FIG_CAPTION_RE.match(lines[i + 1].strip()):
            cap = lines[i + 1].strip().replace("[", r"\[").replace("]", r"\]")
            out.append(f"![{cap}]({m.group('path')}){m.group('attr') or ''}")
            n += 1
            i += 2
            continue
        out.append(lines[i])
        i += 1
    return "\n".join(out), n


def _coerce_date(val: str) -> str:
    """Coerce a date to YYYY-MM-DD (the PR gate's required format).

    A full YYYY-MM-DD passes through; a year-only ("2011") or year-month value is
    padded with "-01"; anything unparseable is returned unchanged (operator fixes).
    """
    val = (val or "").strip().strip('"').strip("'")
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", val):
        return val
    m = re.search(r"(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?", val)
    if m:
        return f"{m.group(1)}-{m.group(2) or '01'}-{m.group(3) or '01'}"
    return val


def normalize_frontmatter(
    qmd_text: str, category: str = "uncategorized", date: str = None,
    cover_fields: dict = None,
) -> str:
    """Ensure the .qmd frontmatter carries the fields the PR gate requires.

    Always forces `category` (taxonomy label the model must not guess). Injects
    `date` if the model omitted one (validate_qmd_files.py requires it); a
    model-supplied date is kept. Prepends a minimal block if there's no frontmatter.

    `cover_fields` (title/subtitle/date/version from cover extraction) wins over
    the converter's guesses where non-empty — the cover extraction read the actual
    cover page. Empty cover values fall back to the converter's value.
    """
    fm_re = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)
    m = fm_re.match(qmd_text.lstrip())
    cat_line = f"category: {category}"

    def _set_or_add(fm: str, key: str, value: str) -> str:
        """Force `key: "value"` in the frontmatter block."""
        if not value:
            return fm
        quoted = f'"{value}"'
        pat = re.compile(r"^\s*" + re.escape(key) + r"\s*:.*$", re.MULTILINE)
        if pat.search(fm):
            return pat.sub(f"{key}: {quoted}", fm, count=1)
        return fm.rstrip() + f"\n{key}: {quoted}"

    def _inject(fm: str) -> str:
        # category always forced (controlled vocabulary)
        if re.search(r"^\s*category\s*:", fm, re.MULTILINE):
            fm = re.sub(r"^\s*category\s*:.*$", cat_line, fm, count=1, flags=re.MULTILINE)
        else:
            fm = fm.rstrip() + "\n" + cat_line
        # cover fields override the converter's guesses where non-empty
        if cover_fields:
            for key in ("title", "subtitle", "version"):
                val = cover_fields.get(key, "")
                if val:
                    fm = _set_or_add(fm, key, val)
        # date precedence: model-supplied > cover's > `date` fallback (today's,
        # which the operator should correct). date is required, so always set one.
        if not re.search(r"^\s*date\s*:", fm, re.MULTILINE):
            cover_date = cover_fields.get("date", "") if cover_fields else ""
            chosen = cover_date or (date or "")
            if chosen:
                fm = fm.rstrip() + f'\ndate: "{chosen}"'
                if not cover_date and chosen == date:
                    log.warning("No date on cover or in converter output — defaulting to %s "
                                "(operator should correct)", date)
        # coerce whatever date is present to YYYY-MM-DD (the PR gate requires it)
        dm = re.search(r"^\s*date\s*:\s*(.+)$", fm, re.MULTILINE)
        if dm:
            coerced = _coerce_date(dm.group(1))
            if coerced != dm.group(1).strip().strip('"'):
                log.info("Coerced date %r → %r", dm.group(1).strip(), coerced)
            fm = re.sub(r"^\s*date\s*:.*$", f'date: "{coerced}"', fm,
                        count=1, flags=re.MULTILINE)
        # subtitle is required by the PR gate; emit an empty one when none supplied
        if not re.search(r"^\s*subtitle\s*:", fm, re.MULTILINE):
            fm = fm.rstrip() + '\nsubtitle: ""'
        return fm

    if not m:
        log.warning("Converter output had no YAML frontmatter — prepending a minimal block")
        fields = [cat_line]
        cover_date = cover_fields.get("date", "") if cover_fields else ""
        chosen_date = cover_date or (date or "")
        if chosen_date:
            fields.append(f'date: "{_coerce_date(chosen_date)}"')
        if cover_fields:
            for key in ("title", "version"):
                if cover_fields.get(key):
                    fields.append(f'{key}: "{cover_fields[key]}"')
        # subtitle required by the PR gate — emit it even when empty
        fields.append(f'subtitle: "{(cover_fields or {}).get("subtitle", "")}"')
        return f"---\n{chr(10).join(fields)}\n---\n\n{qmd_text.lstrip()}"

    body_start = qmd_text.lstrip()[m.end():]
    return f"---\n{_inject(m.group(1))}\n---\n" + body_start


def strip_wrapping_fence(qmd_text: str) -> str:
    """Remove an outer ``` fence the model sometimes wraps the whole document in.

    Line-based (not a whole-text regex) to tolerate ```qmd / ```yaml openers and
    code fences inside the body: drop a leading fence line and, if present, the
    matching trailing bare fence.
    """
    t = qmd_text.strip()
    lines = t.splitlines()
    if lines and re.match(r"^```[\w-]*\s*$", lines[0]):
        lines = lines[1:]
        if lines and lines[-1].strip() == "```":
            lines = lines[:-1]
        return "\n".join(lines).strip()
    return t


_HR_DASH_RE = re.compile(r"^\s*-{3,}\s*$")


def neutralize_body_thematic_breaks(qmd_text: str) -> tuple:
    """Convert body `---` thematic-break lines to `***`. Returns (text, count).

    Pandoc reads a `---` … `---` block (after a blank line) as a YAML metadata
    block and errors when the content isn't a key:value mapping — the converter
    sometimes wraps a footnote/aside in `---` rules, which crashes the render with
    a `readBlockMapping`/`extractYaml` error. `***` renders identically as a
    thematic break but is never parsed as YAML or a setext heading.

    Leaves the document's leading frontmatter delimiters and anything inside ```
    fences untouched. Idempotent.
    """
    lines = qmd_text.split("\n")
    start = 0
    if lines and lines[0].strip() == "---":          # skip leading frontmatter block
        for i in range(1, len(lines)):
            if lines[i].strip() in ("---", "..."):
                start = i + 1
                break
    in_fence = False
    n = 0
    for i in range(start, len(lines)):
        if lines[i].lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if not in_fence and _HR_DASH_RE.match(lines[i]):
            lines[i] = "***"
            n += 1
    return "\n".join(lines), n


def close_unbalanced_fences(qmd_text: str) -> tuple:
    """Append a closing ``` if a fenced block is left open at end-of-document.

    The converter occasionally omits the closing ``` of the last raw-HTML table
    block, leaving the ```{=html} block unterminated; Pandoc then swallows the
    whole table as plain text (no grid, no cell colours). An odd count of fence
    lines means one is still open at EOF. Idempotent.
    Returns (text, closed).
    """
    open_fences = sum(1 for ln in qmd_text.splitlines() if ln.lstrip().startswith("```"))
    if open_fences % 2 == 1:
        return qmd_text.rstrip("\n") + "\n```\n", True
    return qmd_text, False
