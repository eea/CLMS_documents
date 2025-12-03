#!/usr/bin/env python3
import os
import json
import sys
import re
import panflute as pf

CHANGE_LOG_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../.llm_cache/change_logs.json")
)
PATH_MAPPING_FILE = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../DOCS/_meta/.temp_path_mapping.json")
)


# Helper: Load change logs
def load_change_logs():
    if os.path.exists(CHANGE_LOG_PATH):
        with open(CHANGE_LOG_PATH, "r") as f:
            data = json.load(f)
            return data
    return {}


# Helper: Load path mapping (regrouped -> original)
def load_path_mapping():
    if os.path.exists(PATH_MAPPING_FILE):
        try:
            with open(PATH_MAPPING_FILE, "r") as f:
                data = json.load(f)
                return data
        except (json.JSONDecodeError, IOError) as e:
            # If mapping file is corrupted or unreadable, continue without it
            pass
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


def sanitize_html_summary(summary):
    """Sanitize HTML content to prevent XSS and malicious code injection"""

    # Check if it's an HTML list
    if not summary.strip().startswith("<ul>"):
        return summary  # Plain text, no sanitization needed

    # Allow only specific safe HTML tags for lists
    allowed_tags = {"ul", "li"}

    # Remove any attributes from tags (e.g., onclick, style, etc.)
    summary = re.sub(r"<(\w+)\s+[^>]*>", r"<\1>", summary)

    # Find all HTML tags in the content
    tags = re.findall(r"</?(\w+)>", summary)

    # Check if all tags are allowed
    for tag in tags:
        if tag.lower() not in allowed_tags:
            # Convert to plain text by removing all HTML tags
            return re.sub(r"<[^>]+>", "", summary)

    # Additional security checks
    suspicious_patterns = [
        r"javascript:",
        r"on\w+\s*=",
        r"<script",
        r"<iframe",
        r"<object",
        r"<embed",
        r"<link",
        r"<meta",
        r"<style",
    ]

    for pattern in suspicious_patterns:
        if re.search(pattern, summary, re.IGNORECASE):
            return re.sub(r"<[^>]+>", "", summary)

    # Validate proper nesting (basic check)
    if summary.count("<ul>") != summary.count("</ul>") or summary.count(
        "<li>"
    ) != summary.count("</li>"):
        return re.sub(r"<[^>]+>", "", summary)

    return summary


def get_input_file(doc):
    """Get the input file path from various sources"""

    # Get metadata
    meta = doc.get_metadata()

    # Debug: log all available metadata keys

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

    # Get input file
    current_file = get_input_file(doc)
    if not current_file:
        return doc

    # Load data files
    logs = load_change_logs()
    path_mapping = load_path_mapping()

    # Resolve current path to original path using mapping
    original_path = resolve_original_path(current_file, path_mapping)

    # Look up changelog entries using original path
    if original_path in logs:
        entries = logs[original_path]
        if entries:
            # Create changelog table using HTML for cross-format compatibility

            # Add heading with id attribute
            header = pf.Header(pf.Str("Change Log"), level=1, identifier="change-log")
            doc.content.append(header)

            # Create table using proper panflute structure
            # Based on: https://scorreia.com/software/panflute/code.html#panflute.table_elements.Table

            # Create column specifications (3 columns: Date, Version, Summary)
            # Using simple approach without alignment specifications
            colspec = None

            # Create table header with 3 columns: Date, Version, Summary
            header_cells = [
                pf.TableCell(pf.Plain(pf.Str("Date"))),
                pf.TableCell(pf.Plain(pf.Str("Version"))),
                pf.TableCell(pf.Plain(pf.Str("Summary"))),
            ]
            header_row = pf.TableRow(*header_cells)
            table_head = pf.TableHead(header_row)

            # Create table body rows
            body_rows = []
            for entry in entries:
                raw_summary = entry["summary"].strip()

                # Sanitize the summary for security
                sanitized_summary = sanitize_html_summary(raw_summary)

                # Create date cell
                date_cell = pf.TableCell(pf.Plain(pf.Str(entry["date"])))

                # Create version cell
                version_cell = pf.TableCell(
                    pf.Plain(pf.Str(entry.get("version", "Unknown")))
                )

                # Create summary cell - handle HTML lists vs plain text
                if sanitized_summary.startswith("<ul>"):
                    # Convert HTML list to panflute BulletList for cross-format compatibility
                    import re

                    list_items = re.findall(
                        r"<li>(.*?)</li>", sanitized_summary, re.DOTALL
                    )
                    if list_items:
                        # Clean HTML tags from list items and create BulletList
                        list_items_elements = []
                        for item in list_items:
                            clean_item = re.sub(r"<[^>]+>", "", item).strip()
                            # ListItem expects a list of Block elements
                            list_item = pf.ListItem(pf.Plain(pf.Str(clean_item)))
                            list_items_elements.append(list_item)
                        bullet_list = pf.BulletList(*list_items_elements)
                        summary_cell = pf.TableCell(bullet_list)
                    else:
                        # Fallback to plain text if list parsing fails
                        clean_summary = re.sub(r"<[^>]+>", "", sanitized_summary)
                        summary_cell = pf.TableCell(pf.Plain(pf.Str(clean_summary)))
                else:
                    # For plain text, use Plain element
                    summary_cell = pf.TableCell(pf.Plain(pf.Str(sanitized_summary)))

                # Create version cell
                version_cell = pf.TableCell(
                    pf.Plain(pf.Str(entry.get("version", "Unknown")))
                )

                # Create table row with 3 cells: date, version, summary
                row = pf.TableRow(date_cell, version_cell, summary_cell)
                body_rows.append(row)

            # Create table body
            table_body = pf.TableBody(*body_rows)

            # Create the complete table
            # Table constructor: Table(*bodies, head=None, foot=None, colspec=None, caption=None)
            table = pf.Table(table_body, head=table_head)

            doc.content.append(table)

    return doc


def action(elem, doc):
    """Panflute filter action - called for each element"""
    # We don't process individual elements, just return unchanged
    return None


def finalize(doc):
    return add_changelog(doc)


if __name__ == "__main__":
    pf.run_filter(action, finalize=finalize)
