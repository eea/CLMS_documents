# 📚 Document Compilation & AI-Open Portal (Quarto Platform)

An enterprise-grade, highly automated, and AI-ready document hosting and compilation stack built on **Quarto**. 

This repository provides a complete, modern CI/CD compiler pipeline designed to transform raw technical documents, product user manuals, and specifications into beautiful, structured, and search-optimized output formats. It is fully modular—**any organization can fork this repository** to immediately establish their own automated online technical library.

---

## 🚀 Core Features

*   **Multi-Format Compilation:** Compiles raw Markdown (`.qmd`) source files into three target outputs in a single pass:
    *   **Responsive Web HTML:** Clean, mobile-friendly design featuring sidebar navigation and search.
    *   **Typst-Engine PDFs:** Gorgeous, publication-quality printable PDF manuals compiled using the ultra-fast Typst layout tool.
    *   **Companion GFM (.llms.md):** Stripped-down, plain-markdown files designed specifically for ingestion by LLM/RAG systems.
*   **LLM/RAG Optimization:** 
    *   *Table Linearization:* A custom Lua-based Pandoc filter parses complex spatial, metadata, and grid-tables into flat text hierarchies that spatial AI models (like Onyx) can retrieve and read without fragmentation.
    *   *AI Vision Image Descriptions:* Automatically extracts image hashes and generates context-rich visual alt-text dynamically, saving on repetitive API consumption using an MD5-hashed cache window (`.llm_cache`).
*   **Privacy & Hiding Layers (Non-Browsable):** Allows documents flagged as `category: non-browsable` to compile using persistent, cryptographically secure 64-character hashes. It purges these files completely from static indices, `robots.txt`, and standard crawling `sitemap.xml` entries, keeping them accessible strictly via direct link.
*   **Automatic Captions & Fixing:** Formats, sanitizes unknown YAML headers, balances table column widths automatically, and promotes loose title markers into formal native figure/table elements.

---

## 📂 Repository Structure

The documentation files are maintained in the following directory layout:

```
├── DOCS/                        # Active compiled content (generated during build)
├── _meta/                       # Quarto configurations, layouts, CSS, and typst styles
├── assets/                      # Global repository logos, icons, and graphic elements
├── tools/
│   └── pdf_to_qmd/              # Batch PDF-to-Quarto conversion utilities
└── .github/
    └── scripts/build/           # The automated build and cleaning scripts
```

---

## 🛠️ Step-by-Step Guide for Forking

This repository is designed to be fully customizable. If you wish to fork this project to host your own technical documents library, follow these steps:

### 1. Structure Your Documents
1. Clean your repository structure and place your Markdown (`.qmd`) document files under `DOCS/`.
2. Give your files a version-controlling suffix (e.g., `My_Manual_v1.qmd`).
3. Set your document metadata by adding a YAML header at the top of each `.qmd` file:
   ```yaml
   ---
   category: products
   date: '2025-01-15'
   subtitle: Your Organization Name
   title: Technical Specification – Product User Manual
   toc: true
   toc-depth: 3
   toc-title: Content
   version: 1.0
   ---
   ```
   `category` can be `products`, `guidelines`, or `non-browsable`.

### 2. Configure Your Brand Assets
*   Go to `assets/` and replace the logo files (`copernicus-logo.svg`, `lms_logo.svg`) with your own organization logos.
*   Open `_meta/` to adjust global theme variables, colors, or page headers/footers in the stylesheet variables (`styles.css` / `main.css`).

### 3. Set Up GitHub Actions
To enable automated updates and web deployment:
1. Enable **GitHub Pages** under your forked repository settings and target the `gh-pages` branch.
2. In your repository Secrets, add:
   *   `GEMINI_API_KEY` (Required if you wish to use the AI-vision description and metadata auto-generation features during deployment).

---

## 💻 Local Compilation & Conversion

### Batch Convert Legacy PDF manuals to QMD
To easily import existing documents, use the bundled converter script:
```bash
python3 -m pip install -r tools/pdf_to_qmd/requirements.txt
python3 tools/pdf_to_qmd/pdf2qmd.py --out Files_to_convert/processed_documents/output Files_to_convert/processed_documents/inbox
```

### Compile Locally
To run and test the complete cleaning, renaming, and compilation sequence locally on your machine, launch the build script:
```bash
./.github/scripts/build/build-docs.sh
```
*Tip: The script safely creates a pristine copy of your working files (`source_DOCS`). You can completely roll back any experimental render states at any time by running:*
```bash
rm -rf DOCS origin_DOCS && mv source_DOCS DOCS
```