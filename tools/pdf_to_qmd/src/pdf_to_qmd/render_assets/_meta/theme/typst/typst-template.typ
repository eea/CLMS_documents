// Typst template approximating template-guideline.docx styling.
//
// Page geometry from the docx sectPr (A4, 1in top/left/right, ~1.32in bottom).
// Colors and font sizes derived from word/styles.xml.
// Used by Quarto as a template-partial (overrides typst-template.typ).

#let clms-blue       = rgb("#004494")
#let clms-blue-dark  = rgb("#004B7F")
#let heading4-blue   = rgb("#0F4761")
#let caption-blue    = rgb("#3E6893")
#let link-purple     = rgb("#605C9F")
#let footer-grey     = rgb("#808080")
#let clms-green      = rgb("#A0B128")

// Font stacks — first family wins where installed; later names are visually
// equivalent free fallbacks so the template renders on Linux CI too.
// Font stacks below intentionally contain only SIL-OFL-licensed families so
// rendered PDFs can be redistributed without proprietary-font concerns.
// Liberation Sans is the OFL drop-in for Arial; Carlito is the OFL drop-in for
// Calibri (same metrics, same line breaks, very subtly different letterforms).
#let sans-family = ("Liberation Sans",)
#let body-family = ("Lato", "Carlito", "Liberation Sans")
#let mono-family = ("JetBrains Mono", "DejaVu Sans Mono", "Liberation Mono")

#let article(
  title: none,
  subtitle: none,
  authors: none,
  date: none,
  version: none,
  abstract: none,
  abstract-title: none,
  toc: false,
  toc_title: "Table of contents",
  toc_depth: 3,
  toc_indent: 1.5em,
  cols: 1,
  margin: (top: 2.54cm, left: 2.54cm, right: 2.54cm, bottom: 3.35cm),
  paper: "a4",
  lang: "en",
  region: "GB",
  font: body-family,
  fontsize: 10pt,
  sectionnumbering: none,
  doc,
) = {
  // ---- document metadata ----------------------------------------------------
  // set document(author: ...) requires plain strings — the show partial emits
  // names as content (wrapped in [...]) so we walk the content tree to coerce
  // back to string before setting PDF metadata.
  let content-to-str(c) = {
    if type(c) == str { c }
    else if type(c) == content {
      if c.has("text") { c.text }
      else if c.has("body") { content-to-str(c.body) }
      else if c.has("children") { c.children.map(content-to-str).join("") }
      else { "" }
    } else { str(c) }
  }
  set document(
    title: if title != none { title } else { "" },
    author: if authors != none and authors.len() > 0 {
      authors.map(a => content-to-str(if type(a) == dictionary { a.name } else { a }))
    } else { () },
  )

  set text(lang: lang, region: region, font: font, size: fontsize)
  set par(justify: true, leading: 0.65em)

  // ---- headings -------------------------------------------------------------
  show heading: set text(font: sans-family, weight: "bold")
  show heading: set par(justify: false, leading: 0.4em)
  // Chapter (level-1) headings flow inline with the body — no forced page
  // break. The only automatic pagebreak in the document is after the TOC
  // (below). Authors who want a break at a specific chapter use the explicit
  // `{{< pagebreak >}}` shortcode in the qmd.
  show heading.where(level: 1): it => {
    set text(size: 20pt, fill: clms-blue)
    block(above: 1.5em, below: 0.8em, it)
  }
  show heading.where(level: 2): it => {
    set text(size: 14pt, fill: clms-blue)
    block(below: 1em, it)
  }
  show heading.where(level: 3): it => {
    set text(size: 12pt, fill: clms-blue)
    block(below: 1em, it)
  }
  show heading.where(level: 4): it => {
    set text(size: 11pt, fill: heading4-blue, weight: "regular")
    block(below: 1.2em, it)
  }
  show heading.where(level: 5): set text(size: 11pt, fill: heading4-blue, weight: "regular")
  // Heading numbering: append "." after top-level number ("6." vs "6.1" / "6.1.1")
  set heading(numbering: (..nums) => {
    let n = nums.pos()
    if n.len() == 1 {
      str(n.at(0)) + "."
    } else {
      n.map(str).join(".")
    }
  })

  // ---- long snake_case wrapping ---------------------------------------------
  // Insert a zero-width space after each underscore so long identifiers like
  // Prefix_DataTheme_DataSub-Theme_… can break across lines.
  // Skipped inside raw blocks via the show raw rule below (which sets its own content).
  show regex("_"): it => it + "\u{200B}"

  // ---- links ----------------------------------------------------------------
  // Style links and inject break opportunities inside long URLs so they wrap
  // at /, ?, &, = boundaries (matches the docx fix_docx_url_breaks behaviour).
  show link: it => {
    show regex("[/?&=]"): m => m + "\u{200B}"
    set text(fill: link-purple, weight: "bold")
    it
  }

  // ---- code / verbatim ------------------------------------------------------
  show raw: set text(font: mono-family, size: 7.5pt)
  show raw.where(block: true): it => {
    set par(leading: 0.45em)
    block(
      width: 100%,
      fill: luma(245),
      radius: 6pt,
      stroke: (left: 3pt + clms-blue),
      inset: (left: 14pt, right: 12pt, top: 10pt, bottom: 10pt),
      it,
    )
  }

  // ---- figure captions ------------------------------------------------------
  // `it.body` renders just the caption text from the qmd; `it` (the default)
  // would add Typst's auto "Figure N:" supplement on top, which the docx-imported
  // captions already carry. Without this, "Figure 12: foo" would become
  // "Figure 12: Figure 12: foo" in the PDF. HTML never auto-prefixes, so this
  // keeps both outputs consistent.
  show figure.caption: it => {
    set text(size: 9pt, fill: caption-blue)
    it.body
  }
  // Extra breathing room after each figure (caption-to-next-paragraph gap).
  show figure: set block(below: 1.6em)
  // A captioned table is wrapped by Quarto in a #figure, and Typst figures are
  // NON-breakable by default — so a tall captioned table cannot split across a
  // page and overflows (its overflow rows cram and overlap at the page bottom).
  // Let table figures break across pages; image figures stay atomic. Quarto tags
  // table floats with kind "quarto-float-tbl" (NOT the built-in `table` kind).
  show figure.where(kind: "quarto-float-tbl"): set block(breakable: true)

  // ---- lists ----------------------------------------------------------------
  // Bullet rotation matches the docx template (Symbol •, Courier o, Wingdings ▪).
  set list(
    indent: 1em,
    body-indent: 0.6em,
    marker: ([•], [◦], [▪]),
  )
  set enum(indent: 1em, body-indent: 0.6em)

  // ---- tables ---------------------------------------------------------------
  // Cell alignment. Body cells default LEFT; the header row (y: 0) is centered
  // by the show rule below. This holds only while Quarto emits `align: (auto, …)`
  // columns. CAVEAT: a first-row band carrying an inline `text-align:center` (a
  // centered colspan title) makes pandoc propagate that center to EVERY column —
  // rendering all body cells centered — and a cell-level `set align` CANNOT
  // override that explicit column tuple. So the header row must rely on THIS
  // rule to center and must NOT carry an inline text-align:center; the
  // converter's `neutralize_header_center` step strips it from row 0 so the
  // columns stay `auto`. A per-cell `text-align` elsewhere (a right-aligned
  // numeric column, a centered grouping label) is an explicit cell align and
  // still wins.
  set table(
    stroke: 0.5pt + luma(180),
    inset: 6pt,
    align: left + horizon,
  )
  show table.cell: set align(left + horizon)
  show table.cell.where(y: 0): set text(font: sans-family, size: 9.5pt, fill: clms-blue, weight: "bold")
  show table.cell.where(y: 0): set align(center + horizon)
  // Columns are sized to fit each column's longest word (see the table-fix phase),
  // so disable hyphenation in cells: words wrap whole instead of breaking mid-word
  // (no "Conif-/erous"), and they still fit because the column floors guarantee it.
  show table.cell: set text(size: 9pt, hyphenate: false)

  // Nested tables are used for in-cell LAYOUT (e.g. two-column bullet lists),
  // not data — they should carry no border. Every table strips the stroke of
  // any table nested INSIDE it: the outer table keeps the grey stroke it was
  // constructed with (from the `set` above), while a `set table(stroke: none)`
  // inside the show rule reaches only its descendant tables. (A `set` inside a
  // `show table` rule restyles tables nested within `it`, not `it` itself —
  // which is exactly the behaviour we want here.) Quarto's HTML→Typst turns a
  // `border:0` on the nested HTML table into explicit black cell strokes, so the
  // convert prompt must NOT emit `border:0`; the suppression happens here.
  show table: it => {
    set table(stroke: none)
    it
  }

  // ---- page layout ----------------------------------------------------------
  set page(
    paper: paper,
    margin: margin,
    numbering: none, // we draw the footer manually
    header-ascent: 1.0cm,
    footer-descent: 18pt,
    header: context {
      // No header on front matter (title page, TOC, abstract); shown only
      // once `body-started` flips, which happens just before the document body.
      if not state("body-started", false).get() { return none }
      // Three logos left, EEA right, all on one row vertically centered.
      // Negative horizontal pad pushes the strip to full page width.
      pad(x: -2.54cm, y: 0pt)[
        #block(
          width: 100%,
          inset: (left: 1.0cm, right: 1.0cm),
          spacing: 0pt,
          grid(
            columns: (auto, auto, auto, 1fr, auto),
            column-gutter: 14pt,
            align: horizon,
            image("/_meta/theme/typst/logos/eu.png",         height: 0.75cm),
            image("/_meta/theme/typst/logos/copernicus.png", height: 0.75cm),
            image("/_meta/theme/typst/logos/clms.png",       height: 0.75cm),
            [],
            image("/_meta/theme/typst/logos/eea.png",        height: 0.75cm),
          ),
        )
      ]
    },
    footer: context {
      // Footer only renders on body pages; title page and TOC stay clean.
      if not state("body-started", false).get() { return none }
      // Page counter is reset to 1 at the start of the body, so this matches
      // the user-visible "Page 1, 2, …" numbering.
      let n = counter(page).at(here()).first()
      pad(x: -2.54cm, y: 0pt)[
        #block(
          width: 100%,
          inset: (left: 2.54cm, right: 2.54cm),
          {
            set text(font: body-family, size: 7pt, fill: footer-grey)
            align(right)[
              #if title != none [#title \ ]
              Page #n
            ]
          },
        )
      ]
    },
  )

  // ---- TITLE PAGE -----------------------------------------------------------
  // Matches the docx layout: centered title + subtitle, large centered CLMS
  // logo in the middle, Author/Date/Version row at the bottom with gray labels.
  // No top header (handled by the page header rule which skips page 1).
  if title != none {
    v(1cm)
    // Title + subtitle: no hyphenation, breaks only at whole-word boundaries.
    set par(justify: false)
    align(center)[
      #text(
        font: sans-family, size: 28pt, fill: clms-blue, weight: "bold",
        hyphenate: false, lang: "en",
        title,
      )
      #v(0.7em)
      #if subtitle != none {
        text(
          font: sans-family, size: 20pt, fill: clms-blue, weight: "regular",
          hyphenate: false, lang: "en",
          subtitle,
        )
      }
    ]

    v(1fr)
    align(center, image("/_meta/theme/typst/logos/clms.png", width: 10cm))
    v(1fr)

    // Author / Date / Version block — labels light gray, values bold/regular.
    // Sits at the very bottom of the content area with generous row spacing.
    let label = txt => text(fill: rgb("#7F7F7F"), txt)
    set text(size: 11pt)
    pad(left: 0.5cm)[
      #grid(
        columns: (auto, 1fr),
        column-gutter: 1.5em,
        row-gutter: 1.1em,
        label[Author:],   text(weight: "bold")[European Environment Agency (EEA)],
        label[Date:],     if date != none { text(weight: "bold", date) } else { "" },
        label[Version:],  if version != none { text(weight: "bold", version) } else { "" },
      )
    ]

    pagebreak()
  }

  // ---- optional table of contents -------------------------------------------
  if toc {
    block(above: 0pt, below: 1.8em)[
      #text(font: sans-family, size: 20pt, fill: clms-blue, weight: "bold", toc_title)
    ]
    show outline.entry: set block(above: 1em)
    outline(
      title: none,
      depth: toc_depth,
      indent: toc_indent,
    )
  }

  // ---- optional abstract ----------------------------------------------------
  if abstract != none {
    block(above: 0pt, below: 1em)[
      #text(font: sans-family, size: 14pt, fill: clms-blue, weight: "bold",
            if abstract-title != none { abstract-title } else { "Abstract" })
    ]
    abstract
    v(1em)
  }

  // ---- standard contact block (front matter, directly after the TOC) --------
  // For HTML this is injected by inject_contact_info.lua; for Typst it is
  // rendered here instead so it sits in the front matter — unnumbered, no
  // header/footer — right after the TOC, with the body starting on the next
  // page. Keep the address in sync with .github/templates/contact_template.md.
  v(2em)
  block[
    *Contact:*

    European Environment Agency (EEA) \
    Kongens Nytorv 6 \
    1050 Copenhagen K \
    Denmark \
    #link("https://land.copernicus.eu/")[*#"https://land.copernicus.eu/"*]
  ]
  pagebreak()

  // ---- document body --------------------------------------------------------
  // Front matter (title page, TOC, contact) is unnumbered; restart page
  // counter so the body begins at "Page 1".
  state("body-started", false).update(true)
  counter(page).update(1)
  doc
}
