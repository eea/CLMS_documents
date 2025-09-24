
import os
import shutil
import re
import json
import random
import string
from pathlib import Path
import yaml


EXCLUDED_DOCS_DIRS = {"templates", "theme", "includes"}

# Quarto configuration files to copy
QUARTO_CONFIG_FILES = ["_quarto.yml", "_quarto-index.yml", "_quarto-no-headers.yml"]

# Category to directory mapping
# Multiple categories can map to the same directory
CATEGORY_TO_DIRECTORY_MAP = {
    "guidelines": "guidelines",
    "products": "products",
}


# Change working directory to root of the repository
script_dir = Path(__file__).parent
root_dir = script_dir / "../../"
os.chdir(root_dir.resolve())

# Secret doc mapping file
SECRET_MAP_PATH = Path(".github/secret_doc_map.json")

def load_secret_map():
    if SECRET_MAP_PATH.exists():
        with open(SECRET_MAP_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("mappings", [])
    return []

def save_secret_map(mappings):
    with open(SECRET_MAP_PATH, "w", encoding="utf-8") as f:
        json.dump({
            "_comment": "This file maps secret QMD source files to their persistent random output names and URLs. Do not publish this file.",
            "mappings": mappings
        }, f, indent=2)

def random_base(length=64):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def get_secret_mapping_for_source(mappings, source):
    for m in mappings:
        if m["source"] == source:
            return m
    return None

def add_secret_mapping(mappings, source, base, url):
    mappings.append({"source": source, "base": base, "url": url})
    return mappings


def get_directory_for_category(category):
    if not category:
        return "uncategorized"

    # Check if category is in the mapping
    if category in CATEGORY_TO_DIRECTORY_MAP:
        return CATEGORY_TO_DIRECTORY_MAP[category]

    # If not mapped, use the category name as directory name
    return category


def extract_category_from_qmd(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Look for YAML frontmatter between --- markers
        yaml_match = re.search(
            r"^---\s*\n(.*?)\n---", content, re.DOTALL | re.MULTILINE
        )
        if yaml_match:
            yaml_content = yaml_match.group(1)

            # Look for category field in YAML frontmatter only (single line)
            category_match = re.search(
                r'^category:\s*["\']?([^"\'\n\r]+)["\']?\s*$',
                yaml_content,
                re.MULTILINE,
            )
            if category_match:
                return category_match.group(1).strip()

    except Exception as e:
        print(f"Error reading {file_path}: {e}")

    return None


def copy_media_directory_if_exists(qmd_file, target_folder):
    # Get the base filename without extension
    base_name = qmd_file.stem  # filename without .qmd
    media_dir_name = f"{base_name}-media"

    # Look for media directory in the same folder as the qmd file
    source_media_dir = qmd_file.parent / media_dir_name

    if source_media_dir.exists() and source_media_dir.is_dir():
        # Target media directory in the new location
        target_media_dir = target_folder / media_dir_name

        # Remove target if it already exists and copy the media directory
        if target_media_dir.exists():
            shutil.rmtree(target_media_dir)

        shutil.copytree(source_media_dir, target_media_dir)
        print(f"\t\tCopied media directory: {media_dir_name}")
        return True

    return False



def group_qmd_files_by_category(source_dir="origin_DOCS", target_dir="DOCS"):
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    # Create target directory if it doesn't exist
    target_path.mkdir(exist_ok=True)

    # Load secret doc mapping
    secret_mappings = load_secret_map()
    updated = False

    # Find all .qmd files
    qmd_files = [
        f
        for f in source_path.glob("**/*.qmd")
        if not any(
            part in EXCLUDED_DOCS_DIRS
            for part in f.relative_to(source_path).parent.parts
        )
    ]

    if not qmd_files:
        print("No .qmd files found in the current directory")
        return

    print(f"Found {len(qmd_files)} .qmd files")

    for qmd_file in qmd_files:
        category = extract_category_from_qmd(qmd_file)
        rel_source = str(qmd_file.relative_to(source_path))
        project_name = qmd_file.parts[1] if len(qmd_file.parts) > 1 else ""

        if category == "secret":
            # Place all secret docs in DOCS/secret/
            secret_dir = target_path / "secret"
            secret_dir.mkdir(exist_ok=True)
            mapping = get_secret_mapping_for_source(secret_mappings, rel_source)
            if mapping is None:
                base = random_base()
                url = "/" + base + ".html"
                secret_mappings = add_secret_mapping(secret_mappings, rel_source, base, url)
                updated = True
                print(f"\t[secret] Assigned new random base '{base}' for {rel_source}")
            else:
                base = mapping["base"]
                url = mapping["url"]
                print(f"\t[secret] Using existing base '{base}' for {rel_source}")

            target_file = secret_dir / f"{base}.qmd"
            shutil.copy2(qmd_file, target_file)
            orig_media_dir = qmd_file.parent / f"{qmd_file.stem}-media"
            target_media_dir = secret_dir / f"{base}-media"
            if orig_media_dir.exists() and orig_media_dir.is_dir():
                if target_media_dir.exists():
                    shutil.rmtree(target_media_dir)
                shutil.copytree(orig_media_dir, target_media_dir)
                print(f"\t\tCopied media directory: {base}-media (renamed for secret)")
                # Update references in the copied .qmd file
                try:
                    with open(target_file, "r", encoding="utf-8") as f:
                        content = f.read()
                    old_media = f"{qmd_file.stem}-media/"
                    new_media = f"{base}-media/"
                    if old_media in content:
                        content = content.replace(old_media, new_media)
                        with open(target_file, "w", encoding="utf-8") as f:
                            f.write(content)
                        print(f"\t\tRewrote media references in {base}.qmd (secret)")
                except Exception as e:
                    print(f"\t\t[ERROR] Failed to rewrite media references in {base}.qmd: {e}")
            print(f"\t[secret] Copied {qmd_file.name} → secret/{base}.qmd (secret)")
        else:
            # Normal doc: group by category, prefix with project name to avoid collisions
            target_directory = get_directory_for_category(category)
            target_folder = target_path / target_directory
            target_folder.mkdir(exist_ok=True)
            prefix = f"{project_name}_" if project_name else ""
            target_file = target_folder / f"{prefix}{qmd_file.name}"
            shutil.copy2(qmd_file, target_file)
            # Copy media dir with prefix
            orig_media_dir = qmd_file.parent / f"{qmd_file.stem}-media"
            if orig_media_dir.exists() and orig_media_dir.is_dir():
                target_media_dir = target_folder / f"{prefix}{qmd_file.stem}-media"
                if target_media_dir.exists():
                    shutil.rmtree(target_media_dir)
                shutil.copytree(orig_media_dir, target_media_dir)
                print(f"\t\tCopied media directory: {prefix}{qmd_file.stem}-media")
            # Rewrite media references in the copied QMD file
            if prefix:
                try:
                    with open(target_file, "r", encoding="utf-8") as f:
                        content = f.read()
                    # Replace all occurrences of the original media dir with the prefixed one
                    old_media = f"{qmd_file.stem}-media/"
                    new_media = f"{prefix}{qmd_file.stem}-media/"
                    if old_media in content:
                        content = content.replace(old_media, new_media)
                        with open(target_file, "w", encoding="utf-8") as f:
                            f.write(content)
                        print(f"\t\tRewrote media references in {prefix}{qmd_file.name}")
                except Exception as e:
                    print(f"\t\t[ERROR] Failed to rewrite media references in {prefix}{qmd_file.name}: {e}")
            if category:
                if category in CATEGORY_TO_DIRECTORY_MAP:
                    print(f"\tCopied {qmd_file.name} → {target_directory}/ as {prefix}{qmd_file.name} (category: {category})")
                else:
                    print(f"\tCopied {qmd_file.name} → {target_directory}/ as {prefix}{qmd_file.name}")
            else:
                print(f"\tCopied {qmd_file.name} → {target_directory}/ as {prefix}{qmd_file.name} (no category found)")

    # Save updated secret mapping if changed
    if updated:
        save_secret_map(secret_mappings)
        print(f"[secret] Updated mapping file: {SECRET_MAP_PATH}")
    else:
        print(f"[secret] No changes to mapping file: {SECRET_MAP_PATH}")


def copy_excluded_dirs(source_dir="origin_DOCS", target_dir="DOCS"):
    source_path = Path(source_dir)
    target_path = Path(target_dir)
    for excluded_dir in EXCLUDED_DOCS_DIRS:
        src = source_path / excluded_dir
        dst = target_path / excluded_dir
        if src.exists() and src.is_dir():
            if dst.exists():
                shutil.rmtree(dst)
            shutil.copytree(src, dst)


def copy_quarto_config_files(source_dir="origin_DOCS", target_dir="DOCS"):
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    # Ensure target directory exists
    target_path.mkdir(exist_ok=True)

    for quarto_file in QUARTO_CONFIG_FILES:
        src_file = source_path / quarto_file
        dst_file = target_path / quarto_file

        if src_file.exists() and src_file.is_file():
            shutil.copy2(src_file, dst_file)
            print(f"Copied {quarto_file} to DOCS folder")
        else:
            print(f"Warning: {quarto_file} not found in {source_dir}")


def update_bibliography_paths_before_regroup(
    docs_dir="origin_DOCS", bibliography_dir="bibliography"
):
    docs_path = Path(docs_dir)
    bib_dir_path = Path(bibliography_dir)

    # Create bibliography directory if it doesn't exist
    bib_dir_path.mkdir(exist_ok=True)

    print("Updating bibliography references and moving .bib files...")

    processed_projects = 0
    processed_qmd_files = 0

    for project_dir in docs_path.iterdir():
        if not project_dir.is_dir() or project_dir.name in EXCLUDED_DOCS_DIRS:
            continue

        project_name = project_dir.name

        # Find .bib file in this project directory
        bib_files = list(project_dir.glob("*.bib"))

        if len(bib_files) > 1:
            print(
                f"\tWarning: Found multiple .bib files in {project_name}: {[f.name for f in bib_files]}"
            )
            print("\tUsing the first one found.")

        if not bib_files:
            print(f"\tNo .bib file found in {project_name}")
            continue

        original_bib = bib_files[0]
        new_bib_name = f"{project_name}.bib"
        new_bib_path = bib_dir_path / new_bib_name
        new_bib_reference = f"../../{bibliography_dir}/{new_bib_name}"

        # Find all .qmd files in this project directory
        qmd_files = list(project_dir.glob("*.qmd"))

        if not qmd_files:
            print(f"\tNo .qmd files found in {project_name}")
            continue

        # Update each .qmd file's bibliography reference
        for qmd_file in qmd_files:
            if update_qmd_bibliography_reference(qmd_file, new_bib_reference):
                processed_qmd_files += 1
                print(f"  Updated {qmd_file.name}")

        # Move .bib file to new location
        shutil.copy2(original_bib, new_bib_path)
        print(f"  Moved {original_bib.name} -> {new_bib_path}")

        processed_projects += 1


def update_qmd_bibliography_reference(qmd_file_path, new_bib_reference):
    try:
        with open(qmd_file_path, "r", encoding="utf-8") as file:
            content = file.read()

        # Split content into YAML header and body
        if not content.startswith("---"):
            print(f"    Warning: {qmd_file_path.name} doesn't have YAML header")
            return False

        parts = content.split("---", 2)
        if len(parts) < 3:
            print(f"    Warning: {qmd_file_path.name} has malformed YAML header")
            return False

        yaml_header = parts[1]
        body = parts[2]

        # Parse YAML header
        try:
            yaml_data = yaml.safe_load(yaml_header)
            if yaml_data is None:
                yaml_data = {}
        except yaml.YAMLError as e:
            print(f"    Error parsing YAML in {qmd_file_path.name}: {e}")
            return False

        # Only update bibliography if it already exists in YAML header
        if "bibliography" in yaml_data:
            old_bib_ref = yaml_data.get("bibliography", "none")
            yaml_data["bibliography"] = new_bib_reference

            # Convert YAML data back to string
            new_yaml_header = yaml.dump(
                yaml_data, default_flow_style=False, allow_unicode=True
            )
            new_content = f"---\n{new_yaml_header}---{body}"

            with open(qmd_file_path, "w", encoding="utf-8") as file:
                file.write(new_content)

            print(f"    {old_bib_ref} -> {new_bib_reference}")
            return True
        else:
            print(f"    No bibliography field in YAML header, skipping")
            return False

    except Exception as e:
        print(f"    Error processing {qmd_file_path.name}: {e}")
        return False


if __name__ == "__main__":
    update_bibliography_paths_before_regroup()

    group_qmd_files_by_category()

    copy_excluded_dirs()
    copy_quarto_config_files()

    print("\nGrouping complete! Check the 'DOCS' folder.")
