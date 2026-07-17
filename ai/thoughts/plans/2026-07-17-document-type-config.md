# Document-type config — design

**Status:** proposal, awaiting review. No code written.
**Date:** 2026-07-17
**Driver:** `DOCS/CDSE_Migration/CLMS_CDSE_Migration_Dashboard.qmd` — an interactive
OJS dashboard that must render without keywords, TOC, description, changelog or
contact block, while keeping the library's styling.

## Problem

The pipeline assumes every document is a *technical document*: it injects
AI-generated keywords and an intro, fills `version`, injects a changelog and a
contact block, and renders HTML + Typst PDF + gfm. A dashboard wants almost none
of that, but it is not a one-off — `CLMS_CDSE_Migration_Status.qmd` is a second
document of the same shape, and more are expected.

Three facts make this a pipeline problem rather than an authoring problem:

1. **`strip_unknown_frontmatter.py` is a choke point.** Its `ALLOWLIST` is
   `{title, subtitle, category, date, description, author, version, keywords,
   original-filename}`. Anything a document declares outside that list — `toc`,
   `format`, `css` — is deleted from the build copy before Quarto sees it. A
   document therefore *cannot* opt out of anything by editing its own frontmatter.
2. **The AI metadata is already generated.** `.llm_cache/DOCS__CDSE_Migration__
   CLMS_CDSE_Migration_Dashboard.qmd.json` already holds 11 keywords and an intro,
   and `apply_cached_intros.py` injects them into frontmatter at build time.
3. **An existing opt-out is already dead.** `filters/inject_contact_info.lua`
   honours `contact: false` in frontmatter — but `contact` is not in the allowlist,
   so it is stripped before the filter runs. The contact block is currently
   injected unconditionally. This design revives that flag as a side effect.

## Decisions taken (agreed with maintainer, 2026-07-17)

- Config is **declarative on/off toggles**, not pipeline verbs (`drop:` etc.).
  The config states *what a document has*; the build works out how.
- The **`document` type carries the baseline explicitly**. Every default is
  visible in YAML; a new type copies and flips what differs. No hidden defaults
  in Python.
- **Dashboards are HTML-only** — no Typst PDF, no gfm.
- The config also carries **styling/template** where a type needs its own.

## Mechanism — verified

The design rests on one question: can a single document restrict which formats
render, inside the project-wide `quarto render` the build does in one pass?

**Yes.** Confirmed two independent ways.

Quarto's [Project Basics](https://quarto.org/docs/projects/quarto-projects.html)
docs state metadata is deep-merged with document > directory > project precedence,
then:

> "The one exception to metadata merging is `format`. If the document-level YAML
> defines a format, it must define the complete list of formats to be rendered."

Empirically, rendering two documents through the **real** `_meta` config
(`_quarto-no-headers.yml` + `includes/default-no-headers.yml`, which declare
html + typst + gfm):

| document | frontmatter | outputs |
|---|---|---|
| `plain.qmd` | *(no `format:`)* | `.html`, `.pdf`, `.md`, `.llms.md` |
| `dash.qmd` | `format: {html: {toc: false}}` | `.html`, `.llms.md` |

So declaring `format: html` alone suppresses the Typst PDF and the gfm output.
Two useful consequences:

- **The PDF download link disappears on its own.** `dash.html` contained no
  `.pdf` link and no `quarto-alternate-formats` block, because no PDF was built.
  `format-links` needs no override — one fewer knob. (Per Quarto's docs
  `format-links: false` only hides the *link*; it does not stop the render. We
  don't need it.)
- **Frontmatter beats everything.** Because frontmatter is the highest-precedence
  layer, merging the type config *into frontmatter* wins over `_quarto.yml` and
  `metadata-files` by construction — no ordering subtleties.

### Why frontmatter merge rather than the alternatives

- **Quarto profiles** (`_quarto-dashboard.yml` + `--profile`) apply project-wide,
  not per document; a maintainer confirmed per-document format variation isn't
  natively supported this way. The build's `index.qmd` pass uses a profile, but
  that works only because indexes are a whole separate render pass.
- **Directory `_metadata.yml`** is folder-scoped. Documents are grouped into
  folders by `category`, so dashboards and ordinary non-browsable documents land
  in the *same* `non-browsable/` folder. A per-folder file cannot distinguish them.
- **`project: render:`** excludes a file entirely; it can't restrict formats.
- **`format: {typst: false}`** is not supported — no such syntax exists.

## Config shape

`.github/scripts/doc-types.yml` — sits beside the existing `categories.yml`:

```yaml
types:
  - name: document              # the library default
    elements:
      toc: true
      keywords: true
      description: true
      version: true
      changelog: true
      contact: true
      code: true
      number-sections: true
    formats: [html, typst, gfm]

  - name: dashboard
    elements:
      toc: false
      keywords: false
      description: false
      version: false
      changelog: false
      contact: false
      code: false
      number-sections: false
    formats: [html]
    style:
      page-layout: full
      # css: _meta/theme/dashboard.css   # only if a type needs its own
```

Every toggle maps to an injection point that **exists today** — no invented knobs:

| toggle | what it controls | mechanism |
|---|---|---|
| `toc` | table of contents | `toc:` frontmatter (overrides `default-no-headers.yml`) |
| `number-sections` | section numbering | `number-sections:` frontmatter |
| `keywords` | AI keywords | field written by `apply_cached_intros.py` |
| `description` | AI intro | field written by `apply_cached_intros.py` |
| `version` | version field + title-meta block | `fill_version.py` + `default-before-body.html` |
| `changelog` | changelog section | `build/inject_changelog.py` pandoc filter |
| `contact` | EEA contact block | `filters/inject_contact_info.lua` (`contact: false`) |
| `code` | source-code display | `echo:` / `code-fold:` — **see open question 2** |
| `formats` | outputs rendered | frontmatter `format:` (verified above) |
| `style` | layout/theme | `format.html` keys merged into frontmatter |

## Wiring

Mirror `categories.yml` + `helpers/categories.py` exactly — same loader shape,
same loud `sys.exit` on a malformed config, same `__main__` assert self-check.

1. **`.github/scripts/doc-types.yml`** — as above.
2. **`.github/scripts/helpers/doc_types.py`** — cached loader, validation
   (unknown type name, unknown toggle key, unknown format), `allowed_names()`,
   `config_for(name)`. Self-check under `__main__` like `categories.py`.
3. **`strip_unknown_frontmatter.py`** — the one real touch point. It already
   rewrites frontmatter in the build copy, so it becomes: add `document-type` to
   `ALLOWLIST`, strip as today, then resolve the document's type and apply that
   type's toggles + `formats` + `style` into the frontmatter. A `false` toggle
   removes the field (`keywords`) or sets the flag the downstream step reads
   (`contact: false`).
4. **`validate_qmd_files.py`** — accept `document-type`, validate against
   `allowed_names()`, defaulting to `document` when absent. Mirrors the existing
   `category` check.
5. **Tag the two CDSE documents** with `document-type: dashboard`.

Adding a future type is then a YAML entry — no code change. That is the generic
part of the solution.

## Open questions — must resolve before implementing

1. **`.llms.md` is not produced by the gfm writer.** In the render test,
   `dash.qmd` produced **`dash.llms.md` despite rendering HTML only**, and for
   `plain.qmd` the gfm output (`plain.md`) and `plain.llms.md` were *different
   files*. The `.llms.md` companion comes from `website: llms-txt: true` in
   `_quarto-no-headers.yml`, independent of `formats:`. So `formats: [html]` does
   **not** deliver "HTML only" — the dashboard still gets an `.llms.md`, and
   `generate_llm_sitemap.py` will still list it. **This contradicts CLAUDE.md**,
   which describes `.llms.md` as the gfm writer's output. Needs a decision: is an
   `.llms.md` for a dashboard acceptable (it is arguably useful — a text summary
   of a page an LLM cannot execute), or must it be suppressed too? If suppressed,
   the mechanism is unknown and needs its own spike.
2. **`code: false` is unverified.** I claimed earlier that `echo: false` retires
   the OJS `display = "none"` hack in the dashboard (commits `e9f2faaa`,
   `8b044258`, `a1449dfe`). My test was **inconclusive** — the control document
   with `echo` at its default *also* showed no source text, so the test proved
   nothing either way. Do not treat the hack as retired until this is re-tested
   properly. If `echo: false` does work, the hack and its three follow-up commits
   should be deleted as part of this work.
3. **The Version title-meta block.** `_meta/includes/default-before-body.html`
   unconditionally injects a "Version" heading into `.quarto-title-meta` via JS,
   reading `{{< meta version >}}`. With `version: false` this renders an empty
   Version heading. `include-before-body` likely needs to be type-controlled, or
   the script needs a guard. Not yet designed.
4. **Known Quarto edge case.** [quarto-cli#9605](https://github.com/quarto-dev/quarto-cli/issues/9605)
   (open) reports a document's `format:` failing to override a directory
   `_metadata.yml`. We introduce no `_metadata.yml`, so this shouldn't bite — but
   it is a reason not to add one later without re-testing.

## Non-goals

- **Skipping AI *generation* for dashboards.** The intro/keywords are still
  generated into `.llm_cache/`; the build simply doesn't use them. Generation is
  cached and costs no API at build time. Add a generation-side skip when it
  actually costs something.
- **Replacing `category`.** `document-type` is an orthogonal axis: `category`
  controls *where a document is routed and whether it is browsable*;
  `document-type` controls *what a document is made of*. Both CDSE documents are
  `category: non-browsable` **and** `document-type: dashboard`, but a
  non-browsable ordinary document is a real combination.

## Success criteria

*Automated:*
- `ruff check .github/scripts/` clean
- `python3 .github/scripts/helpers/doc_types.py` self-check passes
- `python3 .github/scripts/validate_qmd_files.py` passes
- `python3 -m pytest tests/`
- Full `bash .github/scripts/build/build-docs.sh` succeeds

*Manual:*
- `_site/non-browsable/<dashboard>.html` renders with library styling, no TOC,
  no keywords, no contact block, no changelog, no Version heading
- **No `.pdf` is emitted for either CDSE document**, and no PDF link is shown
- An ordinary product document is **byte-identical** to its pre-change output —
  this change must be a no-op for every existing document
