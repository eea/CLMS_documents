#!/usr/bin/env python3
"""Generate a parallel sitemap whose <loc> entries point to the *.llms.md Markdown
companions Quarto emits (llms-txt: true), falling back to the original HTML URL
when no companion exists on disk."""
import argparse
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import urlparse, unquote

NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
URL_TAG = f"{{{NS}}}url"
LOC_TAG = f"{{{NS}}}loc"
ET.register_namespace("", NS)


def companion_path(url_path):
    """Map a sitemap URL path to the expected .llms.md companion URL path.
    Returns None when the URL shape is unrecognized (caller keeps original)."""
    if url_path.endswith(".html"):
        return url_path[:-5] + ".llms.md"
    if url_path.endswith("/") or "." not in Path(url_path).name:
        return url_path.rstrip("/") + "/index.llms.md"
    return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Source sitemap.xml")
    parser.add_argument("output", type=Path, help="Destination sitemap-llm.xml")
    args = parser.parse_args()

    site_root = args.input.parent
    tree = ET.parse(args.input)
    root = tree.getroot()

    rewritten = fallback = 0
    for url in root.findall(URL_TAG):
        loc = url.find(LOC_TAG)
        if loc is None or not loc.text:
            continue
        parsed = urlparse(loc.text)
        companion_rel = companion_path(unquote(parsed.path))
        if companion_rel and (site_root / companion_rel.lstrip("/")).exists():
            loc.text = parsed._replace(path=companion_rel).geturl()
            rewritten += 1
        else:
            fallback += 1

    tree.write(args.output, encoding="utf-8", xml_declaration=True)
    print(f"Wrote {args.output}: {rewritten} rewritten to .llms.md, {fallback} kept as HTML.")


if __name__ == "__main__":
    main()
