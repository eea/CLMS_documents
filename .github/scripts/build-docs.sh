#!/bin/bash
set -e

echo "🔄 Copying DOCS to origin_DOCS..."
mv DOCS origin_DOCS

echo "🔄 Updating URL mappings..."
python3 .github/scripts/update_url_mappings.py

echo "🔄 Grouping documents by category..."
python3 .github/scripts/group_docs_by_category.py

# Change to DOCS directory as it'll be the root of rendered content
cd DOCS
# Link assets to origin_DOCS as these files need to be served from rendered content
ln -s ../assets assets


echo "🖼 Render all documents into to HTML/DOCX"
sudo cp /usr/bin/chromium /usr/bin/chromium-browser
QUARTO_CHROMIUM_HEADLESS_MODE=new quarto render --to html --no-clean

# Backup the correct sitemap as it may be overwritten by next operations
sleep 5
mv _site/sitemap.xml _site/sitemap.xml.bkp

QUARTO_CHROMIUM_HEADLESS_MODE=new quarto render --to docx --no-clean
find _site -type f -name 'index.docx' -delete

echo "🛠 Generate index.qmd files for all DOCS/* folders"e
node ../.github/scripts/generate_index_all.mjs

echo "📄 Render only index.qmd files using 'index' profile"
mv _quarto.yml _quarto_not_used.yml
mv _quarto-index.yml _quarto.yml
find ./ -type f -name index.qmd -print0 | while IFS= read -r -d '' src; do
  echo "🔧 Rendering $src using profile=index..."
  QUARTO_CHROMIUM_HEADLESS_MODE=new quarto render "$src" --profile index --to html --no-clean
done
mv _quarto.yml _quarto-index.yml
cp _quarto_not_used.yml _quarto.yml && rm _quarto_not_used.yml


echo "📄 Converting .docx files to .pdf..."
timeout 3s ../.github/scripts/convert_docx_to_pdf.sh || true
timeout 10m ../.github/scripts/convert_docx_to_pdf.sh

# Revert the correct sitemap
cp _site/sitemap.xml.bkp _site/sitemap.xml
rm -f _site/sitemap.xml.bkp

echo "🧹 Cleaning up..."
find _site -type f -name '*.docx' -delete
find _site -type f -name '*.qmd' -delete

cp ../404.html _site/404.html
cp ../redirect_map.json _site/redirect_map.json
cp ../url_mapping.json _site/url_mapping.json


echo "✅ Docs built successfully"