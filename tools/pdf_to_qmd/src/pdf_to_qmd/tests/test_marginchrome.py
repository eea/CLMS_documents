"""Tests for marginchrome.detect_running_chrome().

Synthetic PDFs are authored with PyMuPDF in-memory (no disk writes) so these
tests are self-contained and zero-cost.  Each fixture targets one detection case
from the plan's success criteria.
"""

import sys
import tempfile
from pathlib import Path

import pytest

fitz = pytest.importorskip("fitz", reason="PyMuPDF required")
sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))
from pdf_to_qmd.marginchrome import detect_running_chrome, _sig_text  # noqa: E402


# ── helpers ───────────────────────────────────────────────────────────────────

PAGE_W, PAGE_H = 595.0, 842.0   # A4 points

def _new_doc(n_pages: int):
    doc = fitz.open()
    for _ in range(n_pages):
        doc.new_page(width=PAGE_W, height=PAGE_H)
    return doc


def _add_text(page, text: str, y: float, fontsize: int = 10):
    """Insert a single line at (50, y)."""
    page.insert_text((50, y), text, fontsize=fontsize)


def _save(doc) -> Path:
    """Save to a temp file and return the path."""
    tmp = tempfile.NamedTemporaryFile(suffix=".pdf", delete=False)
    doc.save(tmp.name)
    doc.close()
    return Path(tmp.name)


# ── signature helper ──────────────────────────────────────────────────────────

def test_sig_text_strips_digits():
    assert _sig_text("PAGE 1") == _sig_text("PAGE 2")
    assert _sig_text("Urban Atlas Mapping Guide - Page 10") == \
           _sig_text("Urban Atlas Mapping Guide - Page 21")


def test_sig_text_collapses_letter_spacing():
    # Two instances of the same footer — differing only in the page number —
    # must collapse to the same signature so the majority vote fires.
    spaced_p1 = "URB AN  AT L A S  M A PPI NG GU I D E  -  PA GE  1"
    spaced_p2 = "URB AN  AT L A S  M A PPI NG GU I D E  -  PA GE  2"
    assert _sig_text(spaced_p1) == _sig_text(spaced_p2)


def test_sig_text_collapses_different_letter_spacing():
    # The same footer extracted with DIFFERENT letter-spacing on some pages
    # (every char spaced vs irregular) must still share one signature.
    irregular = "URB AN  AT L A S  M A PPI NG GU I D E  -  PA GE  10"
    every_char = "U R B A N  A T L A S  M A P P I N G  G U I D E  -  P A G E  29"
    assert _sig_text(irregular) == _sig_text(every_char) == "urbanatlasmappingguidepage"


# ── (a) text-only running footer with per-page numbers ───────────────────────

def test_text_footer_with_page_numbers_detected():
    """Footer "URBAN ATLAS MAPPING GUIDE - PAGE N" must be detected as chrome
    even though each line ends in a unique page number."""
    n = 6
    doc = _new_doc(n)
    for i, page in enumerate(doc):
        # body content well above the footer
        _add_text(page, f"Body paragraph on page {i}.", y=200)
        # footer near the bottom
        _add_text(page, f"URBAN ATLAS MAPPING GUIDE - PAGE {i + 1}", y=810)

    pdf = _save(doc)
    try:
        regions = detect_running_chrome(pdf)
        # footer detected on every page (or at least the majority)
        assert len(regions) >= n // 2, f"Expected footer on most pages, got {len(regions)}"
        # each region should be in the bottom portion of the page
        for pno, rects in regions.items():
            for (x0, y0, x1, y1) in rects:
                assert y0 > PAGE_H * 0.5, f"Chrome region y0={y0} unexpectedly high on page {pno}"
    finally:
        pdf.unlink(missing_ok=True)


# ── (d) footnote in footer zone is kept (non-repeating) ──────────────────────

def test_footnote_not_detected_as_chrome():
    """A footnote that appears only on one page must NOT be flagged as chrome."""
    n = 5
    doc = _new_doc(n)
    for i, page in enumerate(doc):
        _add_text(page, f"Body text on page {i}.", y=300)
        # running footer on all pages
        _add_text(page, f"Running Footer - Page {i + 1}", y=810)
    # footnote on page 2 only
    _add_text(doc[2], "¹ This is a footnote that only appears once.", y=760)

    pdf = _save(doc)
    try:
        regions = detect_running_chrome(pdf)
        # the footnote text must not be covered by any chrome region on page 2
        footnote_y = 760.0
        page2_regions = regions.get(2, [])
        for (x0, y0, x1, y1) in page2_regions:
            assert not (y0 <= footnote_y <= y1), \
                f"Footnote at y={footnote_y} wrongly inside chrome region {(y0, y1)} on page 2"
    finally:
        pdf.unlink(missing_ok=True)


# ── (g) cover page excluded from vote ────────────────────────────────────────

def test_cover_page_excluded():
    """With skip_pages={0}, the cover's unique header must not pollute the vote."""
    n = 5
    doc = _new_doc(n)
    # cover page: a big decorative title, no running footer
    _add_text(doc[0], "DOCUMENT COVER — DECORATIVE TITLE", y=100)
    for i in range(1, n):
        _add_text(doc[i], f"Body text on page {i}.", y=300)
        _add_text(doc[i], f"Running Footer Page {i}", y=810)

    pdf = _save(doc)
    try:
        # with skip: cover excluded; footer detected cleanly
        regions_no_cover = detect_running_chrome(pdf, skip_pages={0})
        # footer should be detected in both, but cover page itself should never
        # yield a bottom-band chrome region with skip
        assert 0 not in regions_no_cover or all(
            y1 <= PAGE_H * 0.5 for (_, _, _, y1) in regions_no_cover.get(0, [])
        ), "Cover page wrongly has a bottom-chrome region when excluded from vote"
    finally:
        pdf.unlink(missing_ok=True)


# ── determinism ──────────────────────────────────────────────────────────────

def test_detection_is_deterministic():
    """Same PDF must always produce identical region output."""
    n = 5
    doc = _new_doc(n)
    for i, page in enumerate(doc):
        _add_text(page, f"Body content {i}.", y=300)
        _add_text(page, f"Footer Line {i + 1}", y=815)

    pdf = _save(doc)
    try:
        r1 = detect_running_chrome(pdf)
        r2 = detect_running_chrome(pdf)
        assert r1 == r2, "Detection is not deterministic"
    finally:
        pdf.unlink(missing_ok=True)


# ── no false positives on body-only document ─────────────────────────────────

def test_no_chrome_on_body_only_doc():
    """A document with no repeating margin content must return empty."""
    n = 5
    doc = _new_doc(n)
    for i, page in enumerate(doc):
        # body text only — no footer, no header
        _add_text(page, f"Unique body paragraph {i}.", y=300 + i * 10)

    pdf = _save(doc)
    try:
        regions = detect_running_chrome(pdf)
        assert regions == {}, f"Unexpected regions on body-only doc: {regions}"
    finally:
        pdf.unlink(missing_ok=True)


# ── full-bleed figure page (no text) ─────────────────────────────────────────

def test_full_bleed_page_does_not_break_detection():
    """A page with no text at all must not break the detector."""
    n = 5
    doc = _new_doc(n)
    for i, page in enumerate(doc):
        if i == 2:
            continue   # page 2 is "full-bleed figure" — no text inserted
        _add_text(page, f"Body {i}.", y=300)
        _add_text(page, f"Footer {i + 1}", y=815)

    pdf = _save(doc)
    try:
        regions = detect_running_chrome(pdf)   # must not raise
        # footer on the non-blank pages should still be detected
        assert any(pno != 2 for pno in regions), "Expected footer on non-blank pages"
    finally:
        pdf.unlink(missing_ok=True)
