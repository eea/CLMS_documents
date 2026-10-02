"""Phase 1 orchestration: strip chrome, gate pages, detect, crop, placeholders.

  Step 0  strip repeating header/footer chrome -> working.pdf
  Step 1  local page gate: keep only pages that could hold an illustration
  Step 2  per-page Gemini figure detection on candidates only
  Step 3  refine geometry, crop, inject numbered placeholders

No conversion happens here. The operator inspects the artifacts and signs off
before the PDF->qmd conversion.

Outputs (in out_dir):
    <stem>.working.pdf            chrome-stripped copy, kept for traceability
    <stem>.placeholders.pdf       working.pdf with each figure replaced by a [FIG_n] box
    <stem>-media/img-<md5>.png    cropped illustration rasters
    detections.json               FIG_n -> file/page/bbox plus gate+chrome summary
"""

import json
import logging
from pathlib import Path

from .chrome import strip_chrome
from .cover import DEFAULT_COVER_MODEL, extract_cover_metadata, looks_like_cover
from .detect import detect_figures, find_oversized_tables
from .pagefilter import DEFAULT_MAX_ASPECT_RATIO, DEFAULT_MIN_CLUSTER_PT, filter_pages
from .placeholders import inject_placeholders
from .regions import DEFAULT_FIGURE_DPI, materialize_figures, write_sidecar

log = logging.getLogger(__name__)


def _overlaps_any(region, existing, frac: float = 0.5) -> bool:
    """True if `region` overlaps any same-page region by more than `frac` of its
    own area — guards against cropping a table the LLM already flagged twice."""
    ax0, ay0, ax1, ay1 = region.bbox
    area = max((ax1 - ax0) * (ay1 - ay0), 1e-6)
    for e in existing:
        if e.page != region.page:
            continue
        bx0, by0, bx1, by1 = e.bbox
        ix = max(0.0, min(ax1, bx1) - max(ax0, bx0))
        iy = max(0.0, min(ay1, by1) - max(ay0, by0))
        if ix * iy / area > frac:
            return True
    return False


def run_phase1(
    pdf_path: Path,
    out_dir: Path,
    *,
    api_key: str,
    model: str,
    figure_dpi: int = DEFAULT_FIGURE_DPI,
    page_dpi: int = 150,
    refine: bool = True,
    do_strip_chrome: bool = True,
    do_gate_pages: bool = True,
    do_cover: bool = True,
    cover_model: str = DEFAULT_COVER_MODEL,
    min_cluster_pt: float = DEFAULT_MIN_CLUSTER_PT,
    max_aspect_ratio: float = DEFAULT_MAX_ASPECT_RATIO,
    events=None,
    timeout: int = 300,
    detect_workers: int = 1,
) -> dict:
    """Run the full Phase 1 pipeline. Returns a summary dict."""
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = pdf_path.stem

    # keep a copy of the original so later stages (e.g. verify, which diffs
    # against the source) are self-contained.
    import shutil
    source_copy = out_dir / f"{stem}.source.pdf"
    if pdf_path.resolve() != source_copy.resolve():
        shutil.copy2(pdf_path, source_copy)

    # ── Step 0: strip header/footer chrome ────────────────────────────────────
    chrome_report = {"images_removed": 0, "pages_affected": 0, "total_pages": 0}
    if do_strip_chrome:
        working_pdf = out_dir / f"{stem}.working.pdf"
        log.info("[Step 0] Stripping header/footer chrome …")
        # cover_exclude is populated in Step 0b (below) but we need the is_cover
        # signal *before* the strip for the text-chrome vote.  Peek at page 0 now.
        _peek_is_cover = False
        if do_cover:
            try:
                import fitz as _fitz
                _d = _fitz.open(str(pdf_path))
                _peek_is_cover = looks_like_cover(_d[0])
                _d.close()
            except Exception:
                _peek_is_cover = True  # conservative: exclude page 0 when unsure
        chrome_report = strip_chrome(pdf_path, working_pdf,
                                     skip_pages={0} if _peek_is_cover else set())
        if events:
            events.chrome_done(chrome_report)
    else:
        working_pdf = pdf_path
        log.info("[Step 0] Chrome stripping skipped (--no-strip-chrome)")

    # ── Step 0b: cover-page detection + metadata extraction ──────────────────
    # runs on the working PDF (logos already stripped); page 0 is dropped from
    # the candidate list so its decorative image is never cropped as a figure.
    cover_block = None
    cover_exclude = set()
    cover_cost = 0.0
    if do_cover:
        try:
            import fitz
            doc = fitz.open(str(working_pdf))
            cover_page = doc[0]
            is_cover = looks_like_cover(cover_page)
            doc.close()
        except Exception as exc:
            log.debug("cover: page-check failed (%s); assuming cover", exc)
            is_cover = True
        if is_cover:
            log.info("[Step 0b] Cover page detected — extracting metadata …")
            fields, cover_cost = extract_cover_metadata(
                working_pdf, api_key=api_key, model=cover_model
            )
            cover_block = {"is_cover": True, "fields": fields}
            cover_exclude = {0}
            if events:
                events.cover_done(fields)
            log.info("[Step 0b] Cover page excluded from figure detection")
        else:
            log.info("[Step 0b] Page 1 does not look like a cover; no special handling")
            cover_block = {"is_cover": False, "fields": {}}

    # ── Step 1: local page gate ────────────────────────────────────────────────
    gate_report = {"candidates": [], "skipped": [], "total_pages": 0}
    if do_gate_pages:
        log.info("[Step 1] Gating candidate pages …")
        gate_report = filter_pages(
            working_pdf, min_cluster_pt=min_cluster_pt, max_aspect_ratio=max_aspect_ratio
        )
        page_indices = [i for i in gate_report["candidates"] if i not in cover_exclude]
        n_cover_dropped = len(gate_report["candidates"]) - len(page_indices)
        log.info(
            "[Step 1] %d/%d pages are candidates (skipping %d%s)",
            len(page_indices), gate_report["total_pages"], len(gate_report["skipped"]),
            ", cover page excluded" if n_cover_dropped else "",
        )
        if events:
            events.gate_done(len(page_indices), len(gate_report["skipped"]), gate_report["total_pages"])
    else:
        # exclude the cover page even with the gate off
        if cover_exclude:
            doc_tmp = None
            try:
                import fitz
                doc_tmp = fitz.open(str(working_pdf))
                page_indices = [i for i in range(doc_tmp.page_count) if i not in cover_exclude]
                doc_tmp.close()
            except Exception:
                page_indices = None   # fall back to all pages
        else:
            page_indices = None  # all pages
        log.info("[Step 1] Page gate skipped (--no-gate)")

    # ── Step 2: LLM detection on candidate pages ───────────────────────────────
    log.info("[Step 2] Running figure detector …")
    regions, detect_cost = detect_figures(
        working_pdf,
        api_key=api_key,
        model=model,
        page_dpi=page_dpi,
        page_indices=page_indices,
        events=events,
        timeout=timeout,
        workers=detect_workers,
    )

    # ── Step 2b: oversized tables (local), crop as figures ─────────────────────
    # the convert LLM silently drops huge tables (thousands of cells blow its
    # output budget), so crop them as images across all pages. illegible as
    # data at that size anyway.
    log.info("[Step 2b] Scanning for oversized tables …")
    oversized = [r for r in find_oversized_tables(working_pdf)
                 if not _overlaps_any(r, regions)]
    if oversized:
        log.info("[Step 2b] %d oversized table(s), cropping as figures", len(oversized))
        regions = regions + oversized

    # ── Step 3: refine, crop, inject placeholders ──────────────────────────────
    media_dir = out_dir / f"{stem}-media"
    placeholders_pdf = out_dir / f"{stem}.placeholders.pdf"
    sidecar = out_dir / "detections.json"

    figures = materialize_figures(
        working_pdf, regions, media_dir, dpi=figure_dpi, refine=refine
    )
    others = [r for r in regions if r.rtype != "figure"]

    inject_placeholders(working_pdf, figures, placeholders_pdf)
    write_sidecar(sidecar, figures, others, cover=cover_block)

    summary = {
        "chrome_images_removed": chrome_report["images_removed"],
        "chrome_pages_affected": chrome_report["pages_affected"],
        "pages_total": gate_report.get("total_pages") or (
            regions[0].page + 1 if regions else 0
        ),
        "pages_candidate": len(page_indices) if page_indices is not None else gate_report.get("total_pages", 0),
        "pages_skipped": len(gate_report.get("skipped", [])),
        "cover": cover_block,
        "cost_usd": {"cover": cover_cost, "detect": detect_cost},
        "figures": len(figures),
        "tables": sum(1 for r in others if r.rtype == "table"),
        "chrome_detected": sum(1 for r in others if r.rtype == "chrome"),
        "working_pdf": working_pdf,
        "placeholders_pdf": placeholders_pdf,
        "media_dir": media_dir,
        "sidecar": sidecar,
    }
    log.info(
        "Phase 1 done: chrome_removed=%d, pages=%d/%d sent, figures=%d",
        summary["chrome_images_removed"],
        summary["pages_candidate"],
        summary["pages_total"],
        summary["figures"],
    )

    # JSON-safe summary so a later `--dry-run` replay can drive the UI from
    # artifacts with no LLM calls. candidate_pages records the indices the
    # detector saw so replay reproduces the per-page list.
    candidate_pages = (
        list(page_indices) if page_indices is not None
        else list(range(summary["pages_total"]))
    )
    phase1_json = {
        "chrome_images_removed": summary["chrome_images_removed"],
        "chrome_pages_affected": summary["chrome_pages_affected"],
        "pages_total": summary["pages_total"],
        "pages_candidate": summary["pages_candidate"],
        "pages_skipped": summary["pages_skipped"],
        "candidate_pages": candidate_pages,
        "cover": cover_block,
        "cost_usd": summary["cost_usd"],
        "figures": summary["figures"],
        "tables": summary["tables"],
    }
    (out_dir / "phase1.json").write_text(json.dumps(phase1_json, indent=1), encoding="utf-8")

    return summary
