"""Media handling: raster extraction (PyMuPDF), manifest parsing, and resolving
the model's FIGURE_<n> placeholders to content-hash filenames. Applies the
manifest's keep/drop disposition and reports figures it can't resolve.
"""

import hashlib
import json
import logging
import re
from collections import defaultdict
from pathlib import Path
from typing import Optional

# Lazy import so the package still loads without fitz
try:
    import fitz  # PyMuPDF
    _FITZ_AVAILABLE = True
except ImportError:
    _FITZ_AVAILABLE = False

log = logging.getLogger(__name__)

MIN_IMAGE_PX = 64  # drop images smaller than this in either dimension

# Header/footer "chrome" detection: an image that repeats across enough pages AND
# always sits in the top/bottom margin band is page furniture (logos, banners), not
# a figure. Repetition alone isn't enough — the margin check keeps body figures safe.
CHROME_PAGE_FRACTION = 0.5    # appears on >= 50% of pages
CHROME_MARGIN_BAND = 0.15     # top 15% or bottom 15% of page height


def _md5(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


# ── Raster extraction ─────────────────────────────────────────────────────────

def _is_chrome(pages: set, y_centers: list, total_pages: int) -> bool:
    """True if an image looks like repeating header/footer chrome.

    Needs both: repeats on >= CHROME_PAGE_FRACTION of pages (min 2), and every
    placement sits in the margin band. The position check stops a recurring body
    figure being mistaken for chrome.
    """
    if total_pages < 2 or len(pages) < 2:
        return False
    if len(pages) / total_pages < CHROME_PAGE_FRACTION:
        return False
    return all(
        yc < CHROME_MARGIN_BAND or yc > (1.0 - CHROME_MARGIN_BAND)
        for yc in y_centers
    )


def extract_rasters(pdf_path: Path, media_dir: Path) -> list:
    """Extract embedded raster images from the PDF in reading order.

    Returns dicts {path, page, y, x}. Drops sub-MIN_IMAGE_PX images and repeating
    header/footer chrome (see _is_chrome); dedups by content MD5.

    PyMuPDF only sees embedded rasters — vector figures aren't extracted and surface
    as unresolved FIGURE_<n> gaps.
    """
    if not _FITZ_AVAILABLE:
        raise RuntimeError(
            "PyMuPDF (fitz) is required for media extraction but is not installed. "
            "Run: pip install pymupdf"
        )
    media_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(str(pdf_path))
    total_pages = doc.page_count

    # ── Pass 1: collect every placement + image bytes (once per digest) ──
    placements: list[dict] = []          # {digest, page, y, x}
    blob: dict[str, dict] = {}           # digest -> {bytes, ext, w, h}
    pages_of: dict[str, set] = defaultdict(set)
    ycenters_of: dict[str, list] = defaultdict(list)

    for page_num, page in enumerate(doc):
        page_h = page.rect.height or 1.0
        for img_info in page.get_images(full=True):
            xref = img_info[0]
            try:
                base_image = doc.extract_image(xref)
            except Exception as exc:
                log.debug("Page %d: could not extract xref %d: %s", page_num, xref, exc)
                continue

            w, h = base_image["width"], base_image["height"]
            if w < MIN_IMAGE_PX or h < MIN_IMAGE_PX:
                log.debug("Page %d: skipping tiny image %dx%d (xref %d)", page_num, w, h, xref)
                continue

            digest = _md5(base_image["image"])
            if digest not in blob:
                blob[digest] = {
                    "bytes": base_image["image"],
                    "ext": base_image["ext"],
                    "w": w,
                    "h": h,
                }

            rects = page.get_image_rects(xref)
            bbox = rects[0] if rects else fitz.Rect(0, 0, 0, 0)
            pages_of[digest].add(page_num)
            ycenters_of[digest].append(((bbox.y0 + bbox.y1) / 2.0) / page_h)
            placements.append({"digest": digest, "page": page_num, "y": bbox.y0, "x": bbox.x0})

    doc.close()

    # ── Classify repeating header/footer chrome and drop it ─────────────────────
    chrome = {
        d for d in blob
        if _is_chrome(pages_of[d], ycenters_of[d], total_pages)
    }
    for d in chrome:
        b = blob[d]
        log.info(
            "Skipping header/footer chrome img-%s… (%dx%d, on %d/%d pages), not a figure",
            d[:8], b["w"], b["h"], len(pages_of[d]), total_pages,
        )

    # ── Pass 2: write non-chrome images, build the figure list ──────────────────
    saved: dict[str, Path] = {}
    images: list[dict] = []
    for p in placements:
        digest = p["digest"]
        if digest in chrome:
            continue
        if digest not in saved:
            b = blob[digest]
            img_path = media_dir / f"img-{digest}.{b['ext']}"
            img_path.write_bytes(b["bytes"])
            saved[digest] = img_path
            log.debug("extracted %s (%dx%d, %d bytes)", img_path.name, b["w"], b["h"], len(b["bytes"]))
        images.append({"path": saved[digest], "page": p["page"], "y": p["y"], "x": p["x"]})

    # reading order, then dedup paths preserving order
    images.sort(key=lambda i: (i["page"], i["y"], i["x"]))
    seen_paths: set[Path] = set()
    unique: list[dict] = []
    for item in images:
        if item["path"] not in seen_paths:
            seen_paths.add(item["path"])
            unique.append(item)

    log.info(
        "Extracted %d content raster(s) from %s (filtered %d chrome)",
        len(unique), pdf_path.name, len(chrome),
    )
    return unique


# ── Manifest parsing ──────────────────────────────────────────────────────────

def parse_manifest(response_text: str) -> tuple:  # (str, Optional[list])
    """Split the model response into (qmd_body, manifest_list).

    The model ends its output with a fenced ```json block holding the manifest.
    Missing or unparseable -> (response_text, None) and the caller falls back.
    """
    # the manifest is the LAST ```json … ``` block
    pattern = re.compile(r"```json\s*(.*?)```", re.DOTALL | re.IGNORECASE)
    matches = list(pattern.finditer(response_text))
    if not matches:
        log.warning("No JSON manifest in model response; falling back to all-figures")
        return response_text.rstrip(), None

    last_match = matches[-1]
    qmd_body = response_text[: last_match.start()].rstrip()
    json_text = last_match.group(1).strip()

    try:
        manifest = json.loads(json_text)
        if not isinstance(manifest, list):
            raise ValueError("Manifest must be a JSON array")
        return qmd_body, manifest
    except (json.JSONDecodeError, ValueError) as exc:
        log.warning("Could not parse JSON manifest (%s); falling back to all-figures", exc)
        return response_text.rstrip(), None


# ── Reference rewriting ───────────────────────────────────────────────────────

def rewrite_figures(
    qmd_body: str,
    rasters: list,
    manifest: Optional[list],
    media_dir: Path,
    qmd_path: Path,
) -> tuple:
    """Apply the manifest disposition, delete unwanted images, and resolve
    FIGURE_<n> placeholders to relative paths.

    Returns (rewritten_qmd_body, gap_report). gap_report entries:
    {"placeholder", "caption", "note"}.
    """
    gap_report: list[dict] = []

    if manifest is None:
        # fallback: treat every raster as a figure
        log.warning(
            "No manifest: treating all %d extracted rasters as figures. "
            "Figure mapping may be off; review the output.",
            len(rasters),
        )
        figure_paths = [r["path"] for r in rasters]
        low_confidence = True
    else:
        # manifest dispositions align to raster extraction order
        figure_paths: list[Path] = []
        low_confidence = False
        for i, entry in enumerate(manifest):
            disposition = entry.get("type", "figure")
            if i >= len(rasters):
                # more manifest entries than rasters (vector figures etc.)
                if disposition == "figure":
                    caption = entry.get("caption", f"ordinal {entry.get('ordinal', i+1)}")
                    gap_report.append({
                        "placeholder": f"FIGURE_{len(figure_paths) + 1}",
                        "caption": caption,
                        "note": "no extractable raster (likely vector figure)",
                    })
                continue

            raster_path = rasters[i]["path"]

            if disposition == "figure":
                figure_paths.append(raster_path)
            else:
                # table / decorative / diagram: not a figure, drop the raster
                try:
                    if raster_path.exists():
                        raster_path.unlink()
                        log.debug(
                            "Deleted %s (manifest type=%s)", raster_path.name, disposition
                        )
                except OSError as exc:
                    log.warning("Could not delete %s: %s", raster_path, exc)

    placeholder_pattern = re.compile(r"FIGURE_(\d+)")
    placeholders = sorted(
        set(int(m.group(1)) for m in placeholder_pattern.finditer(qmd_body))
    )

    def _rel(p: Path) -> str:
        return str(p.relative_to(qmd_path.parent)).replace("\\", "/")

    body = qmd_body
    for n in placeholders:
        idx = n - 1  # FIGURE_n is 1-based
        placeholder = f"FIGURE_{n}"
        if idx < len(figure_paths):
            rel_path = _rel(figure_paths[idx])
            body = body.replace(f"({placeholder})", f"({rel_path})")
            log.debug("Resolved %s → %s", placeholder, rel_path)
        else:
            # No raster for this placeholder. A literal "![caption](FIGURE_n)" would
            # make Typst/Quarto fail loading a file named "FIGURE_n", so swap in a
            # visible marker that keeps the caption — operator inserts the (usually
            # vector) figure by hand.
            img_re = re.compile(rf"!\[([^\]]*)\]\({re.escape(placeholder)}\)")
            m = img_re.search(body)
            caption = m.group(1) if m else ""
            marker_text = (
                f"figure not extracted: {caption}" if caption
                else f"figure not extracted ({placeholder})"
            )
            body = img_re.sub(f"*⚠ {marker_text}*", body)
            gap_report.append({
                "placeholder": placeholder,
                "caption": caption,
                "note": "no extracted raster available, likely vector figure",
            })
            log.warning(
                "%s has no matching extracted image; replaced with a visible marker",
                placeholder,
            )

    if low_confidence and rasters:
        gap_report.append({
            "placeholder": "ALL",
            "caption": "",
            "note": (
                "Low-confidence figure mapping (no manifest returned). "
                "Verify all figure references manually."
            ),
        })

    return body, gap_report
