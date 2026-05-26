# build/ — build-time scripts

Scripts in this directory run as part of the CI build orchestrated by
`build-docs.sh` (and during local re-renders).

## Files

- `build-docs.sh` — top-level build orchestration. Runs the qmd→HTML and
  qmd→PDF (Typst) renders, plus index pages and sitemap post-processing.
- `build-docs.legacy.sh` — verbatim backup of the previous docx→LibreOffice→PDF
  pipeline. **Not invoked**; kept on disk as a recovery point until the
  current pipeline has had enough production usage to be considered stable.
- `update_url_mappings.py` — recompute the regrouped/original path map.
- `group_docs_by_category.py` — regroup `DOCS/<product>/…` into
  `DOCS/<category>/<category>_<original>` based on each qmd's
  `category:` YAML field.
- `strip_unknown_frontmatter.py` — drop YAML keys Quarto doesn't recognise
  from the build-tree copies of the qmds (`origin_DOCS/` is left alone).
- `generate_index_all.py` — generate `index.qmd` files for every
  category/product folder.
- `generate_llm_sitemap.py` — produce `sitemap-llm.xml` (each `<loc>`
  points at the `.llms.md` companion produced by Quarto's `gfm` writer).
- `remove_non_browsable.py` — strip non-browsable URLs from `sitemap.xml`
  and `llms.txt`.
- `inject_changelog.py` — Pandoc/panflute filter that appends a Change-Log
  table to each document from `.llm_cache/change_logs.json`.

For content-quality lints on `.qmd` source (image widths, table
column-widths, pagebreaks, etc.) see `../qmd-tools/`.
