"""Regression test for the streaming SSE UTF-8 decode (Phase 2).

`requests` defaults `text/event-stream` to Latin-1 (RFC 2616), which mangles
UTF-8 (curly quotes, →, em-dash, °, accents). `_consume_sse` must force UTF-8 so
streamed content round-trips byte-identical — including a multibyte char split
across two network chunks.
"""

import codecs
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent))

from pdf_to_qmd.llm_client import _consume_sse  # noqa: E402


class _FakeResp:
    """Mimics requests.Response.iter_lines: defaults to Latin-1 for
    event-stream (encoding=None), decodes incrementally so a multibyte char
    split across byte chunks is reassembled by the decoder."""

    def __init__(self, byte_chunks, encoding=None):
        self._chunks = byte_chunks
        self.encoding = encoding   # None → requests would use ISO-8859-1

    def iter_lines(self, decode_unicode=False):
        enc = self.encoding or "ISO-8859-1"
        dec = codecs.getincrementaldecoder(enc)("replace")
        buf = ""
        for chunk in self._chunks:
            buf += dec.decode(chunk)
            while "\n" in buf:
                line, buf = buf.split("\n", 1)
                yield line
        buf += dec.decode(b"", final=True)
        if buf:
            yield buf


def _sse_bytes(content: str) -> bytes:
    payload = {"choices": [{"delta": {"content": content}}]}
    return ("data: " + json.dumps(payload, ensure_ascii=False) + "\n\n").encode("utf-8")


def _chunk(data: bytes, size: int) -> list:
    return [data[i:i + size] for i in range(0, len(data), size)]


def test_streamed_unicode_roundtrips_byte_identical():
    content = "“Urban Atlas” → class 1.4 — °C ² café"
    # tiny chunks guarantee multibyte sequences (E2 80 9C, E2 86 92, …) get split
    chunks = _chunk(_sse_bytes(content) + b"data: [DONE]\n\n", 5)
    resp = _FakeResp(chunks, encoding=None)   # event-stream default (would be Latin-1)

    text, usage, finish = _consume_sse(resp, None)

    assert text == content, f"mojibake! got {text!r}"
    assert "â" not in text
    assert "→" in text and "“" in text and "—" in text


def test_on_delta_receives_clean_text():
    content = "Holiday villages (“Club Med”) → class 1.4.2."
    chunks = _chunk(_sse_bytes(content) + b"data: [DONE]\n\n", 4)
    resp = _FakeResp(chunks, encoding=None)

    pieces = []
    _consume_sse(resp, pieces.append)

    assert "".join(pieces) == content
