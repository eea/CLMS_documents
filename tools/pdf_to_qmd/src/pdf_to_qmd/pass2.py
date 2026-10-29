"""Pass-2 conversion (Step 4).

Sends the chrome-stripped, placeholder-injected PDF to the LLM, then resolves the
FIG_n tokens to the cropped Phase-1 figures and normalizes the frontmatter. No figure
detection here — Steps 0-3 already cropped them and stamped [FIG_n] boxes; this pass
just transcribes and references each figure by its token.
"""

import base64
import logging
import os
from pathlib import Path

from .llm_client import call_openrouter
from .prompt import build_user_prompt, parse_prompt_file
from .resolve import (
    close_unbalanced_fences,
    drop_empty_table_rows,
    fix_invalid_entities,
    fold_figure_captions,
    lift_html_table_captions,
    neutralize_body_thematic_breaks,
    neutralize_header_center,
    normalize_frontmatter,
    resolve_fig_tokens,
    sanitize_zero_borders,
    strip_wrapping_fence,
)

log = logging.getLogger(__name__)

DEFAULT_CONVERT_PROMPT = (
    Path(__file__).resolve().parent / "prompt_templates" / "convert_prompt.md"
)
DEFAULT_CATEGORY = "uncategorized"


def convert_placeholdered(
    placeholders_pdf: Path,
    figures: list,
    out_qmd: Path,
    *,
    api_key: str,
    model: str,
    media_dirname: str,
    prompt_file: Path = DEFAULT_CONVERT_PROMPT,
    category: str = DEFAULT_CATEGORY,
    default_date: str = None,
    cover_fields: dict = None,
    on_delta=None,
    timeout: int = 300,
) -> dict:
    """Convert a placeholdered PDF to .qmd and resolve its FIG_n tokens.

    Writes out_qmd, returns {"qmd": Path, "figures": {...}, "cost_usd": float}. With
    `on_delta` set the convert call streams; the resolved .qmd is identical either way.
    """
    system_instruction, user_template = parse_prompt_file(prompt_file)
    user_prompt = build_user_prompt(user_template, placeholders_pdf.name)

    # working PDF is small (chrome stripped), so inline base64 is fine
    b64 = base64.b64encode(placeholders_pdf.read_bytes()).decode("ascii")
    file_data = "data:application/pdf;base64," + b64

    log.info("[Pass 2] Converting %s → .qmd …", placeholders_pdf.name)
    raw, usage = call_openrouter(
        api_key=api_key,
        model=model,
        engine="native",
        system_instruction=system_instruction,
        user_prompt=user_prompt,
        file_data=file_data,
        filename=placeholders_pdf.name,
        timeout=timeout,
        return_usage=True,
        stream=on_delta is not None,
        on_delta=on_delta,
    )

    text = strip_wrapping_fence(raw)
    text, fence_closed = close_unbalanced_fences(text)
    if fence_closed:
        log.warning("[Pass 2] Converter left a fenced block unterminated — appended a closing ``` "
                    "(an unclosed ```{=html} table renders as plain text)")
    text, fig_report = resolve_fig_tokens(text, figures, out_qmd, media_dirname)
    text, n_folded = fold_figure_captions(text)
    if n_folded:
        log.info("[Pass 2] Folded %d stray 'Figure N:' caption line(s) back into the "
                 "image alt (else they render as body text, not a figure caption)", n_folded)
    text, n_empty_rows = drop_empty_table_rows(text)
    if n_empty_rows:
        log.info("[Pass 2] Dropped %d cell-less <tr> row(s) (would compile to invalid Typst)", n_empty_rows)
    text, n_entities = fix_invalid_entities(text)
    if n_entities:
        log.info("[Pass 2] Replaced %d invalid HTML entity(ies) with Unicode (e.g. &sqrt; → √)", n_entities)
    text, n_borders = sanitize_zero_borders(text)
    if n_borders:
        log.info("[Pass 2] Stripped %d zero/none border declaration(s) from HTML styles", n_borders)
    text, n_hdr = neutralize_header_center(text)
    if n_hdr:
        log.info("[Pass 2] Removed text-align:center from %d table header row(s) "
                 "(template centers row 0; inline center would center every body cell)", n_hdr)
    text, n_caps = lift_html_table_captions(text)
    if n_caps:
        log.info("[Pass 2] Lifted %d HTML <caption> into a table-figure div "
                 "(Quarto drops <caption>; the div renders it as a styled caption above the table)", n_caps)
    text, n_hr = neutralize_body_thematic_breaks(text)
    if n_hr:
        log.info("[Pass 2] Converted %d body '---' rule(s) to '***' "
                 "(a body '---…---' block is misread by Quarto as a YAML metadata block)", n_hr)
    text = normalize_frontmatter(text, category, default_date, cover_fields=cover_fields)

    out_qmd.parent.mkdir(parents=True, exist_ok=True)
    # atomic write: resume keys off the .qmd's existence, so a Ctrl-C mid-write must
    # not leave a truncated file that reads as "already done"
    tmp = out_qmd.with_suffix(out_qmd.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, out_qmd)
    log.info("[Pass 2] Wrote %s", out_qmd.name)

    from .cost import usage_cost
    return {"qmd": out_qmd, "figures": fig_report, "cost_usd": usage_cost(usage)}
