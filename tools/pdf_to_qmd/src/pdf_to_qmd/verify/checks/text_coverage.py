"""Check: did the document's body text survive into the .qmd?

Compares the original PDF (not working.pdf, which has lost redaction-clipped text)
against the .qmd. Excludes figure-internal text and running header/footer chrome,
then reports a coverage % plus the source sentences missing from the .qmd.

Chrome exclusion uses marginchrome.detect_running_chrome() — content-type-agnostic
(text, image, or mixed), digit-insensitive so "PAGE 1"…"PAGE N" all collapse to
one signature.  The older identical-text fallback is kept as a backstop.
"""

import re
from collections import defaultdict

from .. import CheckResult, Finding, register
from ..textutil import normalize, pdf_lines, qmd_to_plain, shingles, split_sentences, tokens

# min tokens for a sentence to be worth checking; skips fragments, bare numbers, headers
_MIN_TOKENS = 5
# a sentence is "covered" if this fraction of its shingles appear in the .qmd
_SHINGLE_HIT = 0.5
_MAX_LISTED = 40

# short sentences (<= this many tokens) are too small for reliable 4-gram shingle
# overlap — one missing/extra token tanks the ratio. For them, use anchored-window
# token containment instead (e.g. "Allotment gardens → class 1.4").
_SHORT_MAX_TOKENS = 7
_CONTAIN_HIT = 0.8        # fraction of a short line's tokens that must co-occur
_WINDOW_SLACK = 5         # window half-width = len(tokens) + this

# backstop patterns for bare page numbers not caught by the region detector
_IGNORE_PATTERNS = [
    re.compile(r"^page \d+$"),
    re.compile(r"^\d+$"),
]


def _chrome_text_lines_fallback(lines, total_pages: int) -> set:
    """Identical-text fallback: lines that repeat on >= 50% of pages.

    Used when marginchrome is unavailable (no PyMuPDF) or as a belt-and-
    suspenders check for chrome not caught by the region detector.
    """
    pages_of = defaultdict(set)
    for pno, txt in lines:
        n = normalize(txt)
        if n:
            pages_of[n].add(pno)
    if total_pages < 2:
        return set()
    return {n for n, pages in pages_of.items()
            if len(pages) / total_pages >= 0.5 and len(pages) >= 2}


def _short_line_covered(toks, qmd_tokens, positions) -> bool:
    """True if a short sentence's tokens co-occur in a local window of the .qmd.

    Anchors on the rarest needle token (fewest occurrences in the .qmd), then
    checks a window around each occurrence for >= _CONTAIN_HIT of the needle
    tokens. Local co-occurrence — not bag-of-words over the whole doc — keeps
    false-OKs (scattered words) low while tolerating one missing/extra token.
    """
    need = set(toks)
    if not need:
        return True
    anchor = min(need, key=lambda t: len(positions.get(t, ())))
    anchor_positions = positions.get(anchor, ())
    if not anchor_positions:
        return False
    window = len(toks) + _WINDOW_SLACK
    for p in anchor_positions:
        lo, hi = max(0, p - window), min(len(qmd_tokens), p + window + 1)
        win = set(qmd_tokens[lo:hi])
        if len(need & win) / len(need) >= _CONTAIN_HIT:
            return True
    return False


@register
class TextCoverageCheck:
    name = "text_coverage"

    def applicable(self, ctx) -> bool:
        return bool(ctx.qmd_text) and ctx.original_pdf and ctx.original_pdf.exists()

    def run(self, ctx) -> CheckResult:
        # ── build per-page exclusion boxes (figures + chrome regions) ─────────
        exclude = defaultdict(list)

        # figure-internal text
        for f in ctx.figures:
            exclude[f["page"]].append(tuple(f["bbox"]))

        # running header/footer chrome via the shared region detector
        is_cover = (ctx.detections or {}).get("cover", {}).get("is_cover", False)
        skip_pages = {0} if is_cover else set()
        try:
            from ...marginchrome import detect_running_chrome
            chrome_regions = detect_running_chrome(ctx.original_pdf,
                                                   skip_pages=skip_pages)
            for pno, region_list in chrome_regions.items():
                exclude[pno].extend(region_list)
        except Exception:
            chrome_regions = {}

        lines = pdf_lines(ctx.original_pdf, exclude_boxes_by_page=dict(exclude))
        # the cover page isn't transcribed into the body (the Typst template rebuilds
        # the title page from frontmatter), so its text would falsely read as missing
        if is_cover:
            lines = [(p, t) for (p, t) in lines if p not in skip_pages]
        total_pages = (max((p for p, _ in lines), default=-1) + 1) or 1

        # fallback identical-text chrome (belt-and-suspenders + no-PyMuPDF path)
        fallback_chrome = _chrome_text_lines_fallback(lines, total_pages)

        def _ignored(norm_line: str) -> bool:
            return (
                norm_line in fallback_chrome
                or any(p.match(norm_line) for p in _IGNORE_PATTERNS)
            )

        source_text = "\n".join(
            txt for _, txt in lines if not _ignored(normalize(txt))
        )
        sentences = [s for s in split_sentences(source_text) if len(tokens(s)) >= _MIN_TOKENS]

        qmd_tokens = tokens(qmd_to_plain(ctx.qmd_text))
        qmd_shingles = shingles(qmd_tokens)
        # token -> sorted positions in the .qmd token stream, for the short-line path
        positions = defaultdict(list)
        for i, t in enumerate(qmd_tokens):
            positions[t].append(i)

        missing = []
        for s in sentences:
            stoks = tokens(s)
            if len(stoks) <= _SHORT_MAX_TOKENS:
                # short line: 4-gram shingles are too brittle — use windowed containment
                if not _short_line_covered(stoks, qmd_tokens, positions):
                    missing.append(s)
                continue
            sh = shingles(stoks)
            if not sh:
                continue
            hit = len(sh & qmd_shingles) / len(sh)
            if hit < _SHINGLE_HIT:
                missing.append(s)

        total = len(sentences)
        covered = total - len(missing)
        coverage = round(100 * covered / total, 1) if total else 100.0

        findings = [Finding(f"missing: {m[:120]}", "warn") for m in missing[:_MAX_LISTED]]
        if len(missing) > _MAX_LISTED:
            findings.append(Finding(f"… and {len(missing) - _MAX_LISTED} more", "info"))

        status = "ok" if not missing else "warn"
        return CheckResult(
            self.name, status,
            f"text coverage {coverage}% ({covered}/{total} sentences; {len(missing)} missing)",
            metric=coverage, findings=findings,
        )
