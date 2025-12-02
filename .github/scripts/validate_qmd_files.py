import os
import yaml
import re
from pathlib import Path
from typing import Dict
import sys


# Change working directory to root of the repository
script_dir = Path(__file__).parent
root_dir = script_dir / "../../"
os.chdir(root_dir.resolve())


DOCS_DIR = "DOCS"
EXCLUDED_DOCS_DIRS = {"templates", "theme", "includes", "_meta"}

# Define allowed categories
ALLOWED_CATEGORIES = {
    "guidelines",
    "products",
    "uncategorized",
}


def extract_yaml_header(file_path: Path) -> Dict:
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        # Look for YAML frontmatter between --- markers
        yaml_match = re.search(
            r"^---\s*\n(.*?)\n---", content, re.DOTALL | re.MULTILINE
        )

        if not yaml_match:
            return {"error": "no_yaml_header"}

        yaml_content = yaml_match.group(1)
        metadata = yaml.safe_load(yaml_content)

        if metadata is None:
            return {"error": "empty_yaml_header"}

        return metadata

    except yaml.YAMLError as e:
        return {"error": "yaml_error", "details": str(e)}
    except Exception as e:
        return {"error": "file_error", "details": str(e)}


def validate_qmd_category(file_path: Path) -> Dict:
    relative_path = str(file_path.resolve().relative_to(Path.cwd()))

    metadata = extract_yaml_header(file_path)

    # Handle errors
    if "error" in metadata:
        return {
            "file": relative_path,
            "valid": False,
            "error": metadata["error"],
            "details": metadata.get("details", "No YAML header found"),
        }

    # Check for category
    if "category" not in metadata:
        return {
            "file": relative_path,
            "valid": False,
            "error": "missing_category",
            "details": f"Available fields: {list(metadata.keys())}",
        }

    category = metadata["category"]

    # Validate category value
    if category not in ALLOWED_CATEGORIES:
        return {
            "file": relative_path,
            "valid": False,
            "error": "invalid_category",
            "details": f"Found '{category}', allowed: {sorted(ALLOWED_CATEGORIES)}",
        }

    # Valid!
    return {"file": relative_path, "valid": True, "category": category}


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Validate QMD file categories")
    parser.add_argument(
        "--source",
        "-s",
        default=DOCS_DIR,
        help="Source directory to scan (default: origin_DOCS)",
    )

    args = parser.parse_args()

    # Find all .qmd files
    source_path = Path(args.source)
    qmd_files = [
        f
        for f in source_path.glob("**/*.qmd")
        if not any(
            part in EXCLUDED_DOCS_DIRS
            for part in f.relative_to(source_path).parent.parts
        )
    ]

    if not qmd_files:
        print("No QMD files found.")
        sys.exit(0)

    print(f"Found {len(qmd_files)} QMD files to validate")
    print(f"Allowed categories: {sorted(ALLOWED_CATEGORIES)}")
    print("-" * 60)

    # Validate all files
    invalid_files = 0

    for qmd_file in qmd_files:
        result = validate_qmd_category(qmd_file)

        if not result["valid"]:
            invalid_files += 1
            error_type = result["error"]

            if error_type == "missing_category":
                print(f"❌ {result['file']} → MISSING category field")
            elif error_type == "invalid_category":
                print(f"❌ {result['file']} → INVALID category")
            elif error_type == "no_yaml_header":
                print(f"❌ {result['file']} → NO YAML header")
            else:
                print(f"❌ {result['file']} → ERROR")

    if invalid_files > 0:
        sys.exit(1)
    else:
        print("✅ All QMD files are valid!")
        sys.exit(0)


if __name__ == "__main__":
    main()
