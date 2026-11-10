# Technical Library - Editor Guidelines

2026-05-26

- [<span class="toc-section-number">1</span> How This
  Works](#how-this-works)
  - [<span class="toc-section-number">1.1</span> Your project and the
    central library](#your-project-and-the-central-library)
  - [<span class="toc-section-number">1.2</span> The publish
    flow](#the-publish-flow)
  - [<span class="toc-section-number">1.3</span> The document
    lifecycle](#the-document-lifecycle)
- [<span class="toc-section-number">2</span> Starting a New
  Document](#starting-a-new-document)
  - [<span class="toc-section-number">2.1</span> From a
    template](#from-a-template)
  - [<span class="toc-section-number">2.2</span> From
    scratch](#from-scratch)
  - [<span class="toc-section-number">2.3</span> Migrating an existing
    document](#migrating-an-existing-document)
- [<span class="toc-section-number">3</span> The YAML
  Header](#the-yaml-header)
  - [<span class="toc-section-number">3.1</span> Required
    fields](#required-fields)
  - [<span class="toc-section-number">3.2</span> Optional
    fields](#optional-fields)
  - [<span class="toc-section-number">3.3</span> System-managed
    fields](#system-managed-fields)
- [<span class="toc-section-number">4</span> Writing
  Content](#writing-content)
  - [<span class="toc-section-number">4.1</span> Image folder
    convention](#image-folder-convention)
  - [<span class="toc-section-number">4.2</span> Page
    breaks](#page-breaks)
  - [<span class="toc-section-number">4.3</span> Complex table
    layouts](#complex-table-layouts)
- [<span class="toc-section-number">5</span> Editing and Previewing
  Locally](#editing-and-previewing-locally)
  - [<span class="toc-section-number">5.1</span> Open the project in
    RStudio](#open-the-project-in-rstudio)
  - [<span class="toc-section-number">5.2</span> Preview your
    document](#preview-your-document)
  - [<span class="toc-section-number">5.3</span> Render the full
    project](#render-the-full-project)
- [<span class="toc-section-number">6</span> Publishing to
  Develop](#publishing-to-develop)
- [<span class="toc-section-number">7</span> Folder and File
  Structure](#folder-and-file-structure)
- [<span class="toc-section-number">8</span> File Naming, Versioning,
  and Changelog](#file-naming-versioning-and-changelog)
  - [<span class="toc-section-number">8.1</span> The version
    suffix](#the-version-suffix)
  - [<span class="toc-section-number">8.2</span> When to create a new
    major version](#when-to-create-a-new-major-version)
  - [<span class="toc-section-number">8.3</span> Don’t rename after
    publishing](#dont-rename-after-publishing)
  - [<span class="toc-section-number">8.4</span> The change
    log](#the-change-log)
- [<span class="toc-section-number">9</span> Restoring Previous
  Versions](#restoring-previous-versions)
  - [<span class="toc-section-number">9.1</span> Commands](#commands)
  - [<span class="toc-section-number">9.2</span> When to use
    it](#when-to-use-it)
- [<span class="toc-section-number">10</span> Release
  Path](#release-path)

This guide is for editors writing and publishing documents in the CLMS
Technical Library. It covers the day-to-day workflow: starting a
document from a template, previewing it locally, publishing it to the
library, and keeping it in step with the central repository.

> [!NOTE]
>
> This guide assumes your project is already integrated with the
> Technical Library - the `DOCS/` subtree is in place and the Git
> aliases are configured. If that setup isn’t done yet, see the [Setup
> Guideline](guidelines_setup-guide_v1.html) first.

# How This Works

## Your project and the central library

Your project repository contains a `DOCS/` folder that is both part of
your project and part of the central CLMS Technical Library. The
connection works as a **git subtree**: your documents live in your repo,
but `git docs-publish` merges them into the library’s `develop` branch.

That means you own the source. You edit locally, commit to your project,
and publish when ready. The library pulls in documents from all
projects.

## The publish flow

Publishing to `develop` is not a public release. The public-facing
library only changes when a Technical Library owner promotes changes
from `develop` to `test` to `main`. As an editor, your work stops at
`develop`.

<img src="guidelines_editor-manual_v1-media/publish-flow.svg"
data-fig-align="center" />

## The document lifecycle

<img src="guidelines_editor-manual_v1-media/document-lifecycle.svg"
data-fig-align="center" />

Major version bumps are your decision - you create a new file with a
bumped `_v<N>` suffix. Minor and patch versions are AI-assigned at
release time based on the scope of changes.

# Starting a New Document

## From a template

Pick the template that matches your document type:

- `CLMS_Template_ATBD.qmd` - Algorithm Theoretical Basis Document, for
  the scientific and technical foundations of a data product
- `CLMS_Template_PUM.qmd` - Product User Manual, for how users access
  and interpret a product

Once you’ve chosen:

1.  Copy the template into `DOCS/` (not sure what that looks like? See
    [Folder and File Structure](#folder-and-file-structure))

2.  Rename it using this pattern:
    `CLMS_<Product-Name>_<Document-Type>_v<Major-Version>.qmd`

    For example: `CLMS_HRL-Forest_PUM_v1.qmd`

    Use hyphens within the product name, not underscores. Start every
    new document at `_v1`. The document type is either `ATBD` or `PUM`.

3.  Create a matching `-media/` folder for images:
    `CLMS_HRL-Forest_PUM_v1-media/`

4.  Edit in place, following the structure the template provides

The templates include a pre-filled YAML header, required sections, and
commented guidance throughout. Try to keep the structure intact - it
makes a real difference to how consistently documents behave across the
library.

## From scratch

If neither template fits, create a new `.qmd` file directly in `DOCS/`,
following the same naming pattern, create a matching `-media/` folder,
and add the required YAML header manually (see [The YAML
Header](#the-yaml-header)).

> [!TIP]
>
> Templates save time even when they don’t feel like an exact fit - the
> YAML header and section structure are the main things you’d otherwise
> need to set up manually.

## Migrating an existing document

Migrate when you already have substantial content in an existing `.qmd`
file; start from a template when you don’t. An existing `.qmd` can be
dropped into the library as-is, but it needs to be adapted first.

1.  **Copy.** Place the existing `.qmd` in `DOCS/<product>/` and rename
    it with the pattern above, e.g. `CLMS_HRL-Forest_PUM_v1.qmd`.

2.  **Trim the YAML header** down to `title`, `subtitle`, `category`,
    and `date` if needed.

3.  **Move the images** into the sibling `<document-name>-media/` folder
    and make every reference relative. Check that the file extension
    case matches what is on disk: a `.PNG` referenced as `.png` renders
    locally but breaks the published build.

4.  **Verify** with a local render and the frontmatter check before
    publishing:

    ``` bash
    quarto render DOCS/<product>/<document>_v1.qmd
    python3 .github/scripts/validate_qmd_files.py
    ```

# The YAML Header

If you copied a template, the header is pre-filled - just update
`title`, `subtitle`, and `date`.

## Required fields

``` yaml
---
title: HRL Forest
subtitle: Copernis Land Monitoring Service
category: products
date: "2026-01-27"
---
```

- `title` - short product name, appears as the document title
- `subtitle` - Copernis Land Monitoring Service
- `category` - one of `products`, `guidelines`, `reports`,
  `uncategorized`, `non-browsable`
- `date` - publication or last-updated date in ISO format
  e.g. ‘2026-05-26’

## Optional fields

- `type` - how the document is built. Leave it out for ordinary
  documents. Set `type: dashboard` for an interactive page: it renders
  to HTML only - no PDF, no table of contents, no version or changelog.
  New types are added by a Technical Library owner.
- `product-name` - used internally for metadata and indexing
- `template-version` - records which template version was used as the
  starting point. Set automatically when copying a template; don’t edit
  it manually.

## System-managed fields

Leave these out of your YAML header entirely - the publishing system
handles them:

- `keywords` - AI-generated at publish time based on document content.
  Anything you add gets overwritten.
- `version` - carried by the filename suffix, not the YAML. No version
  field belongs in the header.

# Writing Content

Markdown basics - headings, lists, links, images, tables, equations,
footnotes, diagrams - are covered in the [Quarto Markdown
guide](https://quarto.org/docs/authoring/markdown-basics.html). This
chapter covers only what’s specific to this system.

## Image folder convention

Images go in `<your-document-name>-media/`, referenced with relative
paths:

``` markdown
![Processing workflow](CLMS_HRL-Forest_PUM_v2-media/workflow.png)
```

## Page breaks

Use the Quarto shortcode to insert a page break in PDF output:

``` markdown
{{< pagebreak >}}
```

Note that `---` renders as a horizontal rule, not a page break.

## Complex table layouts

For tables with merged cells, nested content, or custom styling, use
HTML tables directly in your `.qmd` file. Both the HTML output and
Typst-rendered PDF handle them well.

Standard Markdown tables have limited formatting options. HTML tables
let you control exactly how things look - column widths, cell colours,
text alignment, borders - using inline CSS:

```` markdown
```{=html}
<table style="width: 100%; border-collapse: collapse;">
  <thead>
    <tr style="background-color: #2c3e50; color: white;">
      <th colspan="2" style="padding: 10px; text-align: center;">Product Overview</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="padding: 8px; border: 1px solid #ccc; font-weight: bold;">HRL Forest</td>
      <td style="padding: 8px; border: 1px solid #ccc;">Active</td>
    </tr>
    <tr style="background-color: #f2f2f2;">
      <td style="padding: 8px; border: 1px solid #ccc; font-weight: bold;">Water Bodies</td>
      <td style="padding: 8px; border: 1px solid #ccc;">Active</td>
    </tr>
  </tbody>
</table>
```
````

# Editing and Previewing Locally

## Open the project in RStudio

1.  Open RStudio
2.  **File \> Open Project…** and select the root folder of your project
3.  Navigate to `DOCS/` and open the `.qmd` file you want to edit

## Preview your document

Click the **Render** button at the top of the editor pane to render HTML
or PDF:

<img src="guidelines_editor-manual_v1-media/rstudio-render.png"
data-fig-align="center"
data-fig-alt="A screenshot of a software interface toolbar, likely from RStudio, for editing a file named `hello.qmd`. The toolbar contains various options including navigation arrows, a save icon, and a checkbox labelled &#39;Render on Save&#39;. The central part of the toolbar features a &#39;Render&#39; button, visually highlighted with a purple outline, depicted with an icon of two blue arrows pointing right. To the right of the &#39;Render&#39; button are a gear icon (settings) and a dropdown arrow. Further right, a &#39;Run&#39; button with a green arrow is visible, along with a refresh/loop icon. Below the main toolbar, two tabs are visible: &#39;Source&#39; and &#39;Visual&#39;, with &#39;Visual&#39; currently selected. Additional text formatting and editing options are also present, such as bold, italic, code, &#39;Normal&#39; dropdown, list icons, image insertion icon, &#39;Format&#39; dropdown, &#39;Insert&#39; dropdown, &#39;Table&#39; dropdown, and an &#39;Outline&#39; option." />

A screenshot of a software interface toolbar, likely from RStudio, for
editing a file named `hello.qmd`. The toolbar contains various options
including navigation arrows, a save icon, and a checkbox labelled
“Render on Save”. The central part of the toolbar features a “Render”
button, visually highlighted with a purple outline, depicted with an
icon of two blue arrows pointing right. To the right of the “Render”
button are a gear icon (settings) and a dropdown arrow. Further right, a
“Run” button with a green arrow is visible, along with a refresh/loop
icon. Below the main toolbar, two tabs are visible: “Source” and
“Visual”, with “Visual” currently selected. Additional text formatting
and editing options are also present, such as bold, italic, code,
“Normal” dropdown, list icons, image insertion icon, “Format” dropdown,
“Insert” dropdown, “Table” dropdown, and an “Outline” option.

Or enable **Preview on Save** in the toolbar to re-render on every save:

<img src="guidelines_editor-manual_v1-media/rstudio-render-on-save.png"
data-fig-align="center"
data-fig-alt="A screenshot of the RStudio integrated development environment&#39;s toolbar when editing a Quarto (.qmd) file. The document tab displays &#39;hello.qmd&#39;. The main toolbar shows various icons including navigation arrows, a save icon, and a checkbox labeled &#39;Render on Save&#39;, which is highlighted by a purple oval. Following &#39;Render on Save&#39;, there are icons for spelling/grammar check (ABC with green checkmark), search (magnifying glass), and a &#39;Render&#39; button (blue arrow icon). To the right are a settings gear icon, a dropdown arrow, an &#39;Insert Chunk&#39; icon (green C), an upload/download arrow pair, a &#39;Run&#39; button with a green arrow, and a refresh/sync icon. Below this, there are two tabs for editing modes: &#39;Source&#39; and &#39;Visual&#39; (currently active). Further below is a standard text formatting toolbar with options for bold, italic, code, text style (Normal), list types, image insertion, and dropdowns for Format, Insert, Table, and Outline." />

A screenshot of the RStudio integrated development environment’s toolbar
when editing a Quarto (.qmd) file. The document tab displays
“hello.qmd”. The main toolbar shows various icons including navigation
arrows, a save icon, and a checkbox labeled “Render on Save”, which is
highlighted by a purple oval. Following “Render on Save”, there are
icons for spelling/grammar check (ABC with green checkmark), search
(magnifying glass), and a “Render” button (blue arrow icon). To the
right are a settings gear icon, a dropdown arrow, an “Insert Chunk” icon
(green C), an upload/download arrow pair, a “Run” button with a green
arrow, and a refresh/sync icon. Below this, there are two tabs for
editing modes: “Source” and “Visual” (currently active). Further below
is a standard text formatting toolbar with options for bold, italic,
code, text style (Normal), list types, image insertion, and dropdowns
for Format, Insert, Table, and Outline.

The rendered output appears in the **Viewer** tab in the lower-right
pane:

<img
src="guidelines_editor-manual_v1-media/rstudio-render-viewer-tab.png"
data-fig-align="center"
data-fig-alt="A screenshot of the RStudio Integrated Development Environment (IDE) menu bar and toolbar, showing options relevant to documentation rendering. The menu bar displays the following tabs: &#39;Files&#39;, &#39;Plots&#39;, &#39;Packages&#39;, &#39;Help&#39;, &#39;Viewer&#39;, and &#39;Presentation&#39;. The &#39;Viewer&#39; tab is prominently highlighted by a thick purple oval outline. Below the menu bar, the toolbar includes navigation arrows (left, right), an icon with a red &#39;X&#39; (likely close or stop), a blank document icon, an &#39;Edit&#39; button accompanied by a pencil icon, and a &#39;Sync Editor&#39; checkbox. On the right side of the toolbar, a &#39;Publish&#39; button with a blue circular arrows icon is visible, along with a dropdown arrow and a refresh icon. In the top right corner, there are two window management icons." />

A screenshot of the RStudio Integrated Development Environment (IDE)
menu bar and toolbar, showing options relevant to documentation
rendering. The menu bar displays the following tabs: “Files”, “Plots”,
“Packages”, “Help”, “Viewer”, and “Presentation”. The “Viewer” tab is
prominently highlighted by a thick purple oval outline. Below the menu
bar, the toolbar includes navigation arrows (left, right), an icon with
a red ‘X’ (likely close or stop), a blank document icon, an “Edit”
button accompanied by a pencil icon, and a “Sync Editor” checkbox. On
the right side of the toolbar, a “Publish” button with a blue circular
arrows icon is visible, along with a dropdown arrow and a refresh icon.
In the top right corner, there are two window management icons.

If the Viewer tab isn’t showing rendered output, go to **Tools \> Global
Options \> R Markdown** and set **Show output preview in** to **Viewer
Pane**:

<img
src="guidelines_editor-manual_v1-media/rstudio-render-viewer-options.png"
data-fig-align="center"
data-fig-alt="This image is a screenshot of the &#39;Options&#39; dialog within the RStudio Integrated Development Environment (IDE), displaying settings for R Markdown. On the left navigation panel, &#39;R Markdown&#39; is selected. The main pane has four tabs: &#39;Basic&#39; (currently active), &#39;Advanced&#39;, &#39;Visual&#39;, and &#39;Citations&#39;. Under the &#39;Basic&#39; tab for &#39;R Markdown&#39; settings, the following options are visible: &#39;Show document outline by default&#39; (unchecked), &#39;Soft-wrap R Markdown files&#39; (checked), and &#39;Show in document outline:&#39; (dropdown set to &#39;Sections Only&#39;). A key setting, &#39;Show output preview in:&#39;, is highlighted with a purple border, and its dropdown is set to &#39;Viewer Pane&#39;. Below this, &#39;Show output inline for all R Markdown documents&#39; is checked, &#39;Show equation and image previews:&#39; is set to &#39;Inline&#39;, and &#39;Evaluate chunks in directory:&#39; is set to &#39;Document&#39;."
height="300" />

This image is a screenshot of the “Options” dialog within the RStudio
Integrated Development Environment (IDE), displaying settings for R
Markdown. On the left navigation panel, “R Markdown” is selected. The
main pane has four tabs: “Basic” (currently active), “Advanced”,
“Visual”, and “Citations”. Under the “Basic” tab for “R Markdown”
settings, the following options are visible: “Show document outline by
default” (unchecked), “Soft-wrap R Markdown files” (checked), and “Show
in document outline:” (dropdown set to “Sections Only”). A key setting,
“Show output preview in:”, is highlighted with a purple border, and its
dropdown is set to “Viewer Pane”. Below this, “Show output inline for
all R Markdown documents” is checked, “Show equation and image
previews:” is set to “Inline”, and “Evaluate chunks in directory:” is
set to “Document”.

## Render the full project

To render all documents and preview the complete library locally:

``` bash
git docs-preview
```

> [!TIP]
>
> The repository ships with the project config renamed to
> `_quarto-not-used.yaml` so RStudio operates in single-file mode by
> default - faster for day-to-day editing. When you need to render the
> full project, rename it to `_quarto.yaml`, run `quarto render`, then
> rename it back.

# Publishing to Develop

``` bash
git add DOCS/
git commit -m "docs: update [brief description]"
git docs-publish
```

After the pipeline runs, check your document at:
<https://eea.github.io/CLMS_documents/develop/index.html>

Navigation, cross-links, and the sidebar TOC can behave differently than
in your local RStudio preview - worth a quick look before calling it
done.

# Folder and File Structure

``` text
DOCS/
├── _meta/                            # Scripts, config, metadata - do not edit
├── includes/                         # Quarto include files - do not edit
├── templates/                        # Document templates - do not edit
├── theme/                            # Styling definitions - do not edit
├── _quarto.yml                       # Project-wide Quarto config
├── CLMS_HRL-Forest_PUM_v2.qmd
├── CLMS_HRL-Forest_PUM_v2-media/
├── CLMS_Water-Bodies_ATBD_v1.qmd
├── CLMS_Water-Bodies_ATBD_v1-media/
└── ...
```

Your work lives in `DOCS/` directly: one `.qmd` file per document, plus
a matching `-media/` folder for images and diagrams. The four managed
subdirectories (`_meta/`, `includes/`, `templates/`, `theme/`) are
updated centrally - don’t edit them.

# File Naming, Versioning, and Changelog

## The version suffix

The `_v<N>` suffix in the filename is the major version - the only
version number you control. Minor and patch versions are assigned
automatically by AI at library release time based on the scope of
changes: small corrections get a patch bump (`2.3.5 → 2.3.6`), new or
revised sections get a minor bump (`2.3.0 → 2.4.0`). A new file
`CLMS_HRL-Forest_PUM_v3.qmd` starts at `3.0.0` at its first release. You
never set a version number in YAML.

Version numbers are assigned only when your changes reach `main`,
i.e. at the public release. Publishing to `develop`, or promoting to
`test`, assigns nothing - the document keeps its previous version until
the release build runs.

## When to create a new major version

Most changes are an edit to the existing file - the system bumps the
minor or patch version for you. Create a new `_v<N>` file only when the
**old version has to stay available exactly as it is**, for example when
you:

- work on a new product release
- need the earlier release to keep being citable as a stable reference

Creating one is a fork, not an update. Copy the file and its media
folder, and from that point the two documents are independent: separate
version numbers, separate change logs, and no link between them.

``` bash
cp DOCS/CLMS_HRL-Forest_PUM_v2.qmd DOCS/CLMS_HRL-Forest_PUM_v3.qmd
cp -r DOCS/CLMS_HRL-Forest_PUM_v2-media DOCS/CLMS_HRL-Forest_PUM_v3-media
```

The copied filename must carry the new major version (`_v3` above); the
new document then starts at `N.0.0` at its first release, while the old
one keeps its own history.

## Don’t rename after publishing

The filename becomes part of the document’s URL. Renaming breaks links
and cross-references. If a significant revision is needed, create a new
major version rather than renaming.

## The change log

You don’t write the change log. The system generates it at release time
and appends a **Change Log** section to the end of your document - a
table of date, version, and summary entries:

| Date | Version | Summary |
|----|----|----|
| 2026-11-06 | 2.1.0 | Reworded the coverage section and corrected the tile table |
| 2026-07-24 | 2.0.0 | First published version |

At each release - that is, when a change reaches `main`, in the same
step that assigns the version number - the pipeline compares the
document against its last release and writes a short summary of what
changed, storing the entry under the new version. A document with no
previous release gets an initial entry instead.

The stored history is what the library build renders, newest entry
first, as the **Change Log** section appended after your content.
Because it comes from stored history rather than the current diff, it
shows up in every built version of the page (`develop`, `test` and
`main` alike) - you just won’t see your own change there until it has
been released. At most the last 20 entries are kept.

What this means in practice:

- **Nothing to add to the source.** There is no `changelog` field and no
  section to maintain.
- **Write descriptive commits.** The summary is derived from the diff,
  so focused changes produce a clearer entry.
- **It’s absent from your local preview.** `quarto render` doesn’t run
  the library build, so the section only appears on a built page. This
  document has one too - see its [Change Log](#change-log) at the end of
  the published page.
- **Some documents have none.** Interactive pages (`type: dashboard`)
  opt out of the change log. Leave `type` unset unless the document
  really is one.

# Restoring Previous Versions

Restore pulls a published version of a document into your local working
copy. It doesn’t roll back the library - think of it as “pick up from
version X,” not “undo to version X.”

## Commands

``` bash
git docs-restore --list-all                                 # all published documents
git docs-restore --list DOCS/CLMS_HRL-Forest_PUM_v2.qmd     # versions of one file
git docs-restore DOCS/CLMS_HRL-Forest_PUM_v2.qmd 2.0.0      # specific version
git docs-restore --latest DOCS/CLMS_HRL-Forest_PUM_v2.qmd   # latest published version
```

## When to use it

**Recover deleted content.** You removed a section locally and need it
back. Restore the last published version, copy out what you need, then
carry on with your current version.

**Something went wrong in a recent edit.** Restore an earlier version
(e.g. `2.1.0`) and work forward from there rather than trying to
untangle the current state.

**Resurrect a deleted file.** If a file was removed from the project but
still exists in the library history, `--list-all` will find it. Restore
brings it back into `DOCS/` as if nothing happened.

# Release Path

Once you publish to `develop`, the rest of the process belongs to
Technical Library owners. Getting from develop to public requires two
separate pull requests, each reviewed and approved by a second owner
before it merges.

| Stage         | URL                                                       |
|---------------|-----------------------------------------------------------|
| develop       | <https://eea.github.io/CLMS_documents/develop/index.html> |
| test          | <https://eea.github.io/CLMS_documents/test/index.html>    |
| main (public) | <https://library.land.copernicus.eu>                      |

At each release, the system assigns version numbers automatically based
on what changed.
