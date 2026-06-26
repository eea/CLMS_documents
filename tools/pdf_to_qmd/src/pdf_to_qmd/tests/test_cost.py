#!/usr/bin/env python3
"""Tests for cost.py (USD→EUR conversion + usage extraction)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from pdf_to_qmd import cost  # noqa: E402


class TestEur:
    def test_default_rate(self, monkeypatch):
        monkeypatch.delenv("PDF2QMD_USD_EUR", raising=False)
        assert cost.usd_to_eur_rate() == cost.DEFAULT_USD_TO_EUR
        assert cost.eur(1.0) == round(cost.DEFAULT_USD_TO_EUR, 4)

    def test_env_override(self, monkeypatch):
        monkeypatch.setenv("PDF2QMD_USD_EUR", "0.8")
        assert cost.usd_to_eur_rate() == 0.8
        assert cost.eur(10.0) == 8.0
        assert cost.fmt_eur(10.0) == "€8.00"

    def test_bad_env_falls_back(self, monkeypatch):
        monkeypatch.setenv("PDF2QMD_USD_EUR", "not-a-number")
        assert cost.usd_to_eur_rate() == cost.DEFAULT_USD_TO_EUR

    def test_eur_handles_none_zero(self):
        assert cost.eur(0.0) == 0.0
        assert cost.eur(None) == 0.0


class TestUsageCost:
    def test_extracts_cost(self):
        assert cost.usage_cost({"cost": 0.1334}) == 0.1334

    def test_missing_or_bad_returns_zero(self):
        assert cost.usage_cost({}) == 0.0
        assert cost.usage_cost(None) == 0.0
        assert cost.usage_cost({"cost": "nope"}) == 0.0


class TestCallReturnsUsage:
    """call_vision/call_openrouter expose usage when return_usage=True."""

    def test_call_vision_returns_usage_tuple(self, monkeypatch):
        from pdf_to_qmd import llm_client
        monkeypatch.setattr(llm_client, "_post_with_retries",
                            lambda **kw: ("json text", {"cost": 0.05, "total_tokens": 100}))
        text, usage = llm_client.call_vision(
            api_key="k", model="m", system_instruction="s", user_prompt="u",
            image_data_uris=["data:image/png;base64,x"], return_usage=True)
        assert text == "json text" and usage["cost"] == 0.05

    def test_call_vision_text_only_by_default(self, monkeypatch):
        from pdf_to_qmd import llm_client
        monkeypatch.setattr(llm_client, "_post_with_retries",
                            lambda **kw: ("just text", {"cost": 0.05}))
        result = llm_client.call_vision(
            api_key="k", model="m", system_instruction="s", user_prompt="u",
            image_data_uris=["data:image/png;base64,x"])
        assert result == "just text"   # no tuple
