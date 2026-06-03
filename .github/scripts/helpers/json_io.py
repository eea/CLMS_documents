"""Tolerant JSON loading: returns {} for a missing or unparseable file."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Union


def load_json_or_empty(
    path: Union[str, Path], *, label: str = "JSON file"
) -> dict:
    """Load JSON from path. A missing file is silent; a parse error prints
    "[WARNING] Could not load {label}: ..." so the caller can say what failed."""
    p = Path(path)
    if not p.exists():
        return {}
    try:
        with p.open("r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"[WARNING] Could not load {label}: {e}")
        return {}
