#!/usr/bin/env python3
import os
import json
import sys
import re
from html.parser import HTMLParser
import panflute as pf

CHANGE_LOG_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../.llm_cache/change_logs.json")
)
PATH_MAPPING_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../DOCS/_meta/.temp_path_mapping.json")
)


def _load_json_or_empty(path):
    """Load JSON from path, returning {} if the file is missing or corrupt.
    Corrupt files emit a stderr warning so CI logs surface the problem."""
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Warning: failed to load {path}: {e}", file=sys.stderr)
        return {}


# Helper: Resolve current file path to original path using mapping
def resolve_original_path(current_path, path_mapping):
    """
    Resolve the current file path to the original path using the mapping.
    The mapping keys are regrouped paths (without DOCS/), values are original paths (without DOCS/).
    Returns the full path WITH DOCS/ prefix to match changelog keys.
    """

    # Ensure DOCS/ prefix
    if not current_path.startswith("DOCS/"):
        current_path = f"DOCS/{current_path}"

    # Strip DOCS/ for mapping lookup
    lookup_path = current_path[5:]  # Remove "DOCS/"

    # Direct mapping lookup (lookup_path is the regrouped path, we want the original)
    if lookup_path in path_mapping:
        original = path_mapping[lookup_path]
        # Return with DOCS/ prefix to match changelog keys
        return f"DOCS/{original}"

    # No mapping found, return current_path (with DOCS/ prefix for consistency with changelog keys)
    return current_path


class _SafeListParser(HTMLParser):
    """Walks HTML and rebuilds it allowing only <ul>/<li> with no attributes.
    Any other tag sets `rejected`; on rejection callers fall back to plain text."""

    ALLOWED = {"ul", "li"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.text = []
        self.stack = []
        self.rejected = False

    def handle_starttag(self, tag, *_):
        if tag not in self.ALLOWED:
            self.rejected = True
            return
        self.out.append(f"<{tag}>")
        self.stack.append(tag)

    def handle_endtag(self, tag):
        if tag not in self.ALLOWED:
            self.rejected = True
            return
        if not self.stack or self.stack[-1] != tag:
            self.rejected = True
            return
        self.out.append(f"</{tag}>")
        self.stack.pop()

    def handle_data(self, data):
        self.out.append(data)
        self.text.append(data)


def sanitize_html_summary(summary):
    """Allow only a strict <ul>/<li> structure with no attributes; anything
    else (other tags, unbalanced markup, parse errors) collapses to plain text."""
    if not summary.strip().startswith("<ul>"):
        return summary

    parser = _SafeListParser()
    try:
        parser.feed(summary)
        parser.close()
    except Exception:
        return re.sub(r"<[^>]+>", "", summary)

    if parser.rejected or parser.stack:
        return "".join(parser.text)

    return "".join(parser.out)


def get_input_file(doc):
    """Get the input file path from various sources, in priority order."""
    meta = doc.get_metadata()

    # Try our custom original-filename field injected by group_docs_by_category.py (PREFERRED)
    original_filename = meta.get("original-filename")
    if original_filename:
        # Handle panflute MetaString objects
        if hasattr(original_filename, "text"):
            original_filename = original_filename.text
        return original_filename

    # Fallback: Try input-filename field from Lua filter (legacy)
    input_filename = meta.get("input-filename")
    if input_filename:
        # Handle panflute MetaString objects
        if hasattr(input_filename, "text"):
            input_filename = input_filename.text
        return input_filename

    # Try Quarto-specific metadata
    quarto_meta = meta.get("quarto", {})
    if quarto_meta:
        input_file = quarto_meta.get("input_file")
        if input_file:
            return input_file

    # Try standard Pandoc input-files field
    input_files = doc.get_metadata("input-files", [])
    if input_files:
        input_file = input_files[0] if isinstance(input_files, list) else input_files
        return input_file

    # Try environment variable
    env_input = os.environ.get("QUARTO_PROJECT_INPUT")
    if env_input:
        return env_input

    # Try other metadata keys
    for key in ["input-file", "source-file", "file", "filename"]:
        if key in meta:
            value = meta[key]
            if isinstance(value, dict) and "c" in value:
                input_file = value["c"]
            elif isinstance(value, str):
                input_file = value
            else:
                continue
            return input_file

    return None


def add_changelog(doc):
    """Main filter function that adds changelog to the document"""
    current_file = get_input_file(doc)
    if not current_file:
        return doc

    logs = _load_json_or_empty(CHANGE_LOG_PATH)
    path_mapping = _load_json_or_empty(PATH_MAPPING_FILE)

    # Changelog keys use the original (pre-regroup) path, so map back to it.
    original_path = resolve_original_path(current_file, path_mapping)

    if original_path in logs:
        entries = logs[original_path]
        if entries:
            header = pf.Header(pf.Str("Change Log"), level=1, identifier="change-log")
            doc.content.append(header)

            # panflute Table structure:
            # https://scorreia.com/software/panflute/code.html#panflute.table_elements.Table
            header_cells = [
                pf.TableCell(pf.Plain(pf.Str("Date"))),
                pf.TableCell(pf.Plain(pf.Str("Version"))),
                pf.TableCell(pf.Plain(pf.Str("Summary"))),
            ]
            header_row = pf.TableRow(*header_cells)
            table_head = pf.TableHead(header_row)

            body_rows = []
            for entry in entries:
                raw_summary = entry["summary"].strip()
                sanitized_summary = sanitize_html_summary(raw_summary)  # untrusted AI output

                date_cell = pf.TableCell(pf.Plain(pf.Str(entry["date"])))
                version_cell = pf.TableCell(
                    pf.Plain(pf.Str(entry.get("version", "Unknown")))
                )

                # Render a <ul> summary as a real BulletList so it survives in
                # every output format; otherwise fall back to plain text.
                if sanitized_summary.startswith("<ul>"):
                    list_items = re.findall(
                        r"<li>(.*?)</li>", sanitized_summary, re.DOTALL
                    )
                    if list_items:
                        list_items_elements = []
                        for item in list_items:
                            clean_item = re.sub(r"<[^>]+>", "", item).strip()
                            # ListItem expects a list of Block elements
                            list_item = pf.ListItem(pf.Plain(pf.Str(clean_item)))
                            list_items_elements.append(list_item)
                        bullet_list = pf.BulletList(*list_items_elements)
                        summary_cell = pf.TableCell(bullet_list)
                    else:
                        clean_summary = re.sub(r"<[^>]+>", "", sanitized_summary)
                        summary_cell = pf.TableCell(pf.Plain(pf.Str(clean_summary)))
                else:
                    summary_cell = pf.TableCell(pf.Plain(pf.Str(sanitized_summary)))

                row = pf.TableRow(date_cell, version_cell, summary_cell)
                body_rows.append(row)

            table_body = pf.TableBody(*body_rows)

            # colspec sets relative column widths summing to 1.0 — this makes
            # the rendered table fill the full text-area width (otherwise
            # Pandoc emits auto-width columns and the table shrinks to content
            # in Typst output).
            colspec = [
                ("AlignDefault", 0.15),  # Date
                ("AlignDefault", 0.10),  # Version
                ("AlignDefault", 0.75),  # Summary (long descriptive text)
            ]
            table = pf.Table(table_body, head=table_head, colspec=colspec)

            doc.content.append(table)

    return doc


def finalize(doc):
    return add_changelog(doc)


if __name__ == "__main__":
    # No per-element action — all logic runs at finalize-time. Pass an explicit
    # no-op so panflute 2.3+ accepts the call (action is positional there).
    pf.run_filter(lambda elem, doc: None, finalize=finalize)
