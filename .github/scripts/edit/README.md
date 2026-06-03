# edit/ — editor / author-time scripts

Scripts in this directory are run **by an editor or author** when they're
working on a document. They modify the `.qmd` source in place; their
output is intended to be committed to the repo.

## Policy

- **NOT run by CI.** Build pipelines do not invoke anything in this
  directory.
- **Modify `.qmd` source.** The whole point is that the docx pipeline reads
  the improved qmd on subsequent renders.
- **Idempotent re-runs.** Running a script twice on the same source
  should produce no further change (so an editor can safely re-run after
  swapping a figure or correcting a caption).
- **Document-specific.** Most scripts take one or more `.qmd` paths.

## Files

- `stamp_qmd_image_widths.py` — for every image reference in the qmd,
  read the source PNG's pixel dimensions and stamp a `{width=X.XXin}`
  attribute. Width is `min(intrinsic / 150 dpi, max_width_in)`. Run when
  adding or changing figure sources so the next render gets sensible
  per-figure widths instead of every image stretched to full column.

## When to add a script here

- Migrating qmd content to a Pandoc-correct convention
  (e.g., bare `Table N:` paragraphs → `: Table N:` caption syntax).
- Bulk-stamping or normalising qmd attributes that the build pipeline
  can't safely infer at render time.
- Linters / static checks an author runs locally before committing.
