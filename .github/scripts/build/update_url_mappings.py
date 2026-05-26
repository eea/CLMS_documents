import os
import json
import yaml
import re
from pathlib import Path

DOCS_DIR = "origin_DOCS"
CATEGORIZED_DOCS_DIR = "DOCS/_site"
EXCLUDED_DOCS_DIRS = {"_meta", "_site", ".quarto", "assets"}


DOMAIN = "https://library.land.copernicus.eu"

# Redirect template
REDIRECT_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Moved - Redirecting...</title>
    
    <!-- Immediate redirect via meta refresh -->
    <meta http-equiv="refresh" content="0; url=/{target_url}">
    
    <!-- Canonical URL for SEO -->
    <link rel="canonical" href="{canonical_url}">
    
    <!-- JavaScript redirect (faster than meta refresh) -->
    <script>
        window.location.replace("/{target_url}");
    </script>
    
</head>
<body>
    <div class="redirect-message">
        <div class="spinner"></div>
        <h2>Page Moved</h2>
        <p>This page has moved to a new location.</p>
        <p>If you are not redirected automatically, <a href="/{target_url}">click here</a>.</p>
    </div>
</body>
</html>"""

# Change working directory to root of the repository
script_dir = Path(__file__).parent
root_dir = script_dir / "../../../"
os.chdir(root_dir.resolve())


class DocsURLMapper:
    def __init__(self, mapping_file="url_mapping.json"):
        self.mapping_file = mapping_file
        self.url_mappings = self.load_mappings()

    def load_mappings(self):
        if os.path.exists(self.mapping_file):
            with open(self.mapping_file, "r") as f:
                return json.load(f)
        return {}

    def save_mappings(self):
        with open(self.mapping_file, "w") as f:
            json.dump(self.url_mappings, f, indent=2)

    def _current_target_urls(self):
        """Set of live (non-redirect) target URLs — what redirects should resolve to."""
        return {
            v for k, v in self.url_mappings.items() if not k.startswith("redirect:")
        }

    def _find_qmd_files(self, source_dir):
        source_path = Path(source_dir)
        return source_path, [
            f
            for f in source_path.glob("**/*.qmd")
            if not any(
                part in EXCLUDED_DOCS_DIRS
                for part in f.relative_to(source_path).parent.parts
            )
        ]

    def extract_metadata_from_qmd(self, file_path):
        """Extract category and title from QMD file"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()

            yaml_match = re.search(
                r"^---\s*\n(.*?)\n---", content, re.DOTALL | re.MULTILINE
            )
            if yaml_match:
                yaml_content = yaml_match.group(1)
                metadata = yaml.safe_load(yaml_content)

                return {
                    "category": metadata.get("category", "uncategorized"),
                    "title": metadata.get("title", file_path.stem),
                }
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

        return None

    def generate_url_paths(self, category, filename):
        slug = Path(filename).stem
        return {"html": f"{category}/{slug}.html", "pdf": f"{category}/{slug}.pdf"}

    def _upsert_mapping(self, key, new_url, label):
        """Update a mapping; if the URL changed, record a redirect.
        Returns (redirect_created, is_new_file)."""
        redirect_created = is_new = False
        if key in self.url_mappings:
            old_url = self.url_mappings[key]
            if old_url != new_url:
                self.url_mappings[f"redirect:{old_url}"] = new_url
                print(f"{label} redirect created: {old_url} → {new_url}")
                redirect_created = True
        else:
            is_new = True
        self.url_mappings[key] = new_url
        return redirect_created, is_new

    def update_mappings(self, source_dir=DOCS_DIR):
        source_path, qmd_files = self._find_qmd_files(source_dir)

        html_redirects_created = 0
        pdf_redirects_created = 0
        new_files = 0

        for qmd_file in qmd_files:
            metadata = self.extract_metadata_from_qmd(qmd_file)
            if not metadata:
                continue
            filename = str(qmd_file.relative_to(source_path))
            new_urls = self.generate_url_paths(metadata["category"], qmd_file.name)

            html_redirect, html_new = self._upsert_mapping(
                filename, new_urls["html"], "HTML"
            )
            pdf_redirect, _ = self._upsert_mapping(
                f"{filename}:pdf", new_urls["pdf"], "PDF"
            )

            html_redirects_created += int(html_redirect)
            pdf_redirects_created += int(pdf_redirect)
            new_files += int(html_new)

        # Optimize redirect chains - point all old URLs directly to current location
        self.optimize_redirect_chains()

        self.save_mappings()

        if html_redirects_created > 0 or pdf_redirects_created > 0:
            print(
                f"\tCreated {html_redirects_created} HTML redirects, {pdf_redirects_created} PDF redirects from {len(qmd_files)} files."
            )
        if new_files > 0:
            print(f"\tDetected {new_files} new files.")

    def optimize_redirect_chains(self):
        current_urls = self._current_target_urls()

        def find_final_destination(url, visited=None):
            if visited is None:
                visited = set()

            if url in visited:
                print(f"\tWarning: Circular redirect detected for {url}")
                return url

            visited.add(url)

            if url in current_urls:
                return url

            redirect_key = f"redirect:{url}"
            if redirect_key in self.url_mappings:
                return find_final_destination(self.url_mappings[redirect_key], visited)

            return url

        redirects_optimized = 0

        for redirect_key, target_url in list(self.url_mappings.items()):
            if redirect_key.startswith("redirect:"):
                final_destination = find_final_destination(target_url)

                if final_destination != target_url:
                    self.url_mappings[redirect_key] = final_destination
                    old_url = redirect_key.replace("redirect:", "")
                    print(
                        f"\tOptimized: {old_url} → {final_destination} (was → {target_url})"
                    )
                    redirects_optimized += 1

        if redirects_optimized > 0:
            print(f"\tOptimized {redirects_optimized} redirect chains")

    def cleanup_missing_files(self, source_dir=DOCS_DIR):
        """Remove mappings for files that no longer exist"""
        source_path, qmd_files = self._find_qmd_files(source_dir)
        existing_qmd_files = {str(f.relative_to(source_path)) for f in qmd_files}

        removed_count = 0
        for key in list(self.url_mappings.keys()):
            if not key.startswith("redirect:"):
                source_file = key.replace(":pdf", "") if key.endswith(":pdf") else key

                if (
                    source_file.endswith(".qmd")
                    and source_file not in existing_qmd_files
                ):
                    # Remove both HTML and PDF mappings
                    for suffix in ["", ":pdf"]:
                        mapping_key = source_file + suffix
                        if mapping_key in self.url_mappings:
                            del self.url_mappings[mapping_key]
                            removed_count += 1

        return removed_count

    def cleanup_dead_redirects(self):
        valid_urls = self._current_target_urls()

        removed_count = 0
        for key in list(self.url_mappings.keys()):
            if key.startswith("redirect:"):
                target_url = self.url_mappings[key]
                if target_url not in valid_urls:
                    print(f"Removing dead redirect: {key} → {target_url}")
                    del self.url_mappings[key]
                    removed_count += 1

        return removed_count

    def generate_github_pages_redirects(self, output_dir=CATEGORIZED_DOCS_DIR):
        output_path = Path(output_dir)

        redirect_count = 0

        for key, target_url in self.url_mappings.items():
            if key.startswith("redirect:") and target_url.endswith(".html"):
                old_url = key.replace("redirect:", "")

                redirect_file_path = output_path / Path(old_url)
                redirect_file_path.parent.mkdir(parents=True, exist_ok=True)
                canonical_url = f"{DOMAIN}/{target_url}"

                with open(redirect_file_path, "w", encoding="utf-8") as f:
                    f.write(
                        REDIRECT_TEMPLATE.format(
                            target_url=target_url, canonical_url=canonical_url
                        )
                    )

                redirect_count += 1

        return redirect_count

    def generate_redirect_map_json(self, output_dir="."):
        """Generate a JSON file with all redirects for client-side fallback"""
        redirect_map = {}

        for key, target_url in self.url_mappings.items():
            if key.startswith("redirect:"):
                old_url = key.replace("redirect:", "")
                redirect_map[old_url] = target_url

        map_file = Path(output_dir) / "redirect_map.json"
        map_file.parent.mkdir(parents=True, exist_ok=True)
        with open(map_file, "w") as f:
            json.dump(redirect_map, f, indent=2)

        return redirect_map

    def print_redirect_summary(self):
        """Print a summary of all redirects"""
        redirects = {
            k: v for k, v in self.url_mappings.items() if k.startswith("redirect:")
        }

        if redirects:
            print("\n=== REDIRECT SUMMARY ===")
            print(f"Total redirects: {len(redirects)}")
            print("\nActive redirects:")
            html_redirects = []
            pdf_redirects = []

            for redirect_key, target_url in redirects.items():
                old_url = redirect_key.replace("redirect:", "")
                if old_url.endswith(".pdf"):
                    pdf_redirects.append(f"  {old_url} → {target_url}")
                else:
                    html_redirects.append(f"  {old_url} → {target_url}")

            if html_redirects:
                print("  HTML redirects:")
                for redirect in html_redirects:
                    print(redirect)

            if pdf_redirects:
                print("  PDF redirects:")
                for redirect in pdf_redirects:
                    print(redirect)
        else:
            print("\tNo redirects needed - all URLs are current.")


def main():
    mapper = DocsURLMapper()

    # 1. Update mappings (creates redirects)
    mapper.update_mappings()

    # 2. Clean up AFTER redirect creation
    print("\tCleaning up mappings...")
    removed_files = mapper.cleanup_missing_files()
    removed_redirects = mapper.cleanup_dead_redirects()
    if removed_files > 0 or removed_redirects > 0:
        mapper.save_mappings()
        print("\tUpdated url_mapping.json after cleanup")

    if removed_files > 0:
        print(f"\tRemoved {removed_files} mappings for missing files")
    if removed_redirects > 0:
        print(f"\tRemoved {removed_redirects} dead redirects")

    # 3. Generate output files
    print("\tGenerating redirect files...")
    redirect_count = mapper.generate_github_pages_redirects()
    redirect_map = mapper.generate_redirect_map_json()
    mapper.print_redirect_summary()

    print(
        f"\tComplete: {redirect_count} redirects, {len(redirect_map)} redirect map entries"
    )


if __name__ == "__main__":
    main()
