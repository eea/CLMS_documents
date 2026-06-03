#!/usr/bin/env python3
"""Strip entries referencing '/non-browsable/' from a sitemap.xml or llms.txt.
Usage: python3 remove_non_browsable.py [--format {sitemap,llms}] <path>"""
import argparse
import re
import xml.etree.ElementTree as ET
from pathlib import Path

NEEDLE = "/non-browsable/"
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
ET.register_namespace("", SITEMAP_NS)


def strip_sitemap(path: Path) -> int:
    tree = ET.parse(path)
    root = tree.getroot()
    ns = root.tag.split("}")[0] + "}" if root.tag.startswith("{") else ""
    removed = 0
    for url in list(root.findall(f"{ns}url")):
        loc = url.find(f"{ns}loc")
        if loc is not None and loc.text and NEEDLE in loc.text:
            root.remove(url)
            removed += 1
    if removed:
        tree.write(path, encoding="utf-8", xml_declaration=True)
    return removed


def strip_llms(path: Path) -> int:
    link_re = re.compile(r"\]\(([^)]+)\)")
    lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
    kept, removed = [], 0
    for line in lines:
        if any(NEEDLE in target for target in link_re.findall(line)):
            removed += 1
            continue
        kept.append(line)
    if removed:
        path.write_text("".join(kept), encoding="utf-8")
    return removed


HANDLERS = {"sitemap": strip_sitemap, "llms": strip_llms}


def main():
    parser = argparse.ArgumentParser(description="Remove /non-browsable/ entries from a sitemap or llms.txt.")
    parser.add_argument("path", type=Path, help="File to strip in place")
    parser.add_argument("--format", choices=HANDLERS.keys(), default="sitemap")
    args = parser.parse_args()

    removed = HANDLERS[args.format](args.path)
    if removed:
        print(f"Removed {removed} non-browsable entries from {args.format}.")
    else:
        print(f"No non-browsable entries found in {args.format}.")


if __name__ == "__main__":
    main()
