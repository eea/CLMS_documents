#!/usr/bin/env python3
"""Tests for the Phase 2.5 table-fix transforms."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from pdf_to_qmd.tablefix import run_phase_tablefix  # noqa: E402
from pdf_to_qmd.tablefix.transforms import (  # noqa: E402
    html_table_consistency, normalize_table_grid, orient_wide_tables,
    pipe_captions_to_divs, stamp_html_colgroups,
)


# ── Grid normalization: html_table_consistency ────────────────────────────────

class TestHtmlTableConsistency:
    def test_header_wider_than_data_flagged(self):
        # Table-10 v1 pattern: header colspan 25, data rows 16
        t = ('<table><thead><tr><td rowspan="4"></td>'
             '<td colspan="12">Blind</td><td colspan="12">Plausibility</td></tr></thead>'
             '<tbody>' + ('<tr>' + '<td>x</td>' * 16 + '</tr>') * 4 + '</tbody></table>')
        info = html_table_consistency(t)
        assert info["max_header_width"] == 25 and info["data_width"] == 16
        assert not info["consistent"]

    def test_header_narrower_than_data_flagged(self):
        t = ('<table><thead><tr><td colspan="6">Blind</td><td colspan="7">Plausibility</td>'
             '</tr></thead><tbody>' + ('<tr>' + '<td>x</td>' * 15 + '</tr>') * 3
             + '</tbody></table>')
        info = html_table_consistency(t)
        assert info["max_header_width"] == 13 and info["data_width"] == 15
        assert not info["consistent"]

    def test_consistent_table(self):
        t = ('<table><thead><tr>' + '<th>H</th>' * 4 + '</tr></thead>'
             '<tbody>' + ('<tr>' + '<td>v</td>' * 4 + '</tr>') * 3 + '</tbody></table>')
        assert html_table_consistency(t)["consistent"]

    def test_rowspan_table_not_flagged(self):
        # non-uniform data rows (rowspan) → left alone
        t = ('<table><thead><tr>' + '<th>H</th>' * 4 + '</tr></thead><tbody>'
             '<tr><td rowspan="2">m</td><td>a</td><td>b</td><td>c</td></tr>'
             '<tr><td>a</td><td>b</td><td>c</td></tr></tbody></table>')
        assert html_table_consistency(t)["consistent"]   # uniform_data is False


class TestNormalizeTableGrid:
    def _broken_symmetric(self):
        """Two mirror halves (Blind|Plausibility), header 25 wide, data 16 wide."""
        leaf = ("<tr><td>n</td><td>Overall</td><td>95% CI</td><td></td>"
                "<td>Overall</td><td>95% CI</td><td></td>"
                "<td>Overall</td><td>95% CI</td><td></td>") * 2
        thead = ('<thead><tr><td rowspan="3"></td><td colspan="12">Blind</td>'
                 '<td colspan="12">Plausibility</td></tr>'
                 '<tr>' + '<td colspan="4">Y</td>' * 6 + '</tr>'
                 + '<tr>' + leaf + '</tr></thead>')
        row = ("<tr><td>EEA39</td><td>21,000</td><td>68.82%</td><td>0.40%</td>"
               "<td>88.75%</td><td>0.26%</td><td>67.41%</td><td>0.40%</td>"
               "<td>EEA39</td><td>21,000</td><td>87.86%</td><td>0.23%</td>"
               "<td>91.51%</td><td>0.22%</td><td>86.15%</td><td>0.26%</td></tr>")
        return (f"```{{=html}}\n<table>{thead}<tbody>{row * 3}</tbody></table>\n```\n")

    def test_fixes_broken_grid_keeping_values(self):
        out, n = normalize_table_grid(self._broken_symmetric())
        assert n == 1
        # now consistent
        import re
        from pdf_to_qmd.verify.textutil import top_level_html_tables
        tbl = top_level_html_tables(re.search(r"```\{=html\}\n(.*?)\n```", out, re.DOTALL).group(1))[0]
        assert html_table_consistency(tbl)["consistent"]
        # every value preserved verbatim
        for v in ["86.15%", "91.51%", "21,000", "68.82%", "EEA39"]:
            assert v in out
        # symmetric → two-group header rebuilt
        assert ">Blind<" in out and ">Plausibility<" in out

    def test_consistent_table_untouched(self):
        good = ("```{=html}\n<table><thead><tr><th>A</th><th>B</th></tr></thead>"
                "<tbody><tr><td>1</td><td>2</td></tr></tbody></table>\n```\n")
        out, n = normalize_table_grid(good)
        assert n == 0 and out == good

    def test_idempotent(self):
        once, n1 = normalize_table_grid(self._broken_symmetric())
        twice, n2 = normalize_table_grid(once)
        assert n1 == 1 and n2 == 0 and once == twice

    def test_nested_table_skipped(self):
        # a fence with a nested table is not safely rebuildable → left alone
        nested = ("```{=html}\n<table><thead><tr><td colspan=\"5\">H</td></tr></thead>"
                  "<tbody><tr><td>a</td><td><table><tr><td>x</td></tr></table></td></tr>"
                  "</tbody></table>\n```\n")
        out, n = normalize_table_grid(nested)
        assert n == 0


def _html_table(ncols, *, nested=False, colgroup=False):
    cg = "<colgroup>\n<col>\n<col>\n</colgroup>\n" if colgroup else ""
    nest = "<table><tr><td>inner</td></tr></table>" if nested else "wordwordword"
    row = "".join(f"<td>{nest if c == 0 else 'c'+str(c)}</td>" for c in range(ncols))
    return f"```{{=html}}\n<table>\n{cg}<tr>{row}</tr>\n</table>\n```"


def _wide_html(ncols, wlen):
    """An HTML table whose every cell is one `wlen`-char word → estimated min width
    ≈ ncols*(wlen+1), so tests can target a page tier precisely."""
    word = "x" * wlen
    row = "".join(f"<td>{word}</td>" for _ in range(ncols))
    return f"```{{=html}}\n<table>\n<tr>{row}</tr>\n<tr>{row}</tr>\n</table>\n```"


class TestRedistributeStackedCaptions:
    def _div(self, cap):
        return ("::: {.tbl-caption}\n```{=typst}\n#set text(size: 9pt, fill: rgb(\"#3E6893\"))\n```\n"
                f"{cap}\n:::")

    def test_two_stacked_divs_over_two_tables_redistributed(self):
        from pdf_to_qmd.tablefix.transforms import redistribute_stacked_captions
        qmd = (self._div("Table 4: sample units") + "\n\n"
               + self._div("Table 5: weight factors") + "\n\n"
               "| A | B |\n| 1 | 2 |\n\n"
               "| C | D |\n| 3 | 4 |\n")
        out, n = redistribute_stacked_captions(qmd)
        assert n == 1
        # Table 4 now pairs with the first table, Table 5 with the second
        i4 = out.index("Table 4: sample units")
        i5 = out.index("Table 5: weight factors")
        ia = out.index("| A | B |")
        ic = out.index("| C | D |")
        assert i4 < ia < i5 < ic                        # interleaved caption/table/caption/table
        # idempotent
        again, n2 = redistribute_stacked_captions(out)
        assert n2 == 0 and again == out

    def test_two_divs_one_table_left_alone(self):
        # a genuinely missing table (2 captions, 1 table) must NOT be redistributed
        from pdf_to_qmd.tablefix.transforms import redistribute_stacked_captions
        qmd = (self._div("Table 4: x") + "\n\n" + self._div("Table 5: y") + "\n\n"
               "| A | B |\n| 1 | 2 |\n")
        out, n = redistribute_stacked_captions(qmd)
        assert n == 0 and out == qmd

    def test_single_caption_untouched(self):
        from pdf_to_qmd.tablefix.transforms import redistribute_stacked_captions
        qmd = self._div("Table 4: x") + "\n\n| A | B |\n| 1 | 2 |\n"
        out, n = redistribute_stacked_captions(qmd)
        assert n == 0 and out == qmd


class TestExtremeWidthTiers:
    def test_decide_tiers(self):
        from pdf_to_qmd.tablefix.transforms import _decide
        assert _decide(70) is None           # portrait
        assert _decide(100) == "A4-land"     # 9pt
        assert _decide(120) == "A3-land"     # 8pt
        assert _decide(137) == "A3-xl"       # 6pt — the 25-col confusion matrix
        assert _decide(200) == "A3-xxl"      # 5pt floor

    def test_8pt_table_not_regressed_to_smaller(self):
        # a 116-char table (renders fine at 8pt today) must STAY at 8pt, not shrink
        from pdf_to_qmd.tablefix.transforms import _decide
        assert _decide(116) == "A3-land"

    def test_xl_wrap_emits_6pt(self):
        from pdf_to_qmd.tablefix.transforms import _PAGE_RULES
        assert "size: 6pt" in _PAGE_RULES["A3-xl"]
        assert "size: 5pt" in _PAGE_RULES["A3-xxl"]
        assert 'paper: "a3"' in _PAGE_RULES["A3-xl"]


class TestUnwrapPseudoHeaderTables:
    def test_unwraps_one_col_title_wrapper(self):
        from pdf_to_qmd.tablefix.transforms import unwrap_pseudo_header_tables
        qmd = ("| Riparian Zones Delivery Units |\n"
               "| :---------------------------- |\n"
               "| **Table 2: RZ LCLU Delivery Units (DUs)** |\n"
               "| No. | DU ID | Name |\n"
               "| 1 | DU001A | Aegean |\n"
               "| 2 | DU002A | Attica |\n")
        out, n = unwrap_pseudo_header_tables(qmd)
        assert n == 1
        lines = [ln for ln in out.split("\n") if ln.strip()]
        assert lines[0] == "::: {.tbl-caption}"                 # caption extracted
        assert "Table 2: RZ LCLU Delivery Units (DUs)" in out
        assert "Riparian Zones Delivery Units" not in out        # bogus title dropped
        assert "| No. | DU ID | Name |" in out                  # real header kept
        assert "| --- | --- | --- |" in out                     # divider inserted (3 cols)
        assert "| 1 | DU001A | Aegean |" in out
        # idempotent
        again, n2 = unwrap_pseudo_header_tables(out)
        assert n2 == 0 and again == out

    def test_unwraps_without_caption_row(self):
        from pdf_to_qmd.tablefix.transforms import unwrap_pseudo_header_tables
        qmd = ("| Some Title |\n| :--- |\n"
               "| A | B |\n| 1 | 2 |\n")
        out, n = unwrap_pseudo_header_tables(qmd)
        assert n == 1
        assert "tbl-caption" not in out                          # no Table N: row → no caption
        assert "Some Title" not in out
        assert "| A | B |" in out and "| --- | --- |" in out

    def test_legit_one_column_table_untouched(self):
        from pdf_to_qmd.tablefix.transforms import unwrap_pseudo_header_tables
        # every row is genuinely 1 column → must NOT be unwrapped
        qmd = "| Heading |\n| :--- |\n| value one |\n| value two |\n"
        out, n = unwrap_pseudo_header_tables(qmd)
        assert n == 0 and out == qmd

    def test_normal_multicolumn_table_untouched(self):
        from pdf_to_qmd.tablefix.transforms import unwrap_pseudo_header_tables
        qmd = "| A | B |\n| --- | --- |\n| 1 | 2 |\n"
        out, n = unwrap_pseudo_header_tables(qmd)
        assert n == 0 and out == qmd


class TestNormalizeTableCaptions:
    def test_migrates_crossref_div_to_tbl_caption(self):
        from pdf_to_qmd.tablefix.transforms import normalize_table_captions
        qmd = ("::: {#tbl-x}\n\n```{=html}\n<table><tr><td>a</td></tr></table>\n```\n\n"
               "Table 1: A caption\n\n:::\n")
        out, n = normalize_table_captions(qmd)
        assert n == 1
        assert "#tbl-" not in out                         # no crossref → no auto-numbering
        assert out.lstrip().startswith("::: {.tbl-caption}")
        assert "Table 1: A caption" in out
        assert "<table>" in out                            # the html table survives

    def test_nested_caption_div_preserved(self):
        # a crossref div that already contains a lifted `.tbl-caption` (a second table)
        # must keep that nested caption AND migrate the outer one — depth-aware scan.
        from pdf_to_qmd.tablefix.transforms import normalize_table_captions
        qmd = ("::: {#tbl-y}\n\n::: {.tbl-caption}\nInner cap\n:::\n\n"
               "```{=html}\n<table><tr><td>a</td></tr></table>\n```\n\n"
               "Outer cap\n\n:::\n")
        out, n = normalize_table_captions(qmd)
        assert n == 1 and "#tbl-" not in out
        assert "Inner cap" in out and "Outer cap" in out   # both captions kept
        # idempotent
        again, n2 = normalize_table_captions(out)
        assert n2 == 0 and again == out

    def test_no_html_table_left_untouched(self):
        from pdf_to_qmd.tablefix.transforms import normalize_table_captions
        qmd = "::: {#tbl-z}\n\nJust prose, no table.\n\n:::\n"
        out, n = normalize_table_captions(qmd)
        assert n == 0 and out == qmd


class TestPipeCaptionsToDivs:
    def test_caption_after_table_becomes_div_above(self):
        qmd = "| A | B |\n|---|---|\n| 1 | 2 |\n\n: Table 2: Caption\n"
        out, n = pipe_captions_to_divs(qmd)
        assert n == 1
        lines = out.split("\n")
        assert lines[0] == "::: {.tbl-caption}"        # div now leads, above the table
        assert "Table 2: Caption" in out
        assert ": Table 2: Caption" not in out          # the pipe-caption line is gone
        assert "#set text" in out                       # embedded raw-typst styling
        # the table still follows the div
        assert any(ln.startswith("| A") for ln in lines)

    def test_caption_before_table_becomes_div_above(self):
        qmd = ": Table 2: Caption\n\n| A | B |\n|---|---|\n| 1 | 2 |\n"
        out, n = pipe_captions_to_divs(qmd)
        assert n == 1
        lines = out.split("\n")
        assert lines[0] == "::: {.tbl-caption}"
        assert ": Table 2: Caption" not in out
        # table preserved after the div
        assert "| A | B |" in out and "| 1 | 2 |" in out

    def test_idempotent(self):
        qmd = "| A | B |\n|---|---|\n| 1 | 2 |\n\n: Table 2: Caption\n"
        once, n1 = pipe_captions_to_divs(qmd)
        twice, n2 = pipe_captions_to_divs(once)
        assert n1 == 1 and n2 == 0 and once == twice

    def test_non_table_definition_line_left_untouched(self):
        # a ': ' line not adjacent to a pipe table must NOT be converted
        qmd = "Some prose.\n\n: not a table caption\n\nMore prose.\n"
        out, n = pipe_captions_to_divs(qmd)
        assert n == 0 and out == qmd

    def test_ensure_blank_after_caption_is_idempotent(self):
        from pdf_to_qmd.tablefix.transforms import _ensure_blank_after_captions
        qmd = ": A caption\n\nsome prose\n"
        once = _ensure_blank_after_captions(qmd)
        assert _ensure_blank_after_captions(once) == once

    def test_attribute_only_caption_emits_no_orphan_div(self):
        # A caption that is just a tbl-colwidths attribute (no visible text) must
        # NOT become a `.tbl-caption` div whose body is a bare `{...}` line —
        # Pandoc binds that to the typst fence and flips Quarto to the jupyter
        # engine, crashing the build. The colwidths already live in the divider.
        qmd = '| A | B |\n|---|---|\n| 1 | 2 |\n\n: {tbl-colwidths="[30,70]"}\n'
        out, _ = pipe_captions_to_divs(qmd)
        assert ".tbl-caption" not in out         # no styling div emitted
        assert "tbl-colwidths" not in out         # the attribute line is dropped, not orphaned
        assert "| A | B |" in out                 # table preserved


class TestColgroup:
    def test_stamps_when_missing(self):
        out, n = stamp_html_colgroups(_html_table(3))
        assert n == 1 and "<colgroup>" in out and out.count("<col ") == 3

    def test_skips_when_present(self):
        out, n = stamp_html_colgroups(_html_table(3, colgroup=True))
        assert n == 0

    def test_skips_nested_tables(self):
        out, n = stamp_html_colgroups(_html_table(3, nested=True))
        assert n == 0          # nested column model too ambiguous to size

    def test_colgroup_floors_long_token_column(self):
        import re

        from pdf_to_qmd.tablefix.transforms import _colgroup_for
        # col0 has a long word, col1 a single char → col0 must get more width
        cg = _colgroup_for(2, {0: 12, 1: 1}, {0: 12, 1: 1})
        widths = [float(x) for x in re.findall(r"width: ([\d.]+)%", cg)]
        assert widths[0] > widths[1]
        assert abs(sum(widths) - 100) < 0.5

    def test_label_column_not_starved_by_long_description(self):
        import re

        from pdf_to_qmd.tablefix.transforms import _colgroup_for
        # col0: a 11-char label word; col1: a long wrapping description (200 chars)
        cg = _colgroup_for(2, {0: 11, 1: 200}, {0: 11, 1: 9})
        widths = [float(x) for x in re.findall(r"width: ([\d.]+)%", cg)]
        assert widths[0] >= 8          # keeps room for "VALIDATION"-length words

    def test_long_content_column_does_not_starve_short_columns(self):
        import re

        from pdf_to_qmd.tablefix.transforms import _colgroup_for
        # one huge-content column (Catchment-like) must not crush short-token columns
        # (DU-ID / SC01-02-like) below a usable share — the content cap prevents it.
        cg = _colgroup_for(3, {0: 200, 1: 7, 2: 7}, {0: 12, 1: 7, 2: 7})
        widths = [float(x) for x in re.findall(r"width: ([\d.]+)%", cg)]
        assert widths[1] >= 15 and widths[2] >= 15


class TestPageDecision:
    def test_decide_thresholds(self):
        from pdf_to_qmd.tablefix.transforms import _decide
        assert _decide(50) is None          # fits A4-portrait
        assert _decide(95) == "A4-land"     # needs A4-landscape
        assert _decide(120) == "A3-land"    # needs A3-landscape (8pt)

    def test_min_width_pipe_uses_longest_token_not_header_text(self):
        # a numeric column with a long ONE-LINE header but short values must be sized
        # by the longest word (the header wraps), so the table stays narrow.
        from pdf_to_qmd.tablefix.transforms import _pipe_col_tokens
        block = ["| code | Number of Sample Units SC01-02 |",
                 "| 1110 | 1,416 |"]
        toks = _pipe_col_tokens(block, 2)
        assert toks == [4, 7]               # "1110"=4, "SC01-02"=7 (not the 30-char header)


class TestOrient:
    def test_a3_for_very_wide_table(self):
        out, n = orient_wide_tables(_wide_html(11, 10))     # ~121 chars → A3-landscape 8pt
        assert n == 1 and 'paper: "a3"' in out and "#set text(size: 8pt)" in out

    def test_a3_xl_font_shrink_for_extreme_width(self):
        out, n = orient_wide_tables(_wide_html(14, 10))     # ~154 chars → A3-landscape 6pt
        assert n == 1 and 'paper: "a3"' in out and "#set text(size: 6pt)" in out

    def test_a4_landscape_for_moderately_wide_table(self):
        out, n = orient_wide_tables(_wide_html(8, 11))      # ~96 chars → A4-landscape
        assert n == 1
        assert "#set page(flipped: true)" in out and 'paper: "a3"' not in out

    def test_narrow_table_untouched(self):
        out, n = orient_wide_tables(_wide_html(4, 6))       # ~28 chars → A4-portrait
        assert n == 0 and "flipped" not in out

    def test_few_columns_but_wide_still_escalates(self):
        # 3 columns, each a very long word → wide table must escalate despite few cols
        out, n = orient_wide_tables(_wide_html(3, 40))      # ~123 chars → A3-landscape
        assert n == 1 and 'paper: "a3"' in out

    def test_wide_pipe_table_wrapped(self):
        cells = " | ".join("x" * 10 for _ in range(10))     # ~110 chars
        qmd = f"| {cells} |\n|{'|'.join(['---'] * 10)}|\n| {cells} |\n"
        out, n = orient_wide_tables(qmd)
        assert n == 1 and "#set page(flipped: true)" in out

    def test_idempotent(self):
        once, _ = orient_wide_tables(_wide_html(12, 10))
        twice, n = orient_wide_tables(once)
        assert n == 0 and twice == once


class TestRunPhase:
    def test_end_to_end_updates_file_and_summary(self, tmp_path):
        qmd = tmp_path / "doc.qmd"
        qmd.write_text(
            "---\ntitle: T\n---\n\n"
            ": Table 1: cap\n\n| A | B |\n|---|---|\n| 1 | 2 |\n\n"
            + _wide_html(12, 10) + "\n",
            encoding="utf-8")
        summary = run_phase_tablefix(qmd)
        assert summary["captions_moved"] == 1
        assert summary["colgroups_stamped"] == 1
        assert summary["tables_oriented"] == 1
        text = qmd.read_text(encoding="utf-8")
        assert 'paper: "a3"' in text and "<colgroup>" in text
        # idempotent: a second pass changes nothing material
        s2 = run_phase_tablefix(qmd)
        assert s2["tables_oriented"] == 0 and s2["colgroups_stamped"] == 0


class TestDateColumnWidth:
    """A '/'-joined date must be treated as one unbreakable token so its column is
    sized for the whole date (else "14/05/2008" overflows into the next column)."""

    def test_slash_date_is_one_token(self):
        from pdf_to_qmd.tablefix._vendor import fix_table_colwidths as F
        assert F.longest_token("14/05/2008") == 10
        assert F.longest_token("08/05/2008") == 10

    def test_date_column_gets_enough_width(self):
        from pdf_to_qmd.tablefix._vendor import fix_table_colwidths as F
        header = ["", "Name", "Issue", "Date", "Reference"]
        data = [["RD[1]", "C5-Service Validation Protocol", "1.00",
                 "14/05/2008", "RD-0421-RP-0003-C5"]]
        pcts = F.compute_pcts(header, data)
        date_pct = pcts[3]
        # 10-char date needs ~10/70 ≈ 14% minimum; previously it got ~10% and clipped
        assert date_pct >= 14, f"date column too narrow: {date_pct}%"
