# Setup Guide
European Environment Agency (EEA)
2026-06-03

- [<span class="toc-section-number">1</span> What This Sets
  Up](#what-this-sets-up)
- [<span class="toc-section-number">2</span>
  Prerequisites](#prerequisites)
- [<span class="toc-section-number">3</span> Integration
  Steps](#integration-steps)
  - [<span class="toc-section-number">3.1</span> 1. Add the base
    documentation repository as a
    remote](#1-add-the-base-documentation-repository-as-a-remote)
  - [<span class="toc-section-number">3.2</span> 2. Pull in the `DOCS/`
    folder as a subtree](#2-pull-in-the-docs-folder-as-a-subtree)
  - [<span class="toc-section-number">3.3</span> 3. Configure the Git
    aliases](#3-configure-the-git-aliases)
- [<span class="toc-section-number">4</span> Verify the
  Setup](#verify-the-setup)
- [<span class="toc-section-number">5</span> Handoff
  Checklist](#handoff-checklist)

# What This Sets Up

Running through this guide integrates an existing project repository
with the CLMS Technical Library. The result is:

- a `DOCS/` directory in the project repo, linked to the central library
  as a git subtree
- a set of Git aliases (`git docs-publish`, `git docs-update`,
  `git docs-preview`, `git docs-restore`) for day-to-day documentation
  workflow

Once done, editors can follow the Editor Guide to create and publish
documents. Your work here is a one-time setup.

# Prerequisites

**For this setup**, you only need Git installed and access to the
project repository.

**Editors will also need** the following on their machines - not your
responsibility to install, but useful to pass along:

| Tool | Purpose | Download |
|----|----|----|
| RStudio | Writing and previewing `.qmd` files | [posit.co](https://posit.co/download/rstudio-desktop/) |
| Quarto | Document rendering engine | [quarto.org](https://quarto.org/docs/get-started/) |

Pandoc is bundled with both RStudio and Quarto - editors don’t need to
install it separately.

# Integration Steps

Run these commands from the root of the existing project repository.

## 1. Add the base documentation repository as a remote

``` bash
git remote add clms-docs-base git@github.com:eea/CLMS_documents_base.git
```

## 2. Pull in the `DOCS/` folder as a subtree

``` bash
git subtree add --prefix=DOCS clms-docs-base main --squash
```

This creates the `DOCS/` directory and commits it into the project
repository.

## 3. Configure the Git aliases

Run the setup script for your operating system:

``` bash
# macOS or Linux
./DOCS/_meta/scripts/linux/setup-docs-aliases.sh

# Windows (PowerShell)
./DOCS/_meta/scripts/win/setup-docs-aliases.ps1
```

This registers four Git aliases for the project:

| Alias | What it does |
|----|----|
| `git docs-update` | Pulls updates from the central base repository into `DOCS/` |
| `git docs-publish` | Pushes local documentation changes to the Technical Library |
| `git docs-preview` | Renders the full project locally, including PDF output |
| `git docs-restore` | Fetches a published version of a document into the local working copy |

# Verify the Setup

> [!NOTE]
>
> **TODO:** A verification script is planned for this step. This section
> will be updated once the script is ready. In the meantime, use the
> manual checks below as a placeholder.

Confirm the following before handing off to editors:

- [ ] `DOCS/` exists at the project root with `templates/`, `_meta/`,
  `theme/`, and `includes/` inside
- [ ] `git remote -v` lists `clms-docs-base` as a remote
- [ ] `git docs-publish --help` (or equivalent) responds without an
  error

# Handoff Checklist

Before passing to editors, confirm:

- [ ] All three integration steps completed without errors
- [ ] Verification checks above pass
- [ ] Editors have the Editor Guide link: [Editor
  Guide](guidelines_editor-manual_v1.html)
- [ ] Editors know they need RStudio and Quarto on their machines (see
  [Prerequisites](#prerequisites))

The editors’ starting point is the Editor Guide. They don’t need to
touch anything set up here.
