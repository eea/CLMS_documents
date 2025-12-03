import os
import json
import yaml
import re
from pathlib import Path

DOCS_DIR = "origin_DOCS"
CATEGORIZED_DOCS_DIR = "DOCS/_site"
EXCLUDED_DOCS_DIRS = {"_meta", "_site", ".quarto", "assets"}


DOMAIN = "https://library.land.copernicus.eu"

# GitHub Pages redirect template
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
root_dir = script_dir / "../../"
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
                    "slug": metadata.get("slug", file_path.stem),
                }
        except Exception as e:
            print(f"Error reading {file_path}: {e}")

        return None

    def generate_url_paths(self, category, filename):
        slug = Path(filename).stem
        return {"html": f"{category}/{slug}.html", "pdf": f"{category}/{slug}.pdf"}

    def update_mappings(self, source_dir=DOCS_DIR):
        source_path = Path(source_dir)
        qmd_files = [
            f
            for f in source_path.glob("**/*.qmd")
            if not any(
                part in EXCLUDED_DOCS_DIRS
                for part in f.relative_to(source_path).parent.parts
            )
        ]

        current_mappings = {}

        for qmd_file in qmd_files:
            metadata = self.extract_metadata_from_qmd(qmd_file)
            if metadata:
                filename = str(qmd_file.relative_to(source_path))
                new_urls = self.generate_url_paths(metadata["category"], qmd_file.name)

                print(f"\nProcessing: {filename}")
                print(f"  Current category: {metadata['category']}")
                print(f"  New HTML URL: {new_urls['html']}")
                print(f"  New PDF URL: {new_urls['pdf']}")

                # Keys are just the filename for HTML, filename:pdf for PDF
                html_key = filename
                pdf_key = f"{filename}:pdf"

                current_mappings[html_key] = new_urls["html"]
                current_mappings[pdf_key] = new_urls["pdf"]

                if html_key in self.url_mappings:
                    old_html_url = self.url_mappings[html_key]
                    print(f"  Old HTML URL: {old_html_url}")
                    print(f"  URLs different: {old_html_url != new_urls['html']}")

                    if old_html_url != new_urls["html"]:
                        redirect_key = f"redirect:{old_html_url}"
                        self.url_mappings[redirect_key] = new_urls["html"]
                        print(
                            f"  HTML redirect created: {old_html_url} → {new_urls['html']}"
                        )
                    else:
                        print(f"    HTML URL unchanged")
                else:
                    print(f"   New file - no previous HTML URL")

                if pdf_key in self.url_mappings:
                    old_pdf_url = self.url_mappings[pdf_key]
                    print(f"  Old PDF URL: {old_pdf_url}")
                    print(f"  URLs different: {old_pdf_url != new_urls['pdf']}")

                    if old_pdf_url != new_urls["pdf"]:
                        redirect_key = f"redirect:{old_pdf_url}"
                        self.url_mappings[redirect_key] = new_urls["pdf"]
                        print(
                            f"  ✅ PDF redirect created: {old_pdf_url} → {new_urls['pdf']}"
                        )
                    else:
                        print(f"  ➡️  PDF URL unchanged")
                else:
                    print(f"  🆕 New file - no previous PDF URL")

                # Update current mappings
                self.url_mappings[html_key] = new_urls["html"]
                self.url_mappings[pdf_key] = new_urls["pdf"]

        # Optimize redirect chains - point all old URLs directly to current location
        self.optimize_redirect_chains()

        self.save_mappings()
        return current_mappings

    def optimize_redirect_chains(self):
        current_html_urls = {}
        current_pdf_urls = {}

        for key, value in self.url_mappings.items():
            if not key.startswith("redirect:"):
                if key.endswith(":pdf"):
                    current_pdf_urls[value] = value
                elif key.endswith(".qmd"):
                    current_html_urls[value] = value

        def find_final_destination(url, visited=None):
            if visited is None:
                visited = set()

            if url in visited:
                print(f"Warning: Circular redirect detected for {url}")
                return url

            visited.add(url)

            # Check if this URL is a current destination
            if url in current_html_urls or url in current_pdf_urls:
                return url

            # Look for redirect from this URL
            redirect_key = f"redirect:{url}"
            if redirect_key in self.url_mappings:
                next_url = self.url_mappings[redirect_key]
                return find_final_destination(next_url, visited)

            # No redirect found, this is the final destination
            return url

        # Optimize all redirects to point to final destinations
        redirects_optimized = 0

        for redirect_key, target_url in list(self.url_mappings.items()):
            if redirect_key.startswith("redirect:"):
                final_destination = find_final_destination(target_url)

                if final_destination != target_url:
                    self.url_mappings[redirect_key] = final_destination
                    old_url = redirect_key.replace("redirect:", "")
                    print(
                        f"Optimized: {old_url} → {final_destination} (was → {target_url})"
                    )
                    redirects_optimized += 1

        if redirects_optimized > 0:
            print(f"Optimized {redirects_optimized} redirect chains")
        else:
            print("No redirect chain optimization needed")

    def cleanup_missing_files(self, source_dir=DOCS_DIR):
        """Remove mappings for files that no longer exist"""
        source_path = Path(source_dir).resolve()  # Get absolute path
        existing_qmd_files = set()

        # Find all .qmd files
        qmd_files = [
            f
            for f in source_path.glob("**/*.qmd")
            if not any(
                part in EXCLUDED_DOCS_DIRS
                for part in f.relative_to(source_path).parent.parts
            )
        ]

        # Get all currently existing QMD files
        for qmd_file in qmd_files:
            try:
                relative_path = str(qmd_file.relative_to(source_path))
                existing_qmd_files.add(relative_path)
            except ValueError:
                # Skip files outside source_dir
                continue

        # Remove mappings for missing files
        removed_count = 0
        for key in list(self.url_mappings.keys()):
            if not key.startswith("redirect:"):
                source_file = key.replace(":pdf", "") if key.endswith(":pdf") else key

                if (
                    source_file.endswith(".qmd")
                    and source_file not in existing_qmd_files
                ):
                    # Remove both HTML and PDF mappings
                    print(f"Removing mapping for missing file: {source_file}")
                    for suffix in ["", ":pdf"]:
                        mapping_key = source_file + suffix
                        if mapping_key in self.url_mappings:
                            del self.url_mappings[mapping_key]
                            removed_count += 1

        return removed_count

    def cleanup_dead_redirects(self):
        valid_urls = set()
        for key, value in self.url_mappings.items():
            if not key.startswith("redirect:"):
                valid_urls.add(value)

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

        print(self.url_mappings.items())

        for key, target_url in self.url_mappings.items():
            if key.startswith("redirect:") and target_url.endswith(".html"):
                old_url = key.replace("redirect:", "")

                # Create directory structure for old URL
                old_path = Path(old_url)
                redirect_file_path = output_path / old_path

                # Create parent directories
                redirect_file_path.parent.mkdir(parents=True, exist_ok=True)

                # Generate canonical URL (assuming your site domain)
                canonical_url = f"{DOMAIN}/{target_url}"

                # Write redirect HTML file
                with open(redirect_file_path, "w", encoding="utf-8") as f:
                    f.write(
                        REDIRECT_TEMPLATE.format(
                            target_url=target_url, canonical_url=canonical_url
                        )
                    )

                print(f"Created redirect: {old_url} → {target_url}")
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

        """Generate a smart 404 page that can handle redirects"""
        html_404 = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Page Not Found</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f8f9fa;
        }}
        .error-message {{
            text-align: center;
            padding: 2rem;
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            max-width: 500px;
        }}
        .search-box {{
            margin-top: 1rem;
            padding: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            width: 100%;
        }}
    </style>
</head>
<body>
    <div class="error-message">
        <h1>404 - Page Not Found</h1>
        <p>The page you're looking for might have moved to a new category.</p>
        <p>Checking for redirects...</p>
        <div id="redirect-status"></div>
        <p><a href="/">Return to Home</a></p>
    </div>
    
    <script>
        // Try to find redirect for current URL
        fetch('/redirect_map.json')
            .then(response => response.json())
            .then(redirectMap => {{
                const currentPath = window.location.pathname.replace(/^\//, '');
                const pathWithoutExtension = currentPath.replace(/\.html$/, '') + '.html';
                
                if (redirectMap[pathWithoutExtension]) {{
                    document.getElementById('redirect-status').innerHTML = 
                        '<p>Found redirect! Redirecting to new location...</p>';
                    setTimeout(() => {{
                        window.location.replace('/' + redirectMap[pathWithoutExtension]);
                    }}, 2000);
                }} else {{
                    document.getElementById('redirect-status').innerHTML = 
                        '<p>No redirect found for this URL.</p>';
                }}
            }})
            .catch(error => {{
                document.getElementById('redirect-status').innerHTML = 
                    '<p>Could not check for redirects.</p>';
            }});
    </script>
</body>
</html>"""

        with open(Path(output_dir) / "404.html", "w", encoding="utf-8") as f:
            f.write(html_404)

        print("Created smart 404.html page")

    def print_redirect_summary(self):
        """Print a summary of all redirects"""
        redirects = {
            k: v for k, v in self.url_mappings.items() if k.startswith("redirect:")
        }

        if redirects:
            print(f"\n=== REDIRECT SUMMARY ===")
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
            print("\nNo redirects needed - all URLs are current.")


def main():
    mapper = DocsURLMapper()

    # 1. Update mappings (creates redirects)
    print("Updating URL mappings...")
    current_mappings = mapper.update_mappings()
    qmd_count = len([k for k in current_mappings.keys() if not k.endswith(":pdf")])
    print(f"Processed {qmd_count} QMD files")

    # 2. Clean up AFTER redirect creation
    print("Cleaning up mappings...")
    removed_files = mapper.cleanup_missing_files()
    removed_redirects = mapper.cleanup_dead_redirects()
    if removed_files > 0 or removed_redirects > 0:
        mapper.save_mappings()
        print("Updated url_mapping.json after cleanup")

    if removed_files > 0:
        print(f"Removed {removed_files} mappings for missing files")
    if removed_redirects > 0:
        print(f"Removed {removed_redirects} dead redirects")

    # 3. Generate output files
    print("Generating redirect files...")
    redirect_count = mapper.generate_github_pages_redirects()
    redirect_map = mapper.generate_redirect_map_json()
    mapper.print_redirect_summary()

    print(
        f"Complete: {redirect_count} redirects, {len(redirect_map)} redirect map entries"
    )


if __name__ == "__main__":
    main()
