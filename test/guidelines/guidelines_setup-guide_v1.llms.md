# Setup Guide

Copernicus Land Monitoring Service - Technical Library

This guide outlines the essential steps for integrating an existing project repository with the Copernicus Land Monitoring Service (CLMS) Technical Library. It details the technical process of establishing a `DOCS/` directory within the project, linking it to the central library via a Git subtree, and configuring bespoke Git aliases. The document ensures that project repositories are properly set up for seamless documentation contribution, allowing editors to subsequently utilise the CLMS documentation workflow for authoring and publishing scientific and technical materials.

Author

European Environment Agency (EEA)

Published

May 26, 2026

Keywords

CLMS Technical Library, Project repository integration, Git subtree configuration, Git aliases setup, Documentation workflow, Quarto prerequisites, RStudio prerequisites, Technical documentation setup, Version control integration

  
**Contact:**

European Environment Agency (EEA)  
Kongens Nytorv 6  
1050 Copenhagen K  
Denmark  
[**https://land.copernicus.eu/**](https://land.copernicus.eu/)

# 1 What This Sets Up

Running through this guide integrates an existing project repository with the CLMS Technical Library. The result is:

- a `DOCS/` directory in the project repo, linked to the central library as a git subtree
- a set of Git aliases (`git docs-publish`, `git docs-update`, `git docs-preview`, `git docs-restore`) for day-to-day documentation workflow

Once done, editors can follow the Editor Guide to create and publish documents. Your work here is a one-time setup.

# 2 Prerequisites

**For this setup**, you only need Git installed and access to the project repository.

**Editors will also need** the following on their machines - not your responsibility to install, but useful to pass along:

| Tool | Purpose | Download |
|----|----|----|
| RStudio | Writing and previewing `.qmd` files | [posit.co](https://posit.co/download/rstudio-desktop/) |
| Quarto | Document rendering engine | [quarto.org](https://quarto.org/docs/get-started/) |

Pandoc is bundled with both RStudio and Quarto - editors don’t need to install it separately.

# 3 Integration Steps

Run these commands from the root of the existing project repository.

## 3.1 1. Add the base documentation repository as a remote

``` bash
git remote add clms-docs-base git@github.com:eea/CLMS_documents_base.git
```

## 3.2 2. Pull in the `DOCS/` folder as a subtree

``` bash
git subtree add --prefix=DOCS clms-docs-base main --squash
```

This creates the `DOCS/` directory and commits it into the project repository.

## 3.3 3. Configure the Git aliases

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

# 4 Verify the Setup

> **NOTE:**
>
> **TODO:** A verification script is planned for this step. This section will be updated once the script is ready. In the meantime, use the manual checks below as a placeholder.

Confirm the following before handing off to editors:

`DOCS/` exists at the project root with `templates/`, `_meta/`, `theme/`, and `includes/` inside

`git remote -v` lists `clms-docs-base` as a remote

`git docs-publish --help` (or equivalent) responds without an error

# 5 Handoff Checklist

Before passing to editors, confirm:

All three integration steps completed without errors

Verification checks above pass

Editors have the Editor Guide link: [Editor Guide](guidelines_editor-manual_v1.llms.md)

Editors know they need RStudio and Quarto on their machines (see [Prerequisites](#prerequisites))

The editors’ starting point is the Editor Guide. They don’t need to touch anything set up here.

# 6 Change Log

| Date | Version | Summary |
|----|----|----|
| 2026-06-03 | 1.1.0 | Added a new 'Setup Guide' document detailing the integration process for existing project repositories with the CLMS Technical Library. This includes instructions for adding the documentation repository as a Git subtree and configuring essential Git aliases for the documentation workflow. |

Back to top

## Reuse

EUPL (\>= 1.2)
