#!/bin/bash
set -e

# Patterns to filter out from Quarto output
QUARTO_NOISE=(
  -e "Unknown meta key .* specified in a metadata Shortcode"
  -e "^Output created:"
)

quarto_render() {
  # Drop noise lines from the output, but key failure on quarto's exit
  # (PIPESTATUS[0]), not grep's. grep returns 1 when it filters everything out,
  # which isn't a render failure - the `|| true` keeps set -e off our back.
  quarto render "$@" 2>&1 | grep --line-buffered -v "${QUARTO_NOISE[@]}" || true
  local status=${PIPESTATUS[0]}
  if [ "$status" -ne 0 ]; then
    echo "ERROR: quarto render failed (exit $status): quarto render $*" >&2
    return "$status"
  fi
}

# Step timing: each step() prints how long the previous one took, so the slow
# phase stands out in the CI log.
_BUILD_START=$(date +%s); _STEP_PREV=$_BUILD_START; _STEP_NAME=""
step() {
  local now; now=$(date +%s)
  if [ -n "$_STEP_NAME" ]; then
    printf '    -> %s took %ds\n' "$_STEP_NAME" "$((now - _STEP_PREV))"
  fi
  echo "$*"
  _STEP_PREV=$now; _STEP_NAME="$*"
}

step "[1/6] Copying DOCS to origin_DOCS..."
mv DOCS origin_DOCS

step "[2/6] Updating URL mappings and grouping documents by category..."
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

# Bake image descriptions into the qmd source now, so the render doesn't re-hash
# every image once per format (see the script). This was a Lua filter.
echo "Baking image descriptions into qmd source..."
python3 ../.github/scripts/build/inject_image_descriptions.py .

# Render with the no-headers config. The with-headers variant is still on
# disk but nothing activates it anymore.
cp _quarto-no-headers.yml _quarto.yml

step "[3/6] Rendering all documents (HTML + Typst PDF + gfm) in one pass..."
# Render every format in the config - html (site), typst (PDFs), gfm
# (the .llms.md sidecars). One pass over the files instead of one per format.
quarto_render --no-clean

# Back up sitemap.xml and llms.txt - the index.qmd renders below regenerate
# them, and we want to keep the values from this first render.
sleep 5
mv _site/sitemap.xml _site/sitemap.xml.bkp
mv _site/llms.txt _site/llms.txt.bkp

step "[4/6] Generating index.qmd files for all DOCS/* folders..."
python3 ../.github/scripts/build/generate_index_all.py

step "[5/6] Rendering index.qmd files..."
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

step "[6/6] Cleaning up intermediate files..."
find _site -type f -name '*.qmd' -delete
# Strip intermediate Typst sources left next to the PDFs (no keep-typ in prod).
find _site -type f -name '*.typ' -delete

cp ../404.html _site/404.html
cp ../redirect_map.json _site/redirect_map.json
cp ../url_mapping.json _site/url_mapping.json

step "✅ Docs built successfully"
