#!/usr/bin/env python3
"""
remove_non_browsable_from_sitemap.py
Removes <url> entries from sitemap.xml whose <loc> contains '/non-browsable/'
Usage: python3 remove_non_browsable_from_sitemap.py <sitemap.xml>
"""
import sys
import xml.etree.ElementTree as ET

if len(sys.argv) != 2:
    print("Usage: python3 remove_non_browsable_from_sitemap.py <sitemap.xml>")
    sys.exit(1)

sitemap_path = sys.argv[1]
tree = ET.parse(sitemap_path)
root = tree.getroot()

namespace = ''
if root.tag.startswith('{'):
    namespace = root.tag.split('}')[0] + '}'

urls = root.findall(f"{namespace}url")
removed = 0
for url in urls:
    loc = url.find(f"{namespace}loc")
    if loc is not None and '/non-browsable/' in loc.text:
        root.remove(url)
        removed += 1

if removed:
    tree.write(sitemap_path, encoding='utf-8', xml_declaration=True)
    print(f"Removed {removed} non-browsable URLs from sitemap.")
else:
    print("No non-browsable URLs found in sitemap.")
