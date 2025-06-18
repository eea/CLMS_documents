from pathlib import Path
import json
import re
import google.generativeai as genai
import tiktoken
import yaml
import os
from pathlib import Path
import sys
import json5
import hashlib

# Configuration
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise EnvironmentError("GEMINI_API_KEY environment variable not set")
MODEL_NAME = "gemini-2.0-flash"
TOKEN_LIMIT_PER_MINUTE = 950_000  # Keep a safe margin below 1M

SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_DIR = (SCRIPT_DIR / "../../DOCS").resolve()
ROOT_DIR = (SCRIPT_DIR / "../../").resolve()
CACHE_DIR = (SCRIPT_DIR / "../../.llm_cache").resolve()
CACHE_DIR.mkdir(exist_ok=True)
BLACKLISTED_DIRS = {"templates", "includes", "theme"}

PROMPT = """You are an AI assistant helping to enrich technical documents for the Copernicus Land Monitoring Service (CLMS).

Your tasks:
1. Read and understand the entire attached document. Ignore yml metadata and focus on the main content.
2. Generate a professional, engaging **Introduction** (max 1 paragraph) that clearly explains the document’s purpose, scope, and technical focus.
3. Extract exactly 10 **precise and conceptually meaningful keywords or key phrases** that reflect the core scientific or technical content of the document.
4. Use British English spelling and terminology.

Keyword guidance:
- Do **not** use general terms like \"Urban Atlas\", \"metadata\", \"documentation\", \"nomenclature\", or \"report\".
- Focus on **specific concepts, methods, environmental indicators, technical systems, data processing strategies**, or **analytical results** that are central to the document.
- Use **multi-word phrases** when needed for clarity and specificity.
- Think like an expert indexing the document for scientific search or semantic web use.

Return only the result as a raw JSON object (no code block, no explanation):

{
  \"introduction\": \"...\",
  \"keywords\": [\"keyword1\", \"keyword2\", ..., \"keyword10\"]
}

Avoid trailing commas in the JSON output.
"""

# Setup Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL_NAME)
encoding = tiktoken.get_encoding("cl100k_base")
total_tokens_sent = 0


# Function to update YAML frontmatter using PyYAML
def update_qmd_file(doc_path, description: str, keywords_list: list):
    lines = doc_path.read_text(encoding="utf-8").splitlines()
    if lines[0].strip() != "---":
        return

    try:
        end_idx = lines[1:].index("---") + 1
    except ValueError:
        return

    yaml_block = "\n".join(lines[1:end_idx])
    yaml_data = yaml.safe_load(yaml_block) or {}
    yaml_data["description"] = description.replace("\n", " ").strip()
    yaml_data["keywords"] = keywords_list

    new_yaml_block = yaml.dump(yaml_data, sort_keys=False, allow_unicode=True).strip()
    new_lines = ["---"] + new_yaml_block.splitlines() + ["---"] + lines[end_idx + 1 :]

    doc_path.write_text("\n".join(new_lines), encoding="utf-8")


# Function to process one document with Gemini
def process_document_with_llm(doc_path: Path):
    global total_tokens_sent

    file_contents = doc_path.read_text(encoding="utf-8")
    input_tokens = len(encoding.encode(file_contents))
    print(f"[LLM] Processing: {doc_path} ({input_tokens} input tokens)")
    if total_tokens_sent + input_tokens > TOKEN_LIMIT_PER_MINUTE:
        print(
            f"[SKIPPED] {doc_path} would exceed token budget. Estimated at {input_tokens} tokens."
        )
        return

    response = model.generate_content(
        contents=[
            {
                "role": "user",
                "parts": [
                    {"text": PROMPT},
                    {
                        "inline_data": {
                            "mime_type": "text/plain",
                            "data": file_contents.encode("utf-8"),
                        }
                    },
                ],
            }
        ]
    )

    total_tokens_sent += input_tokens

    raw_text = response.text.strip()
    if raw_text.startswith("```"):
        raw_text = re.sub(r"^```(?:json)?\s*", "", raw_text)
        raw_text = re.sub(r"\s*```$", "", raw_text)

    try:
        parsed_output = json5.loads(raw_text)
        return {
            "introduction": parsed_output["introduction"],
            "keywords": parsed_output["keywords"],
        }
    except (json.JSONDecodeError, KeyError) as e:
        print(f"[ERROR] Invalid response for {doc_path}:", raw_text)
        return None


# Function to read paths of modified documents (.qmd) from a file. The file is provided by github actions as an input.
def read_paths_from_filename():
    input_file = sys.argv[1]
    try:
        with open(input_file, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        raise FileNotFoundError(f"File not found: {input_file}")
    except Exception as e:
        raise RuntimeError(f"Error reading file: {e}")


# Cache-related functions
def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def get_cache_path(qmd_path):
    safe_path = "__".join(qmd_path.parts)
    return CACHE_DIR / f"{safe_path}.json"


def load_cached_result(cache_path):
    if cache_path.exists():
        with cache_path.open() as f:
            return json.load(f)
    return {}


def save_cached_result(cache_path, data):
    with cache_path.open("w") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    modified_paths = set(Path(p) for p in read_paths_from_filename())

    for full_doc_path in INPUT_DIR.rglob("*.qmd"):
        doc_path = full_doc_path.relative_to(ROOT_DIR)
        if any(part in BLACKLISTED_DIRS for part in doc_path.parts):
            continue

        cache_path = get_cache_path(doc_path)
        current_hash = file_hash(doc_path)
        cache = load_cached_result(cache_path)

        if doc_path in modified_paths or cache.get("hash") != current_hash:
            result = process_document_with_llm(doc_path)
            cache = {
                "hash": current_hash,
                "intro": result["introduction"],
                "keywords": result["keywords"],
            }
            save_cached_result(cache_path, cache)

        update_qmd_file(doc_path, cache["intro"], cache["keywords"])

    print("Total tokens sent:", total_tokens_sent)
