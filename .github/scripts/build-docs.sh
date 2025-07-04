#!/bin/bash
set -e

echo "🖼 Render all documents into to HTML/DOCX"
sudo cp /usr/bin/chromium /usr/bin/chromium-browser
QUARTO_CHROMIUM_HEADLESS_MODE=new quarto render --to docx 
find _site -type f -name 'index.docx' -delete
QUARTO_CHROMIUM_HEADLESS_MODE=new quarto render --to html --no-clean

# Backup the correct sitemap as it may be overwritten by next operations
sleep 5
mv _site/sitemap.xml _site/sitemap.xml.bkp

echo "🛠 Generate index.qmd files for all DOCS/* folders"e
node .github/scripts/generate_index_all.mjs

echo "📄 Render only index.qmd files using 'index' profile"
mv _quarto.yml _quarto_not_used.yml
mv _quarto-index.yml _quarto.yml
find DOCS -type f -name index.qmd -print0 | while IFS= read -r -d '' src; do
  echo "🔧 Rendering $src using profile=index..."
  QUARTO_CHROMIUM_HEADLESS_MODE=new quarto render "$src" --profile index --to html --no-clean
done
mv _quarto.yml _quarto-index.yml
cp _quarto_not_used.yml _quarto.yml && rm _quarto_not_used.yml

echo "🔄 Additional processing of index.html file"
echo '<!DOCTYPE html>
<html>
  <head>
    <meta http-equiv="refresh" content="0; url=DOCS/index.html" />
    <title>Redirecting...</title>
  </head>
  <body>
    <p>If you are not redirected automatically, <a href="DOCS/index.html">click here</a>.</p>
  </body>
</html>' > _site/index.html

# Revert the correct sitemap
cp _site/sitemap.xml.bkp _site/sitemap.xml
rm -f _site/sitemap.xml.bkp

echo "📄 Converting .docx files to .pdf..."
#chmod +x ./convert_docx_to_pdf.sh
timeout 3s .github/scripts/convert_docx_to_pdf.sh || true
timeout 10m .github/scripts/convert_docx_to_pdf.sh

echo "🧹 Cleaning up..."
find _site -type f -name '*.docx' -delete

echo "✅ Docs built successfully"
