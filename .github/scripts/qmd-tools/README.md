# qmd content-quality tools

Rewrite scripts that clean up `.qmd` source. They're written in Python but
operate on the Markdown, not on code (hence "qmd-tools", not "lint"). All are
idempotent — re-running on already-fixed content changes nothing. Written for
the Typst PDF path, but the fixes help any renderer.

## Usage

Each script takes a root directory and walks every `*.qmd` underneath:

```bash
python3 .github/scripts/qmd-tools/fix_pagebreaks.py      DOCS/
python3 .github/scripts/qmd-tools/strip_pagebreaks.py    DOCS/
python3 .github/scripts/qmd-tools/fix_typst_patterns.py  DOCS/
python3 .github/scripts/qmd-tools/fix_table_colwidths.py DOCS/
```

## What each script does

### `fix_pagebreaks.py`

Hoists inline `{{< pagebreak >}}` shortcodes onto their own paragraph. When
a pagebreak sits at the end of a list item, image caption, or table row,
Pandoc emits the resulting `#pagebreak()` *inside* a container, which Typst
rejects ("pagebreaks are not allowed inside of containers"). Moving the
pagebreak to its own paragraph promotes it out of the container.

### `strip_pagebreaks.py`

Removes every standalone `{{< pagebreak >}}` line. The Typst template
handles document-level breaks (after title page, after TOC) automatically;
explicit per-chapter pagebreaks are no longer needed.

### `fix_typst_patterns.py`

Three substitutions that resolve common Pandoc→Typst translation gotchas:

- **A** — Escape literal `*.ext` (file glob) asterisks to `\*.ext`. Without
  escaping, Pandoc treats `*…*` as emphasis and the resulting
  `#emph[…].ext` is read by Typst as field access on the emph value.
- **B** — Replace `@@download` (Plone CMS URL convention) with
  `%40%40download`. Pandoc reads the second `@` as a citation key, even
  when the first is backslash-escaped.
- **D** — Replace `+/-`, `+ /-`, `+ / -` with `±` (U+00B1). Inside list
  items, Pandoc emits `- + / - 5 m` which Typst's parser can't read.

### Image widths

Stamping image widths from native pixel size lives in
`../edit/stamp_qmd_image_widths.py` (px / DPI → `{width="Xin"}`, capped at the
A4 text width). See `../edit/README.md`.

### `fix_table_colwidths.py`

Computes column widths from cell content and applies them to every pipe
table by rewriting the divider line (the `|---|---|---|` row). Pandoc
reads the dash counts as relative column widths, so this works on any
pipe table — captioned or not.

Algorithm v3:

1. Tokenize each cell at whitespace, `_`, `-`, `–`, `—`, `/`, `?`, `&`,
   `=` to find the longest unbreakable token per column.
2. Column minimum width = `longest_token × 1.43%` (guarantees no overflow
   at 9pt body text across a ~70-char body width).
3. Distribute remaining slack proportional to total content per column.
4. Cap each column at 5%–65% and renormalise to sum 100%.
5. Rewrite the divider with dash counts proportional to the widths.
   If the caption already has a `tbl-colwidths` attribute, update its
   value in lockstep so both sources of truth agree.

Run them in any order, any number of times — each one no-ops on content it
has already fixed.
