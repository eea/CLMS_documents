"""Phase 4: short-line matching in text_coverage.

A short correspondence line (`X → class Y`) present in the .qmd must NOT be
reported missing; a genuinely-absent short line still must be; long paragraphs
keep using shingle matching.
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from pdf_to_qmd.verify.checks.text_coverage import _short_line_covered  # noqa: E402
from pdf_to_qmd.verify.textutil import tokens  # noqa: E402


def _index(qmd_plain: str):
    qtoks = tokens(qmd_plain)
    positions = {}
    for i, t in enumerate(qtoks):
        positions.setdefault(t, []).append(i)
    return qtoks, positions


def test_present_short_arrow_line_is_covered():
    # the .qmd renders the correspondence line (arrow is stripped by normalize)
    qmd = "Some intro text. Allotment gardens class 1.4. More text follows here."
    qtoks, pos = _index(qmd)
    line = tokens("Allotment gardens class 1.4")
    assert _short_line_covered(line, qtoks, pos)


def test_present_with_one_extra_token_still_covered():
    # a footnote superscript sneaks a token into the middle — windowed match tolerates it
    qmd = "Allotment gardens ¹ class 1.4 are complexes of land parcels."
    qtoks, pos = _index(qmd)
    line = tokens("Allotment gardens class 1.4")
    assert _short_line_covered(line, qtoks, pos)


def test_genuinely_absent_short_line_reported_missing():
    qmd = "This document is about urban land cover classes and nomenclature."
    qtoks, pos = _index(qmd)
    line = tokens("Zebra crossings map to class 9.9")
    assert not _short_line_covered(line, qtoks, pos)


def test_scattered_words_not_falsely_covered():
    # the needle tokens all exist in the doc but far apart — must NOT count as covered
    qmd = ("Allotment plots appear early. " + "filler " * 40 +
           "gardens of a different kind. " + "filler " * 40 + "class system. ")
    qtoks, pos = _index(qmd)
    line = tokens("Allotment gardens class 1.4")
    assert not _short_line_covered(line, qtoks, pos)
