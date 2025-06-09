from pathlib import Path
import json
import time
import re
import google.generativeai as genai
import tiktoken
import yaml
from io import StringIO
import os
from pathlib import Path

# Configuration
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise EnvironmentError("GEMINI_API_KEY environment variable not set")
MODEL_NAME = "gemini-2.0-flash"
TOKEN_LIMIT_PER_MINUTE = 950_000  # Keep a safe margin below 1M

SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_DIR = (SCRIPT_DIR / "../../DOCS").resolve()

PROMPT = """You are an AI assistant helping to enrich a Quarto Markdown (.qmd) technical document prepared for the European Environment Agency (EEA).

Your tasks:
1. Read and understand the entire attached document.
2. Generate a professional, engaging **Introduction** (max 1 paragraph) that clearly explains the document’s purpose, scope, and technical focus.
3. Extract exactly 10 **precise and conceptually meaningful keywords or key phrases** that reflect the core scientific or technical content of the document.

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
"""

# Setup Gemini
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel(MODEL_NAME)
encoding = tiktoken.get_encoding("cl100k_base")
total_tokens_sent = 0


# Function to update YAML frontmatter using PyYAML
def update_yaml_header(content: str, description: str, keywords_list: list):
    lines = content.splitlines()
    if lines[0].strip() != "---":
        return content

    try:
        end_idx = lines[1:].index("---") + 1
    except ValueError:
        return content

    yaml_block = "\n".join(lines[1:end_idx])
    yaml_data = yaml.safe_load(yaml_block) or {}
    yaml_data["description"] = description.replace("\n", " ").strip()
    yaml_data["keywords"] = keywords_list

    new_yaml_block = yaml.dump(yaml_data, sort_keys=False, allow_unicode=True).strip()
    new_lines = ["---"] + new_yaml_block.splitlines() + ["---"] + lines[end_idx + 1 :]
    return "\n".join(new_lines)


# Function to process one document with Gemini
def process_document_with_llm(doc_path: Path):
    print("Processing ", doc_path)
    global total_tokens_sent

    file_contents = doc_path.read_text(encoding="utf-8")
    input_tokens = len(encoding.encode(file_contents))
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
        parsed_output = json.loads(raw_text)
        introduction = parsed_output["introduction"]
        keywords_list = parsed_output["keywords"]
        keywords = ", ".join(keywords_list)
    except (json.JSONDecodeError, KeyError) as e:
        print(f"[ERROR] Invalid response for {doc_path}:", raw_text)
        return

    updated_content = update_yaml_header(file_contents, introduction, keywords_list)
    output_file = doc_path.with_name(doc_path.stem + ".qmd")
    output_file.write_text(updated_content, encoding="utf-8")

    print("Estimated input tokens:", input_tokens)


# Process all .qmd files
BLACKLISTED_DIRS = {"templates", "includes", "theme"}

for doc_path in INPUT_DIR.rglob("*.qmd"):
    if any(part in BLACKLISTED_DIRS for part in doc_path.parts):
        continue
    process_document_with_llm(doc_path)

print("Total tokens sent:", total_tokens_sent)
