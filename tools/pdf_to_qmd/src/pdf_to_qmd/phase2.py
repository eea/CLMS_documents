"""Phase 2 (Step 4): convert a Phase-1 run dir's placeholdered PDF.

Consumes the Phase-1 artifacts (*.placeholders.pdf, detections.json, <stem>-media/)
and writes <stem>.qmd with FIG_n tokens resolved. No re-detection.
"""

import json
import logging
from pathlib import Path

from .pass2 import DEFAULT_CATEGORY, convert_placeholdered

log = logging.getLogger(__name__)


def run_phase2(
    run_dir: Path,
    *,
    api_key: str,
    model: str,
    category: str = DEFAULT_CATEGORY,
    default_date: str = None,
    on_delta=None,
    timeout: int = 300,
) -> dict:
    """Convert the placeholdered PDF in a Phase-1 run dir.

    Expects in run_dir: <stem>.placeholders.pdf, detections.json, <stem>-media/.
    Writes <stem>.qmd. Returns a summary dict.
    """
    placeholders = sorted(run_dir.glob("*.placeholders.pdf"))
    if not placeholders:
        raise FileNotFoundError(f"no *.placeholders.pdf in {run_dir} — run Phase 1 first")
    placeholders_pdf = placeholders[0]
    stem = placeholders_pdf.name[: -len(".placeholders.pdf")]

    detections_path = run_dir / "detections.json"
    if not detections_path.exists():
        raise FileNotFoundError(f"no detections.json in {run_dir} — run Phase 1 first")
    sidecar = json.loads(detections_path.read_text(encoding="utf-8"))
    figures = sidecar.get("figures", [])
    cover_block = sidecar.get("cover")
    cover_fields = cover_block.get("fields") if cover_block and cover_block.get("is_cover") else None

    media_dirname = f"{stem}-media"
    out_qmd = run_dir / f"{stem}.qmd"

    result = convert_placeholdered(
        placeholders_pdf,
        figures,
        out_qmd,
        api_key=api_key,
        model=model,
        media_dirname=media_dirname,
        category=category,
        default_date=default_date,
        cover_fields=cover_fields,
        on_delta=on_delta,
        timeout=timeout,
    )

    fig = result["figures"]
    summary = {
        "qmd": out_qmd,
        "figures_total": len(figures),
        "figures_resolved": len(fig["resolved"]),
        "figures_hallucinated": len(fig["hallucinated"]),
        "figures_unreferenced": len(fig["unreferenced"]),
        "media_dirname": media_dirname,
        "cost_usd": result.get("cost_usd", 0.0),
    }
    log.info(
        "Phase 2 done: %d/%d figures placed (%d unknown tokens, %d unreferenced) → %s",
        summary["figures_resolved"], summary["figures_total"],
        summary["figures_hallucinated"], summary["figures_unreferenced"], out_qmd.name,
    )
    return summary
