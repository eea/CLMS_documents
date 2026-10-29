# pdf2qmd

Convert a PDF document into a Quarto `.qmd` — detecting figures, transcribing the
body with an LLM, fixing tables, rendering a PDF, and verifying fidelity, in one
command. Built for the CLMS Technical Library, but standalone.

```bash
python3 tools/pdf_to_qmd/pdf2qmd.py FILE.pdf        # one document
python3 tools/pdf_to_qmd/pdf2qmd.py inbox/          # batch: every *.pdf in inbox/
```

Each run writes `output/<doc>/` containing `<doc>.qmd`, the rendered `<doc>.pdf`,
and a verify report.

## Install

```bash
python3 -m pip install -r tools/pdf_to_qmd/requirements.txt
```

Also required, but not pip-installable: the **Quarto CLI** (for the PDF render;
skip with `--no-render`) and an **`OPENROUTER_API_KEY`** (see [Environment](#environment)).

## Options

| Option | What it does | Default |
|---|---|---|
| `path` | A PDF file, or a directory of PDFs (batch mode). | *(required)* |
| `--out OUT` | Output root directory. | `output/` |
| `--model MODEL` | OpenRouter model for figure detection + body convert. | `$OPENROUTER_MODEL` or `google/gemini-2.5-pro` |
| `--cover-model MODEL` | Model for the cover-page metadata extraction. | `google/gemini-2.5-flash` |
| `--no-render` | Skip the Typst PDF render. | render runs |
| `--no-verify` | Skip the content-fidelity verify pass. | verify runs |
| `--force` | Overwrite an existing `output/<doc>/` instead of skipping it. | skip if done |
| `--detect-workers N` | Concurrent per-page figure-detection calls (Phase 1). See [Detection concurrency](#detection-concurrency). | `8` |
| `--max-cost-per-file EUR` | Skip a file whose pre-flight estimate exceeds this. | no gate |
| `--max-cost-total EUR` | Batch backstop: stop before a file that would push cumulative spend past this. | no gate |
| `--allow-over-budget` | Convert regardless of the estimate (overrides both cost gates). | off |
| `--dry-run` | Replay the UI from an existing output dir — no LLM, no cost. Point it at a folder of raw PDFs instead and it shows mock data. | off |
| `--delay SECONDS` | Per-step pause in `--dry-run` replay. | `0.12` |
| `--quiet` | Plain logging, no rich UI. | rich UI |
| `--verbose` | DEBUG logging. | INFO |
| `-h`, `--help` | Show usage and exit. | — |

## How it works

```
      PDF
       │
       ▼
  pre-flight estimate          pages · candidate pages · cost   (no LLM)
       │                       gated by --max-cost-* before any spend
       ▼
 ┌─ Phase 1 · Detect ─────────────────────────────────────────────┐
 │                                                                │
 │   strip headers/footers  →  read cover page  →  gate pages  →  │
 │   per-page figure detection (LLM vision, --detect-workers N)   │
 │                                                                │
 └────────────────────────────────────────────────────────────────┘
       │   cover → .qmd frontmatter;  figures cropped to <doc>-media/
       ▼
 ┌─ Phase 2 · Convert ────────────────────────────────────────────┐
 │                                                                │
 │   one streamed LLM call transcribes the body  →  <doc>.qmd     │
 │                                                                │
 └────────────────────────────────────────────────────────────────┘
       │
       ▼
 ┌─ Phase 2.5 · Table fixes ──────────────────────────────────────┐
 │                                                                │
 │   deterministic: grid normalize · column widths · captions ·   │
 │   wide-table landscape/orientation   (no LLM, value-safe)      │
 │                                                                │
 └────────────────────────────────────────────────────────────────┘
       │
       ▼
 ┌─ Phase 3 · Render ─────────────────────────────────────────────┐
 │                                                                │
 │   Quarto + Typst  →  <doc>.pdf                                 │
 │                                                                │
 └────────────────────────────────────────────────────────────────┘
       │
       ▼
 ┌─ Phase 4 · Verify ─────────────────────────────────────────────┐
 │                                                                │
 │   content fidelity: text coverage + table coverage  →  report  │
 │                                                                │
 └────────────────────────────────────────────────────────────────┘
       │
       ▼
   output/<doc>/    <doc>.qmd · <doc>.pdf · verify_report.md · <doc>-media/
```

Re-running the same command **resumes**: completed documents are skipped (use
`--force` to redo). The cost gates check a free, local estimate *before* spending.

## Detection concurrency

Phase 1 runs one LLM vision call **per candidate page**; `--detect-workers`
controls how many run at once. The default is **8**, chosen from the workload
rather than the machine's CPU count — these calls are network-bound (each waits on
the Gemini API), so cores are the wrong sizing signal.

Sizing rationale (measured on a real run, `gemini-2.5-pro`, 150-dpi pages):
- ~4–6k tokens and ~$0.018 per page; call latency ~10–20 s (a *thinking* model).
- Detection runs in *waves* of `min(workers, candidate_pages)`. Most docs have
  ~8–15 candidate pages, so 8 clears a typical doc in one or two waves — past that,
  extra workers just sit idle (capped by the page count).
- The only ceiling that bites at single-digit workers is **requests-per-minute**.
  At 8 workers and ~15 s/call that's ~32 req/min — well under Gemini's paid-tier
  limits (~150 RPM on tier 1). Tokens-per-minute and provider concurrency never
  bind at this scale, and the 429 retry/backoff absorbs the occasional overshoot.

Note: detection is the *minority* of wall-clock — the single Phase 2 convert call
dominates — so raising this past 8 yields little end-to-end gain. Raise it on a
higher API tier only for unusually figure-heavy documents; drop to `1` for strictly
sequential, rate-limit-safe runs.

## Environment

| Variable | Required | Purpose |
|---|---|---|
| `OPENROUTER_API_KEY` | yes | API key for the detect + convert calls. |
| `OPENROUTER_MODEL` | no | Default model, overridden by `--model`. |

```bash
export OPENROUTER_API_KEY=sk-or-...
```

## Output layout

```
output/
└── <doc>/
    ├── <doc>.qmd              the converted Quarto document
    ├── <doc>.pdf              rendered PDF (unless --no-render)
    ├── <doc>-media/           cropped figures
    ├── verify_report.md       fidelity check, human-readable (unless --no-verify)
    ├── <doc>.source.pdf       the input, copied in (self-contained run)
    └── *.json                 per-phase sidecars: phase1, detections, result, verify
```

## Examples

```bash
# Fast batch: parallel detection, skip the verify pass
python3 tools/pdf_to_qmd/pdf2qmd.py inbox/ --detect-workers 6 --no-verify

# Cap spend, and don't convert anything pricier than €2 per file
python3 tools/pdf_to_qmd/pdf2qmd.py inbox/ --max-cost-per-file 2 --max-cost-total 20

# Preview the UI on a finished run — free, no API calls
python3 tools/pdf_to_qmd/pdf2qmd.py output/ --dry-run
```
