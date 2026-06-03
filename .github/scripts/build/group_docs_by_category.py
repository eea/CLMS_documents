import os
import shutil
import json
import secrets
from pathlib import Path
import yaml


EXCLUDED_DOCS_DIRS = {
    "_meta",
    "assets",
    "_site",
    ".quarto",
}

# Category to directory mapping
# Multiple categories can map to the same directory
CATEGORY_TO_DIRECTORY_MAP = {
    "guidelines": "guidelines",
    "products": "products",
}


# Change working directory to root of the repository
script_dir = Path(__file__).parent
root_dir = script_dir / "../../../"
os.chdir(root_dir.resolve())

# Non-browsable doc mapping file
NON_BROWSABLE_MAP_PATH = Path(".github/non_browsable_doc_map.json")


def load_secret_map():
    if NON_BROWSABLE_MAP_PATH.exists():
        with open(NON_BROWSABLE_MAP_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("mappings", [])
    return []


def save_secret_map(mappings):
    with open(NON_BROWSABLE_MAP_PATH, "w", encoding="utf-8") as f:
        json.dump(
            {
                "_comment": "This file maps non-browsable QMD source files to their persistent random output names and URLs. Do not publish this file.",
                "mappings": mappings,
            },
            f,
            indent=2,
        )


def random_base(length=64):
    return secrets.token_hex(length // 2)[:length]


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

    if category in CATEGORY_TO_DIRECTORY_MAP:
        return CATEGORY_TO_DIRECTORY_MAP[category]

    return category


def read_qmd_frontmatter(file_path):
    """Return (yaml_data, body) for a QMD file, or (None, None) if no/malformed header."""
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return None, None
    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, None
    yaml_data = yaml.safe_load(parts[1]) or {}
    return yaml_data, parts[2]


def write_qmd_frontmatter(file_path, yaml_data, body):
    new_header = yaml.dump(yaml_data, default_flow_style=False, allow_unicode=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"---\n{new_header}---{body}")


def extract_category_from_qmd(file_path):
    try:
        yaml_data, _ = read_qmd_frontmatter(file_path)
        if yaml_data:
            category = yaml_data.get("category")
            if category is not None:
                return str(category).strip()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")

    return None


def copy_media_and_rewrite(qmd_src, qmd_dst, src_stem, dst_stem):
    """Copy {src_stem}-media next to qmd_dst as {dst_stem}-media and rewrite refs."""
    src_media = qmd_src.parent / f"{src_stem}-media"
    if not (src_media.exists() and src_media.is_dir()):
        return False
    dst_media = qmd_dst.parent / f"{dst_stem}-media"
    if dst_media.exists():
        shutil.rmtree(dst_media)
    shutil.copytree(src_media, dst_media)
    if src_stem != dst_stem:
        try:
            with open(qmd_dst, "r", encoding="utf-8") as f:
                content = f.read()
            old_ref = f"{src_stem}-media/"
            new_ref = f"{dst_stem}-media/"
            if old_ref in content:
                with open(qmd_dst, "w", encoding="utf-8") as f:
                    f.write(content.replace(old_ref, new_ref))
        except Exception as e:
            print(
                f"\t\t[ERROR] Failed to rewrite media references in {qmd_dst.name}: {e}"
            )
    return True


def group_qmd_files_by_category(source_dir="origin_DOCS", target_dir="DOCS"):
    source_path = Path(source_dir)
    target_path = Path(target_dir)

    target_path.mkdir(exist_ok=True)

    path_mappings = {}
    meta_dir = target_path / "_meta"
    meta_dir.mkdir(exist_ok=True)

    secret_mappings = load_secret_map()
    updated = False

    categorized_count = 0
    non_browsable_count = 0
    new_non_browsable_assignments = 0

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

    for qmd_file in qmd_files:
        category = extract_category_from_qmd(qmd_file)
        rel_source = str(qmd_file.relative_to(source_path))
        project_name = qmd_file.parts[1] if len(qmd_file.parts) > 2 else ""

        if category == "non-browsable":
            nb_dir = target_path / "non-browsable"
            nb_dir.mkdir(exist_ok=True)
            mapping = get_secret_mapping_for_source(secret_mappings, rel_source)
            if mapping is None:
                base = random_base()
                url = "/" + base + ".html"
                secret_mappings = add_secret_mapping(
                    secret_mappings, rel_source, base, url
                )
                updated = True
                new_non_browsable_assignments += 1
            else:
                base = mapping["base"]
                url = mapping["url"]

            target_file = nb_dir / f"{base}.qmd"
            shutil.copy2(qmd_file, target_file)

            path_mappings[str(target_file.relative_to(target_path))] = rel_source
            copy_media_and_rewrite(qmd_file, target_file, qmd_file.stem, base)
            non_browsable_count += 1
        else:
            target_directory = get_directory_for_category(category)
            target_folder = target_path / target_directory
            target_folder.mkdir(exist_ok=True)
            prefix = f"{project_name}_" if project_name else ""
            target_file = target_folder / f"{prefix}{qmd_file.name}"
            shutil.copy2(qmd_file, target_file)

            path_mappings[str(target_file.relative_to(target_path))] = rel_source
            copy_media_and_rewrite(
                qmd_file, target_file, qmd_file.stem, target_file.stem
            )
            categorized_count += 1

    if updated:
        save_secret_map(secret_mappings)
        if new_non_browsable_assignments > 0:
            print(
                f"\t[non-browsable] Created {new_non_browsable_assignments} new URL mappings"
            )

    mapping_file = target_path / "_meta" / ".temp_path_mapping.json"
    with open(mapping_file, "w", encoding="utf-8") as f:
        json.dump(path_mappings, f, indent=2)

    print(
        f"\tProcessed {len(qmd_files)} files: {categorized_count} categorized, {non_browsable_count} non-browsable."
    )


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


def inject_original_filename_in_qmd_files(docs_dir="origin_DOCS"):
    """
    Add original-filename field to all QMD files for changelog lookup.
    This eliminates the need for Lua filters to detect filenames.
    """
    docs_path = Path(docs_dir)

    processed_files = 0
    skipped_files = 0

    for qmd_file in docs_path.rglob("*.qmd"):
        if any(excluded in qmd_file.parts for excluded in EXCLUDED_DOCS_DIRS):
            continue

        relative_path = qmd_file.relative_to(docs_path)
        original_filename_field = str(relative_path)

        try:
            yaml_data, body = read_qmd_frontmatter(qmd_file)
            if yaml_data is None:
                print(
                    f"    Warning: {qmd_file.name} missing or malformed YAML header, skipping"
                )
                skipped_files += 1
                continue

            yaml_data["original-filename"] = original_filename_field
            write_qmd_frontmatter(qmd_file, yaml_data, body)
            processed_files += 1

        except yaml.YAMLError as e:
            print(f"    Error parsing YAML in {qmd_file.name}: {e}")
            skipped_files += 1
        except Exception as e:
            print(f"    Error processing {qmd_file.name}: {e}")
            skipped_files += 1

    if skipped_files > 0:
        print(f"Skipped {skipped_files} files due to errors or missing headers.")


def update_bibliography_paths_before_regroup(
    docs_dir="origin_DOCS", bibliography_dir="bibliography"
):
    docs_path = Path(docs_dir)
    bib_dir_path = Path(bibliography_dir)

    bib_dir_path.mkdir(exist_ok=True)

    print("\tUpdating bibliography references and moving .bib files...")

    processed_projects = 0
    processed_qmd_files = 0
    moved_bib_files = 0

    for project_dir in docs_path.iterdir():
        if not project_dir.is_dir() or project_dir.name in EXCLUDED_DOCS_DIRS:
            continue

        project_name = project_dir.name

        bib_files = list(project_dir.glob("*.bib"))

        if len(bib_files) > 1:
            print(
                f"\tWarning: Found multiple .bib files in {project_name}: {[f.name for f in bib_files]}"
            )
            print("\tUsing the first one found.")

        if not bib_files:
            continue

        original_bib = bib_files[0]
        new_bib_name = f"{project_name}.bib"
        new_bib_path = bib_dir_path / new_bib_name
        new_bib_reference = f"../../{bibliography_dir}/{new_bib_name}"

        qmd_files = list(project_dir.glob("*.qmd"))

        if not qmd_files:
            print(f"\tNo .qmd files found in {project_name}")
            continue

        for qmd_file in qmd_files:
            if update_qmd_bibliography_reference(qmd_file, new_bib_reference):
                processed_qmd_files += 1

        shutil.copy2(original_bib, new_bib_path)
        moved_bib_files += 1

        processed_projects += 1


def update_qmd_bibliography_reference(qmd_file_path, new_bib_reference):
    try:
        yaml_data, body = read_qmd_frontmatter(qmd_file_path)
        if yaml_data is None:
            print(
                f"    Warning: {qmd_file_path.name} missing or malformed YAML header"
            )
            return False

        if "bibliography" not in yaml_data:
            return False

        yaml_data["bibliography"] = new_bib_reference
        write_qmd_frontmatter(qmd_file_path, yaml_data, body)
        return True

    except yaml.YAMLError as e:
        print(f"    Error parsing YAML in {qmd_file_path.name}: {e}")
        return False
    except Exception as e:
        print(f"    Error processing {qmd_file_path.name}: {e}")
        return False


if __name__ == "__main__":
    inject_original_filename_in_qmd_files()

    update_bibliography_paths_before_regroup()

    group_qmd_files_by_category()

    copy_excluded_dirs()
