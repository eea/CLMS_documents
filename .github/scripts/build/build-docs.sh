#!/bin/bash
set -e

# Patterns to filter out from Quarto output
QUARTO_NOISE=(
  -e "Unknown meta key .* specified in a metadata Shortcode"
  -e "^Output created:"
)

quarto_render() {
  # Filter noise from quarto's output, but fail on quarto's OWN exit status —
  # PIPESTATUS[0], not the pipeline's. grep exits 1 when it filters out every
  # line, which is not a render failure; the trailing `|| true` only stops
  # `set -e` tripping on that case, while PIPESTATUS still carries quarto's code.
  quarto render "$@" 2>&1 | grep --line-buffered -v "${QUARTO_NOISE[@]}" || true
  local status=${PIPESTATUS[0]}
  if [ "$status" -ne 0 ]; then
    echo "ERROR: quarto render failed (exit $status): quarto render $*" >&2
    return "$status"
  fi
}

echo "[1/7] Copying DOCS to origin_DOCS..."
mv DOCS origin_DOCS

echo "[2/7] Updating URL mappings and grouping documents by category..."
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

# Render with the no-headers config. The with-headers variant is still on
# disk but nothing activates it anymore.
cp _quarto-no-headers.yml _quarto.yml

echo "[3/7] Rendering all documents to HTML..."
quarto_render --to html --no-clean

# Backup sitemap.xml and llms.txt — they're regenerated when index.qmd files
# are rendered later, and we want to preserve the values from the first render.
sleep 5
mv _site/sitemap.xml _site/sitemap.xml.bkp
mv _site/llms.txt _site/llms.txt.bkp

echo "[4/7] Rendering all documents to PDF (Typst)..."
# Typst format is defined in _meta/includes/default-no-headers.yml (pulled in
# via metadata-files). Template + show partials in _meta/theme/typst/.
quarto_render --to typst --no-clean

echo "[5/7] Generating index.qmd files for all DOCS/* folders..."
python3 ../.github/scripts/build/generate_index_all.py

echo "[6/7] Rendering index.qmd files..."
mv _quarto.yml _quarto_not_used.yml
mv _quarto-index.yml _quarto.yml
find ./ -type f -name index.qmd -print0 | \
  xargs -0 -P4 -I{} \
  bash -c 'quarto render "$1" --profile index --to html --no-clean --quiet 2>&1 | grep -v -e "Unknown meta key .* specified in a metadata Shortcode" -e "^Output created:"; exit ${PIPESTATUS[0]}' _ {}
mv _quarto.yml _quarto-index.yml
cp _quarto_not_used.yml _quarto.yml && rm _quarto_not_used.yml

# Revert the sitemap and llms.txt to the originals captured before index renders
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

echo "[7/7] Cleaning up intermediate files..."
find _site -type f -name '*.qmd' -delete
# Strip intermediate Typst sources left next to the PDFs (no keep-typ in prod).
find _site -type f -name '*.typ' -delete

cp ../404.html _site/404.html
cp ../redirect_map.json _site/redirect_map.json
cp ../url_mapping.json _site/url_mapping.json

echo "✅ Docs built successfully"
