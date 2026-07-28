# Git workflow for AI agents

How an AI agent working **directly in the Technical Library repo** should use git.
This is the on-demand detail; the non-negotiable rules also live in
[`AGENTS.md`](../AGENTS.md) under "Guardrails" and always apply. You are not in a
downstream project's `DOCS/` subtree — the `git docs-*` aliases from the human
Editor Guide do not apply here; use plain git.

## When to touch git

Don't commit or push unless the user explicitly asks. Make and verify your edits,
let the user review, then act on request.

## Always: feature branch + pull request

**Never commit directly to `develop` or `main`.** When asked to commit:

1. Cut a branch off `develop`, named by change type: `feat/<topic>`,
   `fix/<topic>`, `docs/<topic>`.
2. Make your commits (grouping rules below).
3. `git push -u origin <branch>`.
4. Open the PR with the **GitHub CLI**:
   `gh pr create --base develop --title "<type>: …" --body "…"`.

`gh` is already authenticated — do **not** hand-roll GitHub REST/API calls,
personal tokens, or other ad-hoc methods. If `gh` isn't installed or
authenticated, stop and ask the user; don't improvise a fallback.

The PR is the human review gate that catches anything the automated guardrails
miss — so this holds even for a small or "obviously safe" change.

## Grouping commits

- **Group commits by concern, not by keystroke.** Each commit is one coherent,
  self-contained change to one area — a pipeline-script change and a docs change
  are separate commits; a single change spanning many files is one commit — and
  must leave the tree working with the gate passing.
- Aim for the fewest commits that stay coherent: never a monolithic "everything"
  commit, never a commit per file or per small edit.
- **Keep the branch history clean.** Squash local WIP / "fix typo" / "address
  review" churn into the meaningful commits before opening the PR, so the history
  reads as deliberate steps.

## Commit messages — Conventional Commits

They drive semantic-release on `main`.

- Subject: `<type>: <imperative summary>`, ≤ ~50 chars, no trailing period —
  e.g. `fix: correct HRL Forest PUM coverage table`.
- Pick the type by release impact: `feat` / `fix` bump the version; `docs`,
  `chore`, `refactor`, `test` don't. Use `!` / `BREAKING CHANGE:` only for a
  genuine breaking change.
- Add a body (after a blank line) when the change isn't self-evident — explain
  **why**, not just what. Reference the affected product/doc.

## Before and around committing

- **Verify first:** `validate_qmd_files.py` (plus `ruff` / a single
  `quarto render` when relevant) must pass — never commit a red gate.
- **Stage deliberately** (`git add <paths>`, not `git add -A`). Never commit
  generated output (`_site/`, per-doc `.html` / `.pdf`, `.quarto/`) — it's
  gitignored; keep it that way.
- **Don't rewrite *shared* history** — tidying your own un-pushed feature branch
  (squash/amend before its first push) is fine; never `--amend` or force-push
  `develop`, `main`, or commits others may have built on.
- **Never use `[skip ci]`** to bypass validation — it's reserved for the release
  bot.
