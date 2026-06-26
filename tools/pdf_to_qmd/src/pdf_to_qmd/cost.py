"""Cost accounting helpers for the pdf_to_qmd tool.

OpenRouter reports per-call cost in USD (the ``cost`` field of the response
``usage`` block). The tool surfaces cost in EUR using a pinned conversion rate (no
live FX lookup, no network dependency). The USD figure stays in the logs for
auditability.

The rate comes from the ``PDF2QMD_USD_EUR`` environment variable, falling back to
``DEFAULT_USD_TO_EUR``. Update the env var (or the default) when the rate drifts
materially; it's deliberately a single, obvious knob.
"""

import os

DEFAULT_USD_TO_EUR = 0.92


def usd_to_eur_rate() -> float:
    """The active USD-to-EUR rate (env override, else the pinned default)."""
    raw = os.environ.get("PDF2QMD_USD_EUR", "").strip()
    if raw:
        try:
            return float(raw)
        except ValueError:
            pass
    return DEFAULT_USD_TO_EUR


def eur(usd: float) -> float:
    """Convert a USD amount to EUR using the active rate."""
    return round((usd or 0.0) * usd_to_eur_rate(), 4)


def eur_to_usd(eur_amount: float) -> float:
    """Convert a EUR amount back to USD. Operator-facing budgets are in EUR, the
    pipeline accounts in USD. Returns None for None so 'no limit' passes through."""
    if eur_amount is None:
        return None
    rate = usd_to_eur_rate()
    return (eur_amount / rate) if rate else eur_amount


def fmt_eur(usd: float) -> str:
    """Format a USD amount as a EUR string, e.g. '€1.62'."""
    return f"€{eur(usd):.2f}"


def usage_cost(usage: dict) -> float:
    """USD cost from an OpenRouter ``usage`` block (0.0 if absent)."""
    cost = (usage or {}).get("cost")
    return float(cost) if isinstance(cost, (int, float)) else 0.0
