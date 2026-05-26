"""Whitelist sanitizer for AI-generated changelog HTML: keeps only <ul>/<li>
(no attributes); every other tag is escaped so it renders as literal text."""

from __future__ import annotations

import html
from html.parser import HTMLParser

_ALLOWED_TAGS = frozenset({"ul", "li"})


class _SafeListParser(HTMLParser):
    """Rebuilds the input keeping only the allowed tags (stripped of attributes);
    every other tag is escaped verbatim. Text content passes through unchanged."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in _ALLOWED_TAGS:
            self._parts.append(f"<{tag}>")
        else:
            raw = self.get_starttag_text() or f"<{tag}>"
            self._parts.append(html.escape(raw))

    def handle_endtag(self, tag):
        if tag in _ALLOWED_TAGS:
            self._parts.append(f"</{tag}>")
        else:
            self._parts.append(html.escape(f"</{tag}>"))

    def handle_startendtag(self, tag, attrs):
        raw = self.get_starttag_text() or f"<{tag}/>"
        self._parts.append(html.escape(raw))

    def handle_data(self, data):
        self._parts.append(data)

    def get_output(self) -> str:
        return "".join(self._parts)


def sanitize_changelog_html(text: str) -> str:
    """Return text with only <ul>/<li> tags kept. Falsy input passes through."""
    if not text:
        return text
    parser = _SafeListParser()
    parser.feed(text)
    parser.close()
    return parser.get_output()
