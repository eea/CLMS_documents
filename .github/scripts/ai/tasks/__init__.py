"""Task modules for the documentation updater. Each runs its LLM analysis and
caches the results; the main script does the file writes so updates stay atomic."""

from . import generate_intros

__all__ = ["generate_intros"]
