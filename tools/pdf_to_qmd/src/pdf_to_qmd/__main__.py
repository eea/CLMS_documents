"""`python3 -m pdf_to_qmd FILE.pdf` entry point (the production two-pass flow)."""

import sys

from .app_cli import main

if __name__ == "__main__":
    sys.exit(main())
