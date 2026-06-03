#!/bin/bash
set -e

# Patterns to filter out from Quarto output
QUARTO_NOISE=(
  -e "Unknown meta key .* specified in a metadata Shortcode"
  -e "^Output created:"
)

quarto_render() {
  quarto render "$@" 2>&1 | grep --line-buffered -v "${QUARTO_NOISE[@]}" || true
}

echo "[1/10] Copying DOCS to origin_DOCS..."
mv DOCS origin_DOCS

echo "[2/10] Updating URL mappings and grouping documents by category..."
python3 .github/scripts/build/update_url_mappings.py &
python3 .github/scripts/build/group_docs_by_category.py &
wait

# Restore Quarto render cache into the freshly created DOCS/ directory
if [[ -d ../.quarto-cache ]]; then
  echo "\t Restoring Quarto render cache..."
  cp -r ../.quarto-cache DOCS/.quarto
fi

# Change to DOCS directory as it'll be the root of rendered content
cd DOCS

# Copy quarto configuration and meta files from _meta to DOCS
cp ../_meta/_quarto*.yml .
cp -r ../_meta .

# Link assets to origin_DOCS as these files need to be served from rendered content
ln -s ../assets assets

# Clean the build copy's YAML frontmatter (origin_DOCS/ is untouched).
echo "Stripping unknown frontmatter fields..."
python3 ../.github/scripts/build/strip_unknown_frontmatter.py .

if [[ -n "$GENERATE_DOCX" ]]; then
  echo "[3/10] Rendering all documents to HTML..."
else
  echo "3/10] Rendering all documents to HTML (DOCX skipped)...   "
fi
#sudo cp /usr/bin/chromium /usr/bin/chromium-browser

# Set up quarto configuration based on environment variables
if [[ -n "$GENERATE_DOCX" ]]; then
  echo -e "\t Using default configuration (HTML + DOCX files kept)"
  # _quarto.yml is already the default with headers - no copying needed
else
  echo -e "\t Using configuration for DOCX cleanup (HTML only)"
  cp _quarto-no-headers.yml _quarto.yml
fi

# Render all files together (changelog filter uses original-filename from YAML headers)
echo "[4/10] Rendering all documents to HTML..."
quarto_render --to html --no-clean

# Backup the correct sitemap and llms.txt as they may be overwritten by next operations
sleep 5
mv _site/sitemap.xml _site/sitemap.xml.bkp
mv _site/llms.txt _site/llms.txt.bkp

# Generate DOCX files (always needed for PDF conversion)
echo "[5/10] Generating DOCX files for PDF conversion..."
quarto_render --to docx --no-clean
find _site -type f -name 'index.docx' -delete

# ============================================================================
# Pre-LO Python fixes — must run BEFORE LibreOffice opens the docx.
# ============================================================================

# Quarto emits each figure caption with two consecutive <w:pPr> elements in the
# same paragraph (invalid OpenXML). LibreOffice mis-renders such captions
# (duplicate caption with mismatched styles when the figure straddles a page
# break). Strip the duplicate pPr before LO opens the doc.
echo "      [Pre-LO] Fixing duplicate <w:pPr> in caption paragraphs..."
python3 ../.github/scripts/build/fix_docx_caption_pprs.py --dir _site

# Quarto 1.9 strips the title-section spacer paragraphs the template uses to
# push the TOC onto its own page. LO's pageBreakBefore is unreliable on
# near-start-of-section paragraphs; we inject an explicit inline page break
# in the title-section date paragraph so TOC starts on page 2.
echo "      [Pre-LO] Inserting page break between title section and TOC..."
python3 ../.github/scripts/build/fix_docx_title_pagebreak.py --dir _site

# ============================================================================
# LO pass 1 — TOC refresh, image-fit, code-block boxify, save .docx (no PDF).
# Things that genuinely need LibreOffice's runtime layout engine.
# ============================================================================
echo "      [LO #1] Refreshing TOC + runtime fixups (UpdateAndSave)..."
if ! timeout 20m ../.github/scripts/build/convert_docx_to_pdf.sh --mode=update 2>&1 | tee conversion-update.log; then
  exit_code=$?
  echo " ❌ LO pass 1 (UpdateAndSave) failed with exit code: $exit_code"
  tail -30 conversion-update.log
  exit $exit_code
fi

# ============================================================================
# Post-LO Python fixes — pure XML mutations applied to the LO-saved .docx.
# These can be reordered freely; they don't depend on each other.
# ============================================================================

# Quarto wraps each figure (image + caption) in a <w:tbl>; the template's
# Table style has a visible border. Strip borders inline on figure-wrapping
# tables only; real content tables keep their template borders.
echo "      [Post-LO] Stripping borders from figure-wrapping tables..."
python3 ../.github/scripts/build/fix_docx_figure_table_borders.py --dir _site

# Templates set <w:u w:val="none"/> on the Hyperlink style so all links come
# out un-underlined. We want external URLs to keep their underline as a visual
# clickability signal. Walk <w:hyperlink r:id="..."> and inject inline
# <w:u w:val="single"/> on their runs; w:anchor links are untouched.
echo "      [Post-LO] Restoring underline on external URL hyperlinks..."
python3 ../.github/scripts/build/fix_docx_link_underlines.py --dir _site

# When a content table spans pages, mark its first row as a repeating header
# and forbid rows from splitting across page breaks.
echo "      [Post-LO] Fixing table pagination (header repeat + cantSplit)..."
python3 ../.github/scripts/build/fix_docx_table_pagination.py --dir _site

# Body tables stretched to 100% of column width with widths redistributed
# proportionally to per-column content length. Image columns locked.
echo "      [Post-LO] Fitting table widths + redistributing column widths..."
python3 ../.github/scripts/build/fix_docx_table_widths.py --dir _site

# Tighten bullet/numbered list indents in word/numbering.xml (each level at
# (ilvl+1)*360 twips left + 360 hanging).
echo "      [Post-LO] Tightening bullet/numbered list indents..."
python3 ../.github/scripts/build/fix_docx_list_indents.py --dir _site

# Inject U+200B zero-width spaces at natural break points inside long URLs
# so LibreOffice's wrapping engine breaks them cleanly. Display only —
# <w:hyperlink r:id> targets are untouched.
echo "      [Post-LO] Inserting zero-width-space break points in long URLs..."
python3 ../.github/scripts/build/fix_docx_url_breaks.py --dir _site

# Populate docx <dc:subject> from each qmd's `subtitle:` frontmatter so the
# PDF's Subject metadata field is non-empty.
echo "      [Post-LO] Populating docx <dc:subject> from qmd subtitle..."
python3 ../.github/scripts/build/fix_docx_metadata.py --dir _site

# Fade header/footer brand PNGs to 55% alpha so the EU/Copernicus/EEA logos
# render as light watermarks. Post-LO because LO strips DrawingML alpha and
# duplicates shared media on save (cover-page logo lands in a fresh image
# file the pre-LO template fade misses).
echo "      [Post-LO] Fading header/footer brand PNGs to 55% alpha..."
python3 ../.github/scripts/build/fix_docx_header_footer_opacity.py --dir _site

# Normalise every table's cell padding to 108 twips (5pt) on all four sides.
# Quarto bakes asymmetric padding (0pt top/bottom, 5pt left/right) into
# every table's inline tblCellMar — visually cramped for image cells next
# to text cells in the same row.
echo "      [Post-LO] Normalising table cell padding to 108/108/108/108..."
python3 ../.github/scripts/build/fix_docx_table_cell_padding.py --dir _site

echo "[6/10] Generating index.qmd files for all DOCS/* folders..."
node ../.github/scripts/build/generate_index_all.mjs

echo "[7/10] Rendering index.qmd files..."
mv _quarto.yml _quarto_not_used.yml
mv _quarto-index.yml _quarto.yml
#index_count=$(find ./ -type f -name index.qmd | wc -l)
#echo "   Rendering $index_count index files (parallel, 4 workers)..."
find ./ -type f -name index.qmd -print0 | \
  xargs -0 -P4 -I{} \
  bash -c "quarto render '{}' --profile index --to html --no-clean --quiet $QUARTO_FLAGS 2>&1 | grep -v -e 'Unknown meta key .* specified in a metadata Shortcode' -e '^Output created:' || true"
mv _quarto.yml _quarto-index.yml
cp _quarto_not_used.yml _quarto.yml && rm _quarto_not_used.yml

echo "[8/10] Exporting DOCX files to PDF (LO pass 2)..."

# Full conversion with detailed error reporting
echo "     Starting PDF export (timeout: 20m)..."
if ! timeout 20m ../.github/scripts/build/convert_docx_to_pdf.sh --mode=pdf 2>&1 | tee conversion.log; then
  exit_code=$?
  echo " ❌ PDF export failed with exit code: $exit_code"
  echo "   Last 30 lines of output:"
  tail -30 conversion.log
  echo "   DOCX files present:"
  find _site -name "*.docx" -type f | head -10
  exit $exit_code
fi

#echo "✅ PDF conversion completed successfully"
#pdf_count=$(find _site -name "*.pdf" -type f | wc -l)
#echo "   Generated $pdf_count PDF files"

# Clean up DOCX files unless explicitly requested to keep them
if [[ -n "$GENERATE_DOCX" ]]; then
  echo "     Keeping DOCX files for download/access"
else
  echo "[9/10] Cleaning up DOCX files..."
  find _site -name "*.docx" -type f -delete
  #echo "   ✅ DOCX files removed to save space"
fi

# Revert the correct sitemap and llms.txt
cp _site/sitemap.xml.bkp _site/sitemap.xml
rm -f _site/sitemap.xml.bkp
mv _site/llms.txt.bkp _site/llms.txt

# Remove non-browsable links from sitemap.xml and llms.txt
python3 ../.github/scripts/build/remove_non_browsable.py _site/sitemap.xml
python3 ../.github/scripts/build/remove_non_browsable.py --format llms _site/llms.txt

# Generate the LLM-oriented sitemap (loc entries point to *.llms.md companions)
python3 ../.github/scripts/build/generate_llm_sitemap.py _site/sitemap.xml _site/sitemap-llm.xml

# Advertise the LLM sitemap in robots.txt (Quarto-generated file only lists sitemap.xml)
echo "Sitemap: https://library.land.copernicus.eu/sitemap-llm.xml" >> _site/robots.txt

echo "[10/10] Cleaning up..."
find _site -type f -name '*.qmd' -delete

cp ../404.html _site/404.html
cp ../redirect_map.json _site/redirect_map.json
cp ../url_mapping.json _site/url_mapping.json


# Save Quarto render cache from DOCS/ back to workspace root for next run
if [[ -d .quarto ]]; then
  echo "     Saving Quarto render cache..."
  rm -rf ../.quarto-cache
  cp -r .quarto ../.quarto-cache
fi

echo "✅ Docs built successfully"