#!/usr/bin/env python3
"""
convert_pdf2qmd.py

Uploads a PDF, parses it with ChatDOC API, downloads the parsed .qmd, and extracts inline base64 images into separate files

Usage:
    python convert_pdf2qmd.py input.pdf

Requirements:
    pip install pillow requests
"""

import sys
import re
import os
import base64
import hashlib
import requests
import time
from pathlib import Path
from PIL import Image
from io import BytesIO


BASE_URL = "https://api.chatdoc.com/api/v2"
PREFIX = "img"


def _get_api_token():
    token = os.getenv("CHATDOC_API_KEY")
    if not token:
        raise RuntimeError("Environment variable CHATDOC_API_KEY is not set.")
    return token


def upload_pdf_and_get_id(pdf_path):
    pdf_path = Path(pdf_path)
    if not pdf_path.is_file():
        raise FileNotFoundError(f"PDF not found: {pdf_path}")

    token = _get_api_token()
    headers = {"Authorization": f"Bearer {token}"}

    with pdf_path.open("rb") as f:
        files = {"file": (pdf_path.name, f, "application/pdf")}
        resp = requests.post(
            f"{BASE_URL}/documents/upload", headers=headers, files=files
        )

    if resp.status_code != 200:
        raise RuntimeError(f"Upload failed ({resp.status_code}): {resp.text}")

    payload = resp.json()
    if payload.get("status") != "ok":
        raise RuntimeError(f"Upload error: {payload}")

    upload_id = payload.get("data", {}).get("id")
    if not upload_id:
        raise RuntimeError(f"Upload response missing 'id': {payload}")

    return upload_id


def download_markdown_qmd(upload_id, output_qmd_path, max_wait_s=300, delay_s=15):
    token = _get_api_token()
    headers = {"Authorization": f"Bearer {token}"}

    url = f"{BASE_URL}/pdf_parser/{upload_id}/markdown"
    start = time.monotonic()

    while True:
        resp = requests.get(url, headers=headers)

        if resp.status_code == 200:
            output_qmd_path = Path(output_qmd_path)
            output_qmd_path.parent.mkdir(parents=True, exist_ok=True)
            output_qmd_path.write_text(resp.text, encoding="utf-8")
            return output_qmd_path

        if resp.status_code == 400:
            try:
                detail = resp.json().get("detail", "")
            except Exception:
                detail = ""
            if detail == "Document parsing not completed.":
                if time.monotonic() - start > max_wait_s:
                    raise RuntimeError(
                        "Timed out waiting for document parsing to complete."
                    )
                time.sleep(delay_s)
                continue  # try again

        # Any other error is fatal
        raise RuntimeError(f"Download failed ({resp.status_code}): {resp.text}")


def upload_pdf_and_download_qmd(pdf_path, force=False):
    """
    If a .qmd with the same basename already exists (and is non-empty), skip upload/download.
    Set force=True to re-upload and overwrite the .qmd.
    """
    qmd_path = Path(pdf_path).with_suffix(".qmd")

    if (not force) and qmd_path.exists() and qmd_path.stat().st_size > 0:
        return qmd_path

    upload_id = upload_pdf_and_get_id(pdf_path)
    print(f"Uploaded id: {upload_id}")
    return download_markdown_qmd(upload_id, qmd_path)


def ensure_yaml_header(text):
    if text.lstrip().startswith("---"):
        # conservative: assume user already has a header
        return text
    header = f"""---
title: "TITLE"
subtitle: "SUBTITLE"
date: "2025--14"
version: 1.5

category: products

toc: true
toc-title: "Content"
toc-depth: 3

#### REMOVE THE SECTION BELOW BEFORE PUBLISHING 
format:
  html:
    css: ../theme/styles.css
    code-fold: true 
    self-contained: false
    embed-resources: true
  docx:
    toc-location: before-body
    toc-pagebreak: true
    data: false
    reference-doc: ../theme/template-guideline.docx
#### 
---

"""
    return header + text


def extract_images(qmd_path, outdir):
    qmd_path = Path(qmd_path)
    outdir = Path(outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    text = qmd_path.read_text(encoding="utf-8")

    # Match data:image/<format>;base64,<data>
    pattern = re.compile(r"data:image/([a-zA-Z0-9\+\.-]+);base64,([A-Za-z0-9+/=]+)")

    seen = {}
    count = 0

    def replace_image(match):
        nonlocal count
        fmt = match.group(1).lower()
        b64data = match.group(2)
        binary = base64.b64decode(b64data)

        # Create hash for deduplication
        h = hashlib.sha1(binary).hexdigest()
        filename = f"{PREFIX}-{h}.png"
        filepath = outdir / filename

        if h not in seen:
            seen[h] = filename
            # Convert to PNG (even if original is JPEG/WebP)
            try:
                if fmt == "svg+xml":
                    # Just save raw SVG without conversion
                    filename = f"{PREFIX}-{h}.svg"
                    filepath = outdir / filename
                    filepath.write_bytes(binary)
                else:
                    img = Image.open(BytesIO(binary))
                    img.save(filepath, format="PNG")
            except Exception as e:
                print(f"[WARN] Failed to process {fmt}: {e}")
                return match.group(0)  # leave as is if failed
            count += 1

        # Always return Unix-style path (forward slashes)
        return str(filepath.relative_to(qmd_path.parent)).replace("\\", "/")

    new_text = pattern.sub(replace_image, text)

    # Ensure YAML header
    new_text = ensure_yaml_header(new_text)

    # Backup original
    backup_path = qmd_path.with_suffix(qmd_path.suffix + ".bak")
    backup_path.write_text(text, encoding="utf-8")

    # Write updated QMD
    qmd_path.write_text(new_text, encoding="utf-8")

    print(f"✅ Extracted {count} unique images to '{outdir}'")
    print(f"💾 Backup saved as {backup_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: convert_pdf2qmd.py input.pdf")
        sys.exit(1)

    pdf_file = sys.argv[1]
    qmd_file = upload_pdf_and_download_qmd(pdf_file)

    qmd_path = Path(qmd_file)
    outdir = f"{qmd_path.stem}-media"

    extract_images(qmd_file, outdir)
