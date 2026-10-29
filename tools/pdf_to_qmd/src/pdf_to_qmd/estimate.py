"""Pre-flight cost estimation.

Built from free local signals (pages, candidate_pages, text_chars) times per-unit USD
costs calibrated from past runs' phase1.json/result.json sidecars, seeded when there's
no history.

detect predicts well (~linear in a known candidate-page count). convert is fuzzy: its
cost is dominated by the not-yet-existing output .qmd, so it's predicted by analogy
($/source-page) with a wide band. This is a guardrail against a 5-10x surprise, not an
invoice; the high band is deliberately generous since under-estimation is the dangerous
direction.
"""

import json
import logging
from pathlib import Path

log = logging.getLogger(__name__)

# ── Seed per-unit costs (USD), from the 2026-06 calibration runs ────────────────
# PUM:  detect 0.0294/2 candidate-pages ≈ 0.0147;  convert 0.194/9 pages ≈ 0.0216
# QA:   detect 0 (no candidates);                  convert 0.180/4 pages ≈ 0.0450
# convert/page varies a lot with table density, so seed toward the higher end.
SEED_COVER_USD = 0.005                  # a flash cover call when it fires
SEED_DETECT_USD_PER_CANDIDATE = 0.015
SEED_CONVERT_USD_PER_PAGE = 0.035

# band multipliers on the convert term (the uncertain one); detect is left tight
_CONVERT_LOW = 0.5
_CONVERT_HIGH = 3.0


def _read_json(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception:
        return None


def load_calibration(out_root: Path) -> dict:
    """Aggregate real per-unit costs from sidecars under out_root/*/, falling back to
    seed constants for any unit with no history."""
    detect_cost = detect_pages = 0.0
    convert_cost = convert_pages = 0.0
    n_docs = 0
    if out_root and out_root.exists():
        for d in out_root.iterdir():
            if not d.is_dir() or d.name.startswith("_"):
                continue
            p1 = _read_json(d / "phase1.json")
            res = _read_json(d / "result.json")
            if not p1 or not res:
                continue
            n_docs += 1
            pc = res.get("phase_cost") or {}
            cand = p1.get("pages_candidate") or 0
            pages = p1.get("pages_total") or 0
            if cand:
                detect_cost += pc.get("detect", 0.0)
                detect_pages += cand
            if pages:
                convert_cost += pc.get("convert", 0.0)
                convert_pages += pages
    return {
        "cover_usd": SEED_COVER_USD,
        "detect_usd_per_candidate": (detect_cost / detect_pages) if detect_pages
        else SEED_DETECT_USD_PER_CANDIDATE,
        "convert_usd_per_page": (convert_cost / convert_pages) if convert_pages
        else SEED_CONVERT_USD_PER_PAGE,
        "n_calibration_docs": n_docs,
    }


def _local_signals(pdf: Path) -> dict:
    """Page count, candidate-page count (local gate), and text length. Returns zeros
    for any signal that can't be computed."""
    import tempfile

    import fitz

    from .chrome import strip_chrome
    from .pagefilter import filter_pages

    pages = text_chars = 0
    try:
        doc = fitz.open(str(pdf))
        pages = doc.page_count
        text_chars = sum(len(doc[i].get_text() or "") for i in range(pages))
        doc.close()
    except Exception as exc:
        log.debug("estimate: could not read %s (%s)", pdf, exc)

    # mirror the real pipeline: gate a chrome-stripped temp copy so header/footer
    # logos don't inflate the candidate count
    candidate_pages = 0
    gate_log = logging.getLogger("pdf_to_qmd.pagefilter")
    chrome_log = logging.getLogger("pdf_to_qmd.chrome")
    prev = (gate_log.level, chrome_log.level)
    gate_log.setLevel(logging.WARNING)
    chrome_log.setLevel(logging.WARNING)
    try:
        with tempfile.TemporaryDirectory() as td:
            gate_target = pdf
            try:
                stripped = Path(td) / "stripped.pdf"
                strip_chrome(pdf, stripped)
                if stripped.exists():
                    gate_target = stripped
            except Exception as exc:
                log.debug("estimate: chrome strip failed (%s) — gating raw PDF", exc)
            candidate_pages = len(filter_pages(gate_target).get("candidates", []))
    except Exception as exc:
        log.debug("estimate: gate failed on %s (%s) — assuming all pages candidate", pdf, exc)
        candidate_pages = pages
    finally:
        gate_log.setLevel(prev[0])
        chrome_log.setLevel(prev[1])

    return {"pages": pages, "candidate_pages": candidate_pages, "text_chars": text_chars}


def estimate_file(pdf: Path, calib: dict = None, *, out_root: Path = None) -> dict:
    """Estimate the USD cost of converting `pdf` before any spend.

    Returns expected_usd / low_usd / high_usd plus the signals and per-phase breakdown
    used."""
    if calib is None:
        calib = load_calibration(out_root) if out_root else {
            "cover_usd": SEED_COVER_USD,
            "detect_usd_per_candidate": SEED_DETECT_USD_PER_CANDIDATE,
            "convert_usd_per_page": SEED_CONVERT_USD_PER_PAGE,
            "n_calibration_docs": 0,
        }
    sig = _local_signals(pdf)

    cover = calib["cover_usd"]
    detect = sig["candidate_pages"] * calib["detect_usd_per_candidate"]
    convert = sig["pages"] * calib["convert_usd_per_page"]
    expected = cover + detect + convert

    # convert carries the uncertainty; detect is tight
    low = cover + detect + _CONVERT_LOW * convert
    high = cover + detect + _CONVERT_HIGH * convert

    return {
        "expected_usd": round(expected, 6),
        "low_usd": round(low, 6),
        "high_usd": round(high, 6),
        "pages": sig["pages"],
        "candidate_pages": sig["candidate_pages"],
        "text_chars": sig["text_chars"],
        "breakdown": {"cover": round(cover, 6), "detect": round(detect, 6),
                      "convert": round(convert, 6)},
        "calibrated": bool(calib.get("n_calibration_docs")),
    }
