"""Prompt loading: parse the ## Section format used by CLMS prompt templates and
fill placeholders."""

import logging
import re
import sys
from pathlib import Path

log = logging.getLogger(__name__)


def parse_prompt_file(prompt_path: Path) -> tuple:
    """Extract (system_instruction, user_prompt) from a prompt template file."""
    if not prompt_path.exists():
        log.error("Prompt file not found: %s", prompt_path)
        sys.exit(1)

    text = prompt_path.read_text(encoding="utf-8")

    def _extract(heading: str) -> str:
        # legacy (conversion prompt): fenced block right after the heading. `\s*`
        # absorbs only whitespace, so an inline ``` later in prose can't match.
        fenced = re.compile(
            re.escape(heading) + r"\s*```(?:\w*\n)?(.*?)```",
            re.DOTALL | re.IGNORECASE,
        )
        m = fenced.search(text)
        if m and m.group(1).strip():
            return m.group(1).strip()

        # new (detection prompt): plain markdown from the heading to the next `## `
        delim = re.compile(
            re.escape(heading) + r"[ \t]*\r?\n(.*?)(?=\r?\n##\s|\Z)",
            re.DOTALL | re.IGNORECASE,
        )
        m = delim.search(text)
        if m and m.group(1).strip():
            return m.group(1).strip()

        raise ValueError(
            f"Could not extract the '{heading}' section from {prompt_path}"
        )

    system_instruction = _extract("## System Instruction")
    user_prompt = _extract("## User Prompt")
    return system_instruction, user_prompt


def build_user_prompt(user_prompt_template: str, filename: str) -> str:
    return user_prompt_template.replace("{{FILENAME}}", filename)
