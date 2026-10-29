"""Text extraction and normalization shared by verify checks.

Turns a PDF and a .qmd into comparable plain text so coverage can be measured without
formatting noise (hyphenation, ligatures, Markdown syntax).
"""

import re
import unicodedata

try:
    import fitz  # PyMuPDF
    _FITZ_AVAILABLE = True
except ImportError:
    _FITZ_AVAILABLE = False


# ── Normalization ───────────────────────────────────────────────────────────────

def normalize(text: str) -> str:
    """Lowercase, fold ligatures/accents, de-hyphenate line breaks, strip
    punctuation, collapse whitespace into a bag-comparable string."""
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")  # drop accents/ligatures
    text = re.sub(r"-\s*\n\s*", "", text)   # join hyphenated line breaks
    text = text.lower()
    text = re.sub(r"[^a-z0-9 ]+", " ", text)  # keep alphanumerics and space
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def tokens(text: str) -> list:
    return normalize(text).split()


def shingles(toks: list, k: int = 4) -> set:
    """Set of consecutive k-grams (tuples): order-aware, position-independent."""
    if len(toks) < k:
        return {tuple(toks)} if toks else set()
    return {tuple(toks[i:i + k]) for i in range(len(toks) - k + 1)}


def split_sentences(text: str) -> list:
    """Rough sentence split on . ! ? ; and newlines (PDFs lack clean boundaries)."""
    parts = re.split(r"(?<=[.!?;])\s+|\n+", text)
    return [p.strip() for p in parts if p.strip()]


# ── PDF text extraction ─────────────────────────────────────────────────────────

def _rect_center_in(rect, boxes) -> bool:
    cx, cy = (rect[0] + rect[2]) / 2.0, (rect[1] + rect[3]) / 2.0
    for b in boxes:
        if b[0] <= cx <= b[2] and b[1] <= cy <= b[3]:
            return True
    return False


def pdf_lines(pdf_path, exclude_boxes_by_page: dict = None) -> list:
    """Return [(page_idx, line_text), …] for the whole PDF.

    exclude_boxes_by_page: {page_idx: [(x0,y0,x1,y1), …]} — lines whose center
    falls inside any box on their page are dropped (e.g. figure-internal text).
    """
    if not _FITZ_AVAILABLE:
        raise RuntimeError("PyMuPDF (fitz) is required for PDF text extraction.")
    exclude_boxes_by_page = exclude_boxes_by_page or {}
    out = []
    doc = fitz.open(str(pdf_path))
    try:
        for pno in range(doc.page_count):
            boxes = exclude_boxes_by_page.get(pno, [])
            for block in doc[pno].get_text("dict").get("blocks", []):
                for line in block.get("lines", []):
                    if boxes and _rect_center_in(line["bbox"], boxes):
                        continue
                    txt = "".join(s["text"] for s in line["spans"]).strip()
                    if txt:
                        out.append((pno, txt))
    finally:
        doc.close()
    return out


# ── HTML tables ──────────────────────────────────────────────────────────────────

def top_level_html_tables(text: str) -> list:
    """Full HTML of each TOP-LEVEL <table>...</table>. Depth-aware, so nested
    tables stay inside their parent instead of truncating it."""
    tables = []
    depth, start = 0, None
    for m in re.finditer(r"<table\b|</table\s*>", text, re.IGNORECASE):
        if m.group().lower().startswith("<table"):
            if depth == 0:
                start = m.start()
            depth += 1
        else:
            depth = max(0, depth - 1)
            if depth == 0 and start is not None:
                tables.append(text[start:m.end()])
                start = None
    return tables


# ── .qmd → plain text ────────────────────────────────────────────────────────────

def qmd_to_plain(qmd_text: str) -> str:
    """Strip frontmatter and Markdown decoration down to comparable prose,
    table-cell text, and figure captions."""
    # drop YAML frontmatter
    qmd_text = re.sub(r"^---\s*\n.*?\n---\s*\n", "", qmd_text, count=1, flags=re.DOTALL)
    # image refs: keep the caption (alt text), drop the path
    qmd_text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", qmd_text)
    # links: keep the link text
    qmd_text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", qmd_text)
    # raw-HTML table fences (```{=html} … ```): keep the inner HTML
    qmd_text = re.sub(r"```\{=html\}\s*\n(.*?)\n```", r"\1", qmd_text, flags=re.DOTALL)
    # HTML tags to spaces, then unescape entities. Match only real tags (no newline
    # inside) so a literal '<' in prose, e.g. "water bodies (< 30%)", doesn't open a
    # phantom tag that swallows everything to the next '>' far below.
    qmd_text = re.sub(r"</?[a-zA-Z!][^>\n]*>", " ", qmd_text)
    qmd_text = (qmd_text.replace("&lt;", "<").replace("&gt;", ">")
                .replace("&amp;", "&").replace("&nbsp;", " "))
    # table pipes to spaces (keep cell text)
    qmd_text = qmd_text.replace("|", " ")
    # drop table divider rows
    qmd_text = re.sub(r"^\s*[-:\s]+\s*$", "", qmd_text, flags=re.MULTILINE)
    # heading/list/emphasis markers, footnote refs, inline code ticks
    qmd_text = re.sub(r"\[\^[^\]]*\]", " ", qmd_text)
    qmd_text = re.sub(r"[#>*_`]+", " ", qmd_text)
    return qmd_text
