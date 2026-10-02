#!/usr/bin/env python3
"""Tests for the pdf_to_qmd verify package (plugin checks)."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from pdf_to_qmd.verify import (  # noqa: E402
    CHECKS, CheckResult, VerifyContext, _load_checks, overall_status, run_verify, write_report,
)
from pdf_to_qmd.verify import textutil as tu  # noqa: E402


# ── textutil ────────────────────────────────────────────────────────────────────

class TestTextUtil:
    def test_normalize_dehyphenates_and_folds(self):
        assert tu.normalize("interpre-\ntation") == "interpretation"
        assert tu.normalize("Café RÉSUMÉ!") == "cafe resume"

    def test_qmd_to_plain_strips_frontmatter_and_syntax(self):
        qmd = ('---\ntitle: "T"\n---\n\n# Heading\n\n'
               '![Figure 5: cap](media/img-x.png)\n\n'
               '| A | B |\n|---|---|\n| 1 | 2 |\n\nText with [a link](http://x).\n')
        plain = tu.qmd_to_plain(qmd)
        assert "title:" not in plain          # frontmatter gone
        assert "Figure 5: cap" in plain       # caption kept
        assert "img-x.png" not in plain       # image path gone
        assert "a link" in plain and "http" not in plain
        assert "A" in plain and "1" in plain  # table cells kept

    def test_literal_lt_does_not_swallow_following_prose(self):
        # a literal '<' in prose (e.g. "(< 30%)") must NOT open a phantom HTML tag that
        # eats everything up to the next real '>' far below — that dropped whole prose
        # sections from coverage and produced false "missing sentence" warnings.
        qmd = ("Water bodies (< 30%) are excluded.\n\n"
               "# Results\n\nThe accuracy exceeds the threshold.\n\n"
               '<table>\n<tr><td>cell</td></tr>\n</table>\n')
        plain = tu.qmd_to_plain(qmd)
        assert "the accuracy exceeds the threshold" in plain.lower()
        assert "results" in plain.lower()
        assert "cell" in plain.lower()        # real tag still stripped, cell text kept

    def test_shingles_overlap(self):
        a = tu.shingles(tu.tokens("the quick brown fox jumps"))
        b = tu.shingles(tu.tokens("the quick brown fox"))
        assert b & a  # shared 4-gram


# ── registry / runner ───────────────────────────────────────────────────────────

class TestRegistry:
    def test_all_checks_register(self):
        _load_checks()
        names = {c.name for c in CHECKS}
        assert {"frontmatter", "structural_counts", "figure_placement",
                "text_coverage", "table_coverage"} <= names

    def test_runner_skips_inapplicable_and_aggregates(self, tmp_path):
        ctx = VerifyContext(
            run_dir=tmp_path, original_pdf=tmp_path / "nope.pdf",
            working_pdf=tmp_path / "w.pdf", qmd_path=tmp_path / "d.qmd",
            qmd_text="", detections={"figures": []}, media_dir=tmp_path,
        )
        results = run_verify(ctx)
        assert results  # ran without raising
        assert overall_status(results) in {"ok", "warn", "fail"}


# ── frontmatter check ────────────────────────────────────────────────────────────

class TestFrontmatterCheck:
    def _ctx(self, tmp_path, qmd):
        return VerifyContext(run_dir=tmp_path, original_pdf=tmp_path / "x.pdf",
                             working_pdf=tmp_path / "w.pdf", qmd_path=tmp_path / "d.qmd",
                             qmd_text=qmd, detections={"figures": []}, media_dir=tmp_path)

    def test_ok(self, tmp_path):
        from pdf_to_qmd.verify.checks.frontmatter import FrontmatterCheck
        qmd = '---\ntitle: "T"\nsubtitle: "S"\ncategory: uncategorized\ndate: "2020-01-01"\n---\nBody\n'
        r = FrontmatterCheck().run(self._ctx(tmp_path, qmd))
        assert r.status == "ok"

    def test_missing_and_bad_category(self, tmp_path):
        from pdf_to_qmd.verify.checks.frontmatter import FrontmatterCheck
        qmd = '---\ntitle: "T"\ncategory: bogus\n---\nBody\n'
        r = FrontmatterCheck().run(self._ctx(tmp_path, qmd))
        assert r.status == "fail"
        msgs = " ".join(f.message for f in r.findings)
        assert "subtitle" in msgs and "date" in msgs and "bogus" in msgs


# ── figure_placement check ───────────────────────────────────────────────────────

class TestFigurePlacementCheck:
    def _ctx(self, tmp_path, qmd, figs):
        return VerifyContext(run_dir=tmp_path, original_pdf=tmp_path / "x.pdf",
                             working_pdf=tmp_path / "w.pdf", qmd_path=tmp_path / "d.qmd",
                             qmd_text=qmd, detections={"figures": figs}, media_dir=tmp_path)

    def test_all_placed(self, tmp_path):
        from pdf_to_qmd.verify.checks.figure_placement import FigurePlacementCheck
        figs = [{"fig_id": "FIG_1", "file": "img-a.png", "page": 0, "bbox": [0, 0, 1, 1]}]
        qmd = "![cap](dir-media/img-a.png)\n"
        r = FigurePlacementCheck().run(self._ctx(tmp_path, qmd, figs))
        assert r.status == "ok" and r.metric == 100.0

    def test_unreferenced_and_unresolved(self, tmp_path):
        from pdf_to_qmd.verify.checks.figure_placement import FigurePlacementCheck
        figs = [{"fig_id": "FIG_1", "file": "img-a.png", "page": 0, "bbox": [0, 0, 1, 1]},
                {"fig_id": "FIG_2", "file": "img-b.png", "page": 0, "bbox": [0, 0, 1, 1]}]
        qmd = "![cap](dir-media/img-a.png)\n\n![oops](FIG_9)\n"  # FIG_2 unreferenced, FIG_9 unresolved
        r = FigurePlacementCheck().run(self._ctx(tmp_path, qmd, figs))
        assert r.status == "fail"  # unresolved token
        msgs = " ".join(f.message for f in r.findings)
        assert "FIG_2" in msgs and "FIG_9" in msgs


# ── structural_counts (qmd table counter) ────────────────────────────────────────

class TestStructuralCounts:
    def test_qmd_table_count(self):
        from pdf_to_qmd.verify.checks.structural_counts import _count_qmd_tables
        qmd = "intro\n\n| A | B |\n|---|---|\n| 1 | 2 |\n\nmid\n\n| X |\n|---|\n| y |\n"
        assert _count_qmd_tables(qmd) == 2

    def test_table_count_is_informational_never_warns(self, tmp_path, monkeypatch):
        # find_tables over-segments → many source "tables"; .qmd has none. The
        # table count must NOT drive a warn (table_coverage owns content); the
        # count still appears in the summary for context.
        from pdf_to_qmd.verify.checks import structural_counts as sc
        monkeypatch.setattr(sc, "_count_source_tables", lambda p: 31)
        pdf = tmp_path / "src.pdf"
        pdf.write_bytes(b"%PDF stub")
        ctx = VerifyContext(run_dir=tmp_path, original_pdf=pdf, working_pdf=pdf,
                            qmd_path=tmp_path / "d.qmd",
                            qmd_text="---\ntitle: T\n---\n\nprose, no tables\n",
                            detections={"figures": []}, media_dir=tmp_path)
        r = sc.StructuralCountsCheck().run(ctx)
        assert r.status == "ok"
        # informational wording: source count framed as a rough region count, not a
        # target the .qmd must hit (avoids implying a dropped table)
        assert "see table_coverage" in r.summary
        assert "0 in .qmd" in r.summary and "~31 source region" in r.summary
        assert "0/31" not in r.summary
        assert r.findings == []


# ── table_coverage (qmd grid parse + match) ──────────────────────────────────────

class TestTableCoverage:
    def test_qmd_grids_and_match(self):
        from pdf_to_qmd.verify.checks.table_coverage import _qmd_grids, _best_match
        qmd = "| Name | Value |\n|---|---|\n| OID | unique id |\n| Red | colour |\n"
        grids = _qmd_grids(qmd)
        assert grids and "name" in grids[0] and "unique id" in grids[0]
        src = ["name", "value", "oid", "unique id", "red", "colour"]
        match, score = _best_match(src, grids)
        assert score >= 0.7

    def _ctx(self, tmp_path, qmd):
        pdf = tmp_path / "src.pdf"
        pdf.write_bytes(b"%PDF-1.7 stub")    # exists; _source_grids is monkeypatched
        return VerifyContext(run_dir=tmp_path, original_pdf=pdf, working_pdf=pdf,
                             qmd_path=tmp_path / "d.qmd", qmd_text=qmd,
                             detections={"figures": []}, media_dir=tmp_path)

    def _qmd_with_words(self, words):
        rows = "".join(f"| {w} |\n" for w in words)
        return f"---\ntitle: T\n---\n\n| H |\n|---|\n{rows}"

    def test_weighted_coverage_warns_when_substantial_table_dropped(self, tmp_path, monkeypatch):
        from pdf_to_qmd.verify.checks import table_coverage as tc
        present = [f"word{i}" for i in range(40)]
        absent = [f"absent{i}" for i in range(40)]      # a whole big table missing
        monkeypatch.setattr(tc, "_source_grids", lambda p: [present, absent])
        r = tc.TableCoverageCheck().run(self._ctx(tmp_path, self._qmd_with_words(present)))
        assert r.status == "warn"          # weighted ~50% < 85%
        assert r.metric < 85
        assert any("table 2" in f.location for f in r.findings)

    def test_oversized_table_excluded_from_coverage(self):
        # a 58-col confusion matrix is cropped as a figure → not a transcription target
        from pdf_to_qmd.verify.checks.table_coverage import _is_oversized
        assert _is_oversized([["x"] * 58 for _ in range(59)]) is True
        assert _is_oversized([["a", "b", "c"], ["1", "2", "3"]]) is False   # normal table

    def test_weighted_coverage_ok_when_only_a_fragment_is_missing(self, tmp_path, monkeypatch):
        from pdf_to_qmd.verify.checks import table_coverage as tc
        present = [f"word{i}" for i in range(40)]
        fragment = ["x", "y", "z"]                       # a find_tables sliver (3 tokens)
        monkeypatch.setattr(tc, "_source_grids", lambda p: [present, fragment])
        r = tc.TableCoverageCheck().run(self._ctx(tmp_path, self._qmd_with_words(present)))
        assert r.status == "ok"            # weighted ~93% ≥ 85%; sliver can't trip it
        assert r.findings == []            # fragment filtered out of diagnostics (< _MIN_TOKENS)


# ── text_coverage regression (the headline test) ─────────────────────────────────

class TestTextCoverage:
    def _pdf(self, tmp_path, sentences):
        import fitz
        doc = fitz.open()
        page = doc.new_page(width=595, height=842)
        y = 200
        for s in sentences:
            page.insert_text((72, y), s, fontsize=11)
            y += 20
        p = tmp_path / "src.pdf"
        doc.save(str(p))
        doc.close()
        return p

    def _ctx(self, tmp_path, pdf, qmd):
        return VerifyContext(run_dir=tmp_path, original_pdf=pdf, working_pdf=pdf,
                             qmd_path=tmp_path / "d.qmd", qmd_text=qmd,
                             detections={"figures": []}, media_dir=tmp_path)

    def test_flags_a_dropped_sentence(self, tmp_path):
        from pdf_to_qmd.verify.checks.text_coverage import TextCoverageCheck
        sents = [
            "The quick brown fox jumps over the lazy dog every morning.",
            "First boxes in both rows show the land cover status visible on image.",
            "Change polygons should have a size of at least five hectares.",
        ]
        pdf = self._pdf(tmp_path, sents)
        # qmd contains sentence 1 and 3 but DROPS sentence 2
        qmd = ('---\ntitle: "T"\n---\n\n'
               + sents[0] + "\n\n" + sents[2] + "\n")
        r = TextCoverageCheck().run(self._ctx(tmp_path, pdf, qmd))
        assert r.status == "warn"
        assert r.metric is not None and r.metric < 100
        joined = " ".join(f.message for f in r.findings).lower()
        assert "first boxes" in joined  # the dropped sentence is reported

    def test_full_coverage_when_all_present(self, tmp_path):
        from pdf_to_qmd.verify.checks.text_coverage import TextCoverageCheck
        sents = [
            "The quick brown fox jumps over the lazy dog every morning.",
            "Change polygons should have a size of at least five hectares.",
        ]
        pdf = self._pdf(tmp_path, sents)
        qmd = '---\ntitle: "T"\n---\n\n' + "\n\n".join(sents) + "\n"
        r = TextCoverageCheck().run(self._ctx(tmp_path, pdf, qmd))
        assert r.status == "ok" and r.metric == 100.0


class TestOversizedTables:
    def _ctx(self, tmp_path, qmd, detections):
        pdf = tmp_path / "src.pdf"
        pdf.write_bytes(b"%PDF stub")          # _count_oversized... is monkeypatched
        return VerifyContext(run_dir=tmp_path, original_pdf=pdf, working_pdf=pdf,
                             qmd_path=tmp_path / "d.qmd", qmd_text=qmd,
                             detections=detections, media_dir=tmp_path)

    def test_warns_when_oversized_table_dropped(self, tmp_path, monkeypatch):
        from pdf_to_qmd.verify.checks import oversized_tables as ot
        monkeypatch.setattr(ot, "_count_oversized_source_tables", lambda p: 4)
        r = ot.OversizedTableCheck().run(self._ctx(tmp_path, "prose, no tables", {"figures": []}))
        assert r.status == "warn" and "DROPPED" in r.summary

    def test_ok_when_cropped_as_figures(self, tmp_path, monkeypatch):
        from pdf_to_qmd.verify.checks import oversized_tables as ot
        monkeypatch.setattr(ot, "_count_oversized_source_tables", lambda p: 4)
        dets = {"figures": [{"origin": "oversized-table"} for _ in range(4)]}
        r = ot.OversizedTableCheck().run(self._ctx(tmp_path, "x", dets))
        assert r.status == "ok" and "cropped" in r.summary

    def test_ok_when_no_oversized_source_tables(self, tmp_path, monkeypatch):
        from pdf_to_qmd.verify.checks import oversized_tables as ot
        monkeypatch.setattr(ot, "_count_oversized_source_tables", lambda p: 0)
        r = ot.OversizedTableCheck().run(self._ctx(tmp_path, "x", {"figures": []}))
        assert r.status == "ok"


# ── report writer ────────────────────────────────────────────────────────────────

def test_write_report(tmp_path):
    results = [CheckResult("a", "ok", "fine"), CheckResult("b", "warn", "hmm")]
    p = write_report(results, tmp_path)
    assert p.exists() and (tmp_path / "verify.json").exists()
    data = json.loads((tmp_path / "verify.json").read_text())
    assert data["overall"] == "warn" and len(data["checks"]) == 2


# ── HTML-table awareness (complex tables emitted as raw HTML) ─────────────────

class TestHtmlTableAwareness:
    def test_table_coverage_parses_html_table(self):
        from pdf_to_qmd.verify.checks.table_coverage import _qmd_grids, _best_match
        qmd = ('```{=html}\n<table>\n'
               '<tr><td>Level 1</td><td>Level 2</td></tr>\n'
               '<tr><td>1 Urban</td><td>1.1 Urban fabric</td></tr>\n'
               '</table>\n```\n')
        grids = _qmd_grids(qmd)
        # HTML tables come back as one token-bag per top-level table
        assert grids and "1 urban" in grids[0][0]
        src = ["level 1", "level 2", "1 urban", "1 1 urban fabric"]
        _, score = _best_match(src, grids)
        assert score >= 0.9  # all source tokens present → near-full coverage

    def test_structural_counts_counts_html_table(self):
        from pdf_to_qmd.verify.checks.structural_counts import _count_qmd_tables
        qmd = "intro\n\n```{=html}\n<table><tr><td>a</td></tr></table>\n```\n"
        assert _count_qmd_tables(qmd) == 1

    def test_qmd_to_plain_keeps_html_cell_text(self):
        from pdf_to_qmd.verify.textutil import qmd_to_plain
        qmd = '```{=html}\n<table><tr><td>Continuous urban fabric IMD &lt;30%</td></tr></table>\n```\n'
        plain = qmd_to_plain(qmd)
        assert "Continuous urban fabric" in plain and "<td>" not in plain


# ── Nested HTML tables (the det07 bug) ────────────────────────────────────────

class TestNestedHtmlTables:
    def test_top_level_split_keeps_nested_inside(self):
        from pdf_to_qmd.verify.textutil import top_level_html_tables
        html = ('<table><tr><td>before</td></tr>'
                '<tr><td><table><tr><td>inner</td></tr></table></td></tr>'
                '<tr><td>after nested</td></tr></table>')
        tops = top_level_html_tables(html)
        assert len(tops) == 1                       # ONE top-level table
        assert "inner" in tops[0] and "after nested" in tops[0]  # nested + tail kept

    def test_table_coverage_not_truncated_by_nesting(self):
        from pdf_to_qmd.verify.checks.table_coverage import _qmd_grids, _best_match
        qmd = ('```{=html}\n<table>'
               '<tr><td>Input Data Sources</td></tr>'
               '<tr><td><table><tr><td>Products SPOT-5</td></tr></table></td></tr>'
               '<tr><td>Methodology</td></tr>'
               '<tr><td>Geographic Coverage</td></tr></table>\n```\n')
        grids = _qmd_grids(qmd)
        # "methodology" comes AFTER the nested table — must still be covered
        _, score = _best_match(["input data sources", "products spot 5", "methodology",
                                "geographic coverage"], grids)
        assert score >= 0.9


class TestWideTableLegibilityCheck:
    def _ctx(self, tmp_path, qmd):
        return VerifyContext(run_dir=tmp_path, original_pdf=tmp_path / "x.pdf",
                             working_pdf=tmp_path / "w.pdf", qmd_path=tmp_path / "d.qmd",
                             qmd_text=qmd, detections={"figures": []}, media_dir=tmp_path)

    def test_ok_when_no_small_fonts(self, tmp_path):
        from pdf_to_qmd.verify.checks.wide_table_legibility import WideTableLegibilityCheck
        qmd = '```{=typst}\n#set page(flipped: true, paper: "a3")\n#set text(size: 8pt)\n```\n'
        r = WideTableLegibilityCheck().run(self._ctx(tmp_path, qmd))
        assert r.status == "ok"

    def test_warns_on_6pt_and_5pt(self, tmp_path):
        from pdf_to_qmd.verify.checks.wide_table_legibility import WideTableLegibilityCheck
        qmd = ("```{=typst}\n#set text(size: 6pt)\n```\n"
               "```{=typst}\n#set text(size: 5pt)\n```\n")
        r = WideTableLegibilityCheck().run(self._ctx(tmp_path, qmd))
        assert r.status == "warn"
        assert "6pt" in r.summary and "5pt" in r.summary
        assert r.findings and r.findings[0].severity == "warn"
