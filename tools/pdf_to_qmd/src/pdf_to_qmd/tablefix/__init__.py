"""Phase 2.5: deterministic table fixes applied to the converted .qmd before render.

The LLM emits tables that render poorly under Typst: pathological pipe divider widths,
captions placed before their table (Pandoc drops these), and wide HTML tables with no
column-width or orientation control. This phase repairs them, reusing the production
qmd-tools (vendored in `_vendor/`) plus the transforms in `transforms.py`. No LLM,
idempotent.

Order matters; the run order is the sequence in run_phase_tablefix below. The vendored
file-level passes run last, after the atomic write, because they reopen the file.
"""

import logging
import os
from pathlib import Path

from ._vendor import (
    fix_grid_stray_dividers,
    fix_pagebreaks,
    fix_table_colwidths,
    fix_typst_patterns,
    promote_bare_captions as _promote,
)
from .transforms import (
    normalize_table_captions,
    normalize_table_grid,
    orient_wide_tables,
    pipe_captions_to_divs,
    redistribute_stacked_captions,
    stamp_html_colgroups,
    unwrap_pseudo_header_tables,
)

log = logging.getLogger(__name__)


def run_phase_tablefix(qmd_path: Path, *, source_pdf: Path = None, events=None) -> dict:
    """Apply every table fix to `qmd_path` in place. Returns a summary dict.
    A failing transform never raises: table fixing must not abort a conversion.

    `source_pdf` is accepted for backward compatibility but unused (orientation is now
    decided from each table's estimated content width)."""
    summary = {"grid_normalized": 0, "tables_unwrapped": 0, "captions_normalized": 0,
               "captions_moved": 0, "captions_promoted": 0, "captions_redistributed": 0,
               "colgroups_stamped": 0, "tables_oriented": 0, "pagebreaks": 0,
               "typst_escapes": 0, "pipe_colwidths": 0, "stray_dividers": 0}
    try:
        text = qmd_path.read_text(encoding="utf-8")

        text, summary["grid_normalized"] = normalize_table_grid(text)
        text, summary["tables_unwrapped"] = unwrap_pseudo_header_tables(text)
        text, summary["captions_normalized"] = normalize_table_captions(text)
        text, summary["captions_moved"] = pipe_captions_to_divs(text)
        text, summary["captions_promoted"] = _promote.promote_bare_captions(text)
        text, summary["captions_redistributed"] = redistribute_stacked_captions(text)
        text, summary["colgroups_stamped"] = stamp_html_colgroups(text)
        text, summary["tables_oriented"] = orient_wide_tables(text)

        text, summary["pagebreaks"] = fix_pagebreaks.rewrite(text)
        esc = 0
        for fn in (fix_typst_patterns.fix_a1_globs, fix_typst_patterns.fix_a2_var_ext,
                   fix_typst_patterns.fix_b_plone, fix_typst_patterns.fix_d_plusminus):
            text, n = fn(text)
            esc += n
        summary["typst_escapes"] = esc

        # atomic write before the file-level vendored passes pick the file up
        tmp = qmd_path.with_suffix(qmd_path.suffix + ".tmp")
        tmp.write_text(text, encoding="utf-8")
        os.replace(tmp, qmd_path)

        summary["pipe_colwidths"] = fix_table_colwidths.process_file(qmd_path, overwrite=True)
        summary["stray_dividers"] = fix_grid_stray_dividers.normalize(qmd_path)
    except Exception as exc:                # noqa: BLE001 — never abort the conversion
        log.warning("table-fix phase error on %s: %s", qmd_path.name, exc)

    log.info("[Table-fix] grid-norm:%d unwrapped:%d cap-norm:%d captions:%d promoted:%d "
             "cap-redist:%d colgroups:%d oriented:%d pagebreaks:%d escapes:%d pipe-widths:%d stray:%d",
             summary["grid_normalized"], summary["tables_unwrapped"],
             summary["captions_normalized"], summary["captions_moved"],
             summary["captions_promoted"], summary["captions_redistributed"],
             summary["colgroups_stamped"], summary["tables_oriented"], summary["pagebreaks"],
             summary["typst_escapes"], summary["pipe_colwidths"], summary["stray_dividers"])
    if events:
        events.tablefix_done(summary)
    return summary
