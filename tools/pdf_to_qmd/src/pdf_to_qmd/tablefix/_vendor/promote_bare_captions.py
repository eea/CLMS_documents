# VENDORED VERBATIM from .github/scripts/qmd-tools/promote_bare_captions.py
# Copy kept in-tree so the standalone pdf_to_qmd tool stays decoupled from CI.
# If the production script changes, re-sync this copy (diff against source).
#!/usr/bin/env python3
"""
Promote bare table/figure captions into proper annotations.

The PDF/DOCX→qmd converters sometimes leave a caption as a plain paragraph
("Table 3: ...", "*Table 3: ...*", "Figure 9: ...") sitting next to its float
instead of annotating it, so it renders as ordinary body text in HTML/PDF. This
rewrite repairs that:

  - a bare "Table N:" caption adjacent to a table — pipe, `{=html}`, or a
    table-as-image `![](...)` — is wrapped in a `::: {.tbl-caption}` div placed
    directly above the float (the convention the rest of the library uses);
  - a bare "Figure N:" caption next to an empty-alt image is folded into that
    image's alt text (`![Figure N: ...](path)`), which Quarto renders as a real
    figcaption.

Attachment is directional: prefer the float immediately BELOW the caption (these
docs caption above their float), else the float immediately ABOVE. When a caption
sits below a CLUSTER of stacked floats (ambiguous which one it belongs to) it is
left untouched for a human to resolve. Runs of 3+ consecutive caption paragraphs
(a "List of Tables/Figures" index) are left alone. Deterministic and idempotent.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# Caption blue — must match build_tbl_caption in
# tools/pdf_to_qmd/src/pdf_to_qmd/resolve.py and the Typst template's caption-blue.
_TBL_CAPTION_FILL = "#3E6893"
_CAPTION_ATTR_RE = re.compile(r"\s*\{[^}]*\}\s*$")

_TBL_RE = re.compile(r"^\s*\*{0,2}\s*Table\s+\d+\s*[.:]", re.I)
_FIG_RE = re.compile(r"^\s*\*{0,2}\s*Figure\s+\d+\s*[.:]", re.I)
_IMG_RE = re.compile(
    r"^(?P<pre>\s*)!\[(?P<alt>.*?)\]\((?P<tgt>[^)]*)\)(?P<attrs>\s*\{[^}]*\})?\s*$"
)
_EMPTY_IMG_RE = re.compile(r"^\s*!\[\s*\]\(")
_ROW_RE = re.compile(r"^\s*\|.*\|\s*$")
_HTML_OPEN_RE = re.compile(r"^\s*```\{=html\}\s*$")
_FENCE_RE = re.compile(r"^\s*```\s*$")
_CAPDIV_RE = re.compile(r"^\s*:::\s*\{\.tbl-caption\}")
_DIVCLOSE_RE = re.compile(r"^\s*:::\s*$")
_STAR_WRAP_RE = re.compile(r"^(\*{1,2})(.*?)(\*{1,2})$")


def build_tbl_caption(caption_text: str) -> str:
    """Return a `.tbl-caption` div for `caption_text`, or "" if no visible text.

    Output must stay byte-identical to build_tbl_caption in
    tools/pdf_to_qmd/src/pdf_to_qmd/resolve.py."""
    caption_text = _CAPTION_ATTR_RE.sub("", caption_text).strip()
    if not caption_text:
        return ""
    return (
        "::: {.tbl-caption}\n"
        "```{=typst}\n"
        f'#set text(size: 9pt, fill: rgb("{_TBL_CAPTION_FILL}"))\n'
        "```\n"
        f"{caption_text}\n"
        ":::"
    )


def _strip_markup(text: str) -> str:
    """Collapse a (possibly multi-line) caption to one line, stripping wrapping */**."""
    text = " ".join(s.strip() for s in text.splitlines()).strip()
    m = _STAR_WRAP_RE.match(text)
    if m and m.group(1) == m.group(3):
        text = m.group(2).strip()
    return text


def _next_nonblank(lines: list[str], k: int) -> int | None:
    while k < len(lines):
        if lines[k].strip():
            return k
        k += 1
    return None


def _prev_nonblank(lines: list[str], k: int) -> int | None:
    k -= 1
    while k >= 0:
        if lines[k].strip():
            return k
        k -= 1
    return None


def _float_block(lines: list[str], k: int | None):
    """If line k is (or bounds) a float, return (start, end_exclusive); else None.

    A float is a pipe table, a `{=html}` table block (matched from either edge),
    or a standalone `![](...)` image line."""
    if k is None or k < 0 or k >= len(lines):
        return None
    s = lines[k]
    if _IMG_RE.match(s):
        return (k, k + 1)
    if _ROW_RE.match(s):
        a = k
        while a - 1 >= 0 and _ROW_RE.match(lines[a - 1]):
            a -= 1
        b = k
        while b + 1 < len(lines) and _ROW_RE.match(lines[b + 1]):
            b += 1
        return (a, b + 1)
    if _HTML_OPEN_RE.match(s):
        b = k + 1
        while b < len(lines) and not _FENCE_RE.match(lines[b]):
            b += 1
        return (k, min(b + 1, len(lines)))
    if _FENCE_RE.match(s):  # may be an {=html} block's closing fence
        a = k - 1
        while a >= 0 and not _FENCE_RE.match(lines[a]):
            if _HTML_OPEN_RE.match(lines[a]):
                return (a, k + 1)
            a -= 1
    return None


def _in_capdiv(lines: list[str], i: int) -> bool:
    """True if line i is inside an open `::: {.tbl-caption}` div (non-nested)."""
    for k in range(i - 1, -1, -1):
        if _CAPDIV_RE.match(lines[k]):
            return True
        if _DIVCLOSE_RE.match(lines[k]):
            return False
    return False


def _index_run_lines(lines: list[str]) -> set[int]:
    """Line indices belonging to a run of 3+ consecutive caption paragraphs."""
    out: set[int] = set()
    i = 0
    while i < len(lines):
        if (_TBL_RE.match(lines[i]) or _FIG_RE.match(lines[i])) and not _IMG_RE.match(lines[i]):
            members, j = [], i
            while j < len(lines):
                if (_TBL_RE.match(lines[j]) or _FIG_RE.match(lines[j])) and not _IMG_RE.match(lines[j]):
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


def _caption_block_end(lines: list[str], i: int) -> int:
    """Exclusive end of the caption paragraph starting at i (stops at blank/float/new caption)."""
    j = i + 1
    while j < len(lines):
        s = lines[j]
        if not s.strip() or _float_block(lines, j) or _TBL_RE.match(s) or _FIG_RE.match(s):
            break
        j += 1
    return j


def promote_bare_captions(text: str) -> tuple[str, int]:
    """Promote bare table/figure captions to annotations. Returns (text, count)."""
    lines = text.split("\n")
    idx = _index_run_lines(lines)
    ops: list[tuple[int, int, list[str]]] = []  # (start, end_excl, replacement)
    count = 0

    i = 0
    while i < len(lines):
        line = lines[i]
        is_tbl, is_fig = bool(_TBL_RE.match(line)), bool(_FIG_RE.match(line))
        if (not (is_tbl or is_fig)) or i in idx or _IMG_RE.match(line) or _in_capdiv(lines, i):
            i += 1
            continue

        ce = _caption_block_end(lines, i)
        cap = _strip_markup("\n".join(lines[i:ce]))

        if is_fig:
            # A figure caption folds into an adjacent EMPTY-ALT image's alt text
            # (prefer the image below, else above). An image that already carries
            # alt text or a #fig- id is a real figure and is left untouched — so a
            # stray caption next to an already-captioned figure is not mis-folded.
            target_img = None
            for fi in (_next_nonblank(lines, ce), _prev_nonblank(lines, i)):
                if fi is None:
                    continue
                m = _IMG_RE.match(lines[fi])
                if m and _EMPTY_IMG_RE.match(lines[fi]) and "#fig-" not in (m.group("attrs") or ""):
                    target_img = (fi, m)
                    break
            if target_img is None:
                i = ce
                continue
            fi, m = target_img
            new_img = f"{m.group('pre')}![{cap}]({m.group('tgt')}){m.group('attrs') or ''}"
            ops.append((fi, fi + 1, [new_img]))
            ops.append((i, ce, []))
            count += 1
            i = ce
            continue

        # Table caption: wrap in a `.tbl-caption` div above its float. Prefer the
        # float below the caption (these docs caption above), else the one above.
        below = _float_block(lines, _next_nonblank(lines, ce))
        above = _float_block(lines, _prev_nonblank(lines, i))
        target, side = (below, "below") if below else (above, "above") if above else (None, None)
        if target is None:
            i = ce
            continue

        # Conservative skip: a caption below a cluster of stacked table-IMAGES is
        # ambiguous — each image is a separate table needing its own caption, so
        # attaching to the nearest would mislabel it. Leave it for manual fixing.
        # Stacked pipe tables are fragments of one table, so nearest-above is fine.
        if side == "above" and (target[1] - target[0] == 1) and _IMG_RE.match(lines[target[0]]):
            prev = _float_block(lines, _prev_nonblank(lines, target[0]))
            if prev is not None and (prev[1] - prev[0] == 1) and _IMG_RE.match(lines[prev[0]]):
                i = ce
                continue

        div = build_tbl_caption(cap)
        if not div:
            i = ce
            continue
        fs = target[0]
        if side == "below":
            ops.append((i, fs, div.split("\n") + [""]))   # caption+blanks before float -> div+blank
        else:
            ops.append((fs, fs, div.split("\n") + [""]))  # insert div above the float
            ops.append((i, ce, []))                       # remove the bare caption
        count += 1
        i = ce

    for start, end, repl in sorted(ops, key=lambda o: o[0], reverse=True):
        lines[start:end] = repl
    return "\n".join(lines), count


def process_file(qmd: Path, overwrite: bool = True) -> int:
    text = qmd.read_text(encoding="utf-8")
    new_text, count = promote_bare_captions(text)
    if count and new_text != text:
        qmd.write_text(new_text, encoding="utf-8")
    return count


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("root", help="directory scanned recursively for *.qmd")
    args = ap.parse_args()
    root = Path(args.root)
    if not root.exists():
        print(f"❌ not found: {root}")
        return 1
    total = 0
    for qmd in sorted(root.rglob("*.qmd")):
        n = process_file(qmd)
        if n:
            print(f"  promoted {n:3d} caption(s) in {qmd.relative_to(root)}")
            total += n
    print(f"\ntotal captions promoted: {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
