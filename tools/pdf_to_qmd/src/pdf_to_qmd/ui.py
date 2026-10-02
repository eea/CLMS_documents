"""Rich terminal UI for the pdf_to_qmd CLI.

One renderer (`RichUI`) for both single-file and batch runs — single is a batch of
one. A finished document's detail collapses to a one-line result row above the live
region, so a long batch stays scannable. Falls back to no-op `Events` when rich is
missing or stdout isn't a TTY (keeps pipes/CI clean).
"""

from .app import Events
from .cost import fmt_eur

try:
    from rich.console import Console, Group
    from rich.live import Live
    from rich.panel import Panel
    from rich.progress import (BarColumn, MofNCompleteColumn, Progress,
                               SpinnerColumn, TextColumn, TimeElapsedColumn)
    from rich.padding import Padding
    from rich.table import Table
    from rich.text import Text
    _RICH = True
except ImportError:
    _RICH = False

_ICON = {"ok": "[green]✔[/]", "warn": "[yellow]⚠[/]", "fail": "[red]✘[/]",
         "skip": "[grey58]⊘[/]"}
_VCOLOR = {"ok": "green", "warn": "yellow", "fail": "red", "skip": "grey58"}
_INDENT = 2          # left-indent the active-doc band off the screen edge
_BAND_FLOOR = 56     # min rule length, so rules aren't shorter than the live bars


_NAME_W = 48         # fixed width for the document-name column, so rows align
_METRICS_W = 16      # "N fig · M tbl" column width
_VER_W = 4           # verify-status column width (warn/fail/skip; ok is shorter)


def _clip(s: str, n: int) -> str:
    return s if len(s) <= n else s[:n - 1] + "…"


def _fit_name(name: str, width: int = _NAME_W) -> str:
    """Pad/truncate a filename to exactly `width` cells so the columns after it
    line up. Long names get a middle ellipsis — the prefix and the version/year
    suffix both stay visible (they're what tells two docs apart)."""
    if len(name) <= width:
        return name.ljust(width)
    keep = width - 1
    head = (keep + 1) // 2
    return name[:head] + "…" + name[len(name) - (keep - head):]


def _attention_reason(r) -> str:
    """Plain-text reason for a warn/fail/skip row: the first verify issue (with a
    +N for the rest), else the error, else a bare status."""
    if r.verify_issues:
        more = f"  (+{len(r.verify_issues) - 1} more)" if len(r.verify_issues) > 1 else ""
        return r.verify_issues[0]["summary"] + more
    if r.error:
        return r.error
    if r.verify_status and r.verify_status != "ok":
        return f"verify {r.verify_status}"
    return ""


def make_ui(batch: bool = False, console=None, force: bool = False):
    """Rich UI, or no-op Events when rich is missing or stdout isn't a TTY.
    `batch` is accepted for call-site compatibility; the UI adapts from events."""
    if not _RICH:
        return Events()
    con = console or Console()
    if not force and not con.is_terminal:
        return Events()
    return RichUI(con)


class RichUI(Events):
    wants_stream = True

    def __init__(self, console):
        self.con = console
        self._live = None
        self._init = None             # animated phase spinner until the doc's first tick
        self._init_task = None
        self._is_batch = False
        self._total = 1
        self._overall = self._otask = None
        # tallies + results for the final panel
        self._results = []
        self._done = self._warn = self._fail = self._skip = self._resumed = 0
        self._cost = 0.0
        self._reset_current()

    def _reset_current(self):
        self._name = ""
        self._est = None              # estimate line markup, or None
        self._setup = []              # chrome/cover/gate tick bits (one line)
        self._ticks = []              # detect/convert/render/verify result lines
        self._active = None           # live Progress during detect/convert
        self._figs = 0
        self._toks = self._clines = self._secs = self._tbls = 0
        self._dtask = self._ctask = None

    # ── rendering ──────────────────────────────────────────────────────────────

    def _band_width(self):
        """Rule length: the widest content line (so the rules just cover the band),
        floored so they never come up short of the live progress bars."""
        widths = [Text.from_markup(f"▸ {self._name} ").cell_len]
        if self._est:
            widths.append(Text.from_markup(self._est).cell_len)
        if self._setup:
            widths.append(Text.from_markup("  " + "   ".join(self._setup)).cell_len)
        widths += [Text.from_markup(t).cell_len for t in self._ticks]
        return min(max(max(widths), _BAND_FLOOR), self.con.width - 2 * _INDENT - 1)

    def _titled_rule(self, width):
        t = Text.from_markup(f"[b]▸ {self._name}[/] ")
        t.append("─" * max(0, width - t.cell_len), style="cyan")
        return t

    def _group(self):
        band = []
        if self._name:                    # titled rule opens the active-doc band,
            w = self._band_width()        # dim rule closes it; both indented + short
            band.append(self._titled_rule(w))
        if self._est:
            band.append(Text.from_markup(self._est))
        if self._setup:
            band.append(Text.from_markup("  " + "   ".join(self._setup)))
        band.extend(Text.from_markup(t) for t in self._ticks)
        if self._active is not None:
            band.append(self._active)
        # no determinate progress bar running → we're between phases (setup, the
        # cover/render/verify waits, etc). Show the moving phase spinner so the row
        # never looks frozen. The label is kept current via _set_phase.
        idle = self._active is None and self._name
        if idle and self._init is not None:
            band.append(self._init)
        if self._name:
            band.append(Text("─" * w, style="grey37"))

        parts = []
        if band:
            parts.append(Text(""))
            parts.append(Padding(Group(*band), (0, 0, 0, _INDENT)))
        if self._overall is not None:
            parts.append(Text(""))
            parts.append(self._overall)
            parts.append(Text(""))        # breathing room below the Documents bar
        return Group(*parts)

    def _refresh(self):
        if self._live:
            self._live.update(self._group())

    def _banner(self):
        from . import __version__
        t = Text()
        t.append("  ╔═╗  ", style="cyan")
        t.append("pdf2qmd", style="bold cyan")
        t.append(f"  v{__version__}\n", style="dim")
        t.append("  ╚═╝  ", style="cyan")
        t.append("AI-assisted PDF → Quarto (.qmd) conversion · CLMS Technical Library",
                 style="dim")
        return t

    def _start_live(self, header):
        self.con.print()
        self.con.print(self._banner())
        self.con.print()
        self.con.print(Panel(Text.from_markup(header), border_style="cyan",
                             expand=False, padding=(0, 2)))
        self.con.print()
        self._init = Progress(SpinnerColumn(style="cyan"),
                              TextColumn("[dim]{task.fields[phase]}[/]"))
        self._init_task = self._init.add_task("", total=None, phase="Estimating cost…")
        self._live = Live(console=self.con, refresh_per_second=14)
        self._live.start()
        self._refresh()

    # ── batch lifecycle ──────────────────────────────────────────────────────────

    def batch_start(self, pdfs):
        self._is_batch = True
        self._total = max(len(pdfs), 1)
        self._overall = Progress(
            TextColumn("[b]Documents[/]"),
            BarColumn(bar_width=24, complete_style="cyan", finished_style="green"),
            MofNCompleteColumn(), TextColumn("·  {task.fields[tally]}"),
            TimeElapsedColumn())
        self._otask = self._overall.add_task("", total=self._total, tally="[dim]€0.00[/]")
        noun = "document" if len(pdfs) == 1 else "documents"
        self._start_live(f"[b]batch[/] · {len(pdfs)} {noun}")

    def batch_done(self, results):
        self._finalize()

    # ── per-file ──────────────────────────────────────────────────────────────────

    def file_start(self, pdf, index, total):
        if self._live is None:        # single-file run: no overall bar
            self._total = total
            self._start_live(f"[b]converting[/] [dim]{pdf.name}[/]")
        self._reset_current()
        self._name = pdf.stem
        self._set_phase("Estimating cost…")   # reset label for each doc in a batch
        self._refresh()

    def _set_phase(self, text):
        """Update the inter-step spinner label to name the work now starting."""
        if self._init is not None and self._init_task is not None:
            self._init.update(self._init_task, phase=text)

    def estimate_done(self, est):
        rng = f"{fmt_eur(est['low_usd'])}–{fmt_eur(est['high_usd'])}"
        seed = "" if est.get("calibrated") else " [dim](seed)[/]"
        self._est = (f"  [cyan]≈[/] est [b]{fmt_eur(est['expected_usd'])}[/] "
                     f"[dim]({rng}; {est.get('pages', 0)}p, "
                     f"{est.get('candidate_pages', 0)} candidate)[/]{seed}")
        self._set_phase("Removing headers/footers…")
        self._refresh()

    def chrome_done(self, report):
        self._setup.append(f"[green]✔[/] headers [dim]({report.get('images_removed', 0)})[/]")
        self._set_phase("Reading cover page…")
        self._refresh()

    def cover_done(self, fields):
        title = (fields or {}).get("title") or "—"
        short = (title[:28] + "…") if len(title) > 29 else title
        self._setup.append(f"[green]✔[/] cover page [dim]{short}[/]")
        self._set_phase("Scanning pages…")
        self._refresh()

    def gate_done(self, n_candidates, n_skipped, total):
        self._setup.append(f"[green]✔[/] pages to scan [b]{n_candidates}/{total}[/]")
        self._set_phase("Detecting figures…")
        self._refresh()

    def detect_start(self, n_candidates):
        self._figs = 0
        self._active = Progress(
            SpinnerColumn(style="cyan"),
            TextColumn("[b]Detecting[/]"),
            BarColumn(bar_width=18, complete_style="green", finished_style="green"),
            MofNCompleteColumn(), TextColumn("· [green]{task.fields[figs]} fig[/]"),
            TimeElapsedColumn())
        self._dtask = self._active.add_task("", total=max(n_candidates, 1), figs=0)
        self._refresh()

    def detect_page(self, page_idx, n_figures):
        self._figs += n_figures
        if self._active and self._dtask is not None:
            self._active.update(self._dtask, advance=1, figs=self._figs)
        self._refresh()

    def detect_done(self, total_figures):
        self._ticks.append(f"  [green]✔[/] detected [b]{total_figures}[/] figure(s)")
        self._active = self._dtask = None
        self._set_phase("Converting to .qmd…")
        self._refresh()

    def convert_start(self):
        self._toks = self._clines = self._secs = self._tbls = 0
        self._active = Progress(
            SpinnerColumn(style="cyan"),
            TextColumn("[b]Converting → .qmd[/]"),
            BarColumn(bar_width=18, pulse_style="cyan"),
            TextColumn("{task.fields[info]}"),
            TimeElapsedColumn())
        self._ctask = self._active.add_task("", total=None, info="[dim]…[/]")
        self._refresh()

    def convert_delta(self, chunk):
        self._toks += max(1, len(chunk) // 4)
        self._clines += chunk.count("\n")
        self._secs += chunk.count("## ")
        self._tbls += chunk.count("Table ")     # rough: counts caption + prose refs alike
        if self._active and self._ctask is not None:
            self._active.update(self._ctask, info=f"[dim]~{self._toks:,} tok · "
                                f"{self._clines} lines · {self._secs} sections · "
                                f"{self._tbls} tables[/]")
        self._refresh()

    def convert_done(self):
        self._ticks.append("  [green]✔[/] converted → .qmd")
        self._active = self._ctask = None
        self._set_phase("Fixing tables…")
        self._refresh()

    def tablefix_done(self, summary):
        bits = []
        if summary.get("tables_oriented"):
            bits.append(f"{summary['tables_oriented']} landscape")
        restructured = summary.get("grid_normalized", 0) + summary.get("tables_unwrapped", 0)
        if restructured:
            bits.append(f"{restructured} grid-fixed")
        captions = (summary.get("captions_moved", 0) + summary.get("captions_normalized", 0)
                    + summary.get("captions_redistributed", 0))
        if captions:
            bits.append(f"{captions} captioned")
        if bits:                                 # stay quiet when nothing changed
            self._ticks.append("  [green]✔[/] tables — " + " · ".join(bits))
            self._refresh()

    def render_start(self):
        self._set_phase("Rendering PDF…")
        self._refresh()

    def render_done(self, ok):
        self._ticks.append("  [green]✔[/] rendered PDF" if ok else "  [red]✘[/] render failed")
        self._refresh()

    def verify_start(self):
        self._set_phase("Verifying content…")
        self._refresh()

    def verify_done(self, status):
        self._ticks.append(f"  {_ICON.get(status, '[yellow]⚠[/]')} "
                           f"verify [{_VCOLOR.get(status, 'yellow')}]{status}[/]")
        self._set_phase("Finishing…")
        self._refresh()

    def file_done(self, result):
        self._done += 1
        self._warn += result.status == "warn"
        self._fail += result.status == "fail"
        self._skip += result.status == "skip"
        self._resumed += bool(result.resumed)
        self._cost += result.cost_usd or 0.0
        self._results.append(result)
        if self._is_batch:
            # collapse this file's detail to a permanent row above the live region
            self._print_row(result)
            self._reset_current()
            if self._overall:
                self._overall.update(self._otask, advance=1, tally=self._tally())
            self._refresh()
        else:
            self._finalize()

    # ── helpers ──────────────────────────────────────────────────────────────────

    def _print_row(self, r):
        name = _fit_name(r.stem)
        if r.resumed:
            row = f"[grey58]↻ {name}   already done[/]"
        elif r.status == "skip":
            est = f"  [grey58]est {fmt_eur(r.est_usd)}[/]" if r.est_usd else ""
            row = f"{_ICON['skip']} [grey58]{name}   skipped[/]{est}"
        else:
            ver = r.verify_status or r.status
            # pad the metrics + verify columns (their widths vary with counts and
            # ok/warn/fail) so the cost lines up across rows
            metrics = f"{r.figures} fig" + (f" · {r.tables} tbl" if r.tables else "")
            metrics = metrics.ljust(_METRICS_W)
            ver_cell = f"[{_VCOLOR.get(ver, 'green')}]{ver}[/]" + " " * max(0, _VER_W - len(ver))
            row = (f"{_ICON.get(r.status, '')} [b]{name}[/]   {metrics}   "
                   f"{ver_cell}   [dim]{fmt_eur(r.cost_usd)}[/]")
        self.con.print(Text.from_markup("  " + row))
        # why it's warn/fail — one dim sub-line per non-ok check, so the status is
        # assessable without opening verify_report.md
        for iss in r.verify_issues or []:
            t = Text.from_markup(f"      {_ICON.get(iss['status'], '[yellow]⚠[/]')} ")
            t.append(_clip(iss["summary"], 74), style="dim")
            self.con.print(t)

    def _tally(self):
        ok = self._done - self._warn - self._fail - self._skip
        bits = [f"[green]✔{ok}[/]"]
        if self._warn:
            bits.append(f"[yellow]⚠{self._warn}[/]")
        if self._fail:
            bits.append(f"[red]✘{self._fail}[/]")
        if self._skip:
            bits.append(f"[grey58]⊘{self._skip}[/]")
        bits.append(f"[dim]{fmt_eur(self._cost)}[/]")
        return "  ".join(bits)

    def abort(self):
        """Ctrl+C: stop the live region so the cursor/terminal is restored. No
        summary panel — the run didn't finish."""
        if self._live:
            self._live.stop()
            self._live = None

    def _finalize(self):
        if self._live:
            self._live.stop()
            self._live = None
        self.con.print(self._summary_panel())
        self.con.print()

    def _summary_panel(self):
        results = self._results
        batch = self._is_batch or self._total > 1
        ok = self._done - self._warn - self._fail - self._skip - self._resumed
        t = Table(show_header=False, box=None, pad_edge=False)
        t.add_column(style="dim", justify="right", no_wrap=True)
        t.add_column()

        if batch:
            line = (f"{self._done}   [green]✔{ok} ok[/]   "
                    f"[yellow]⚠{self._warn} warn[/]   [red]✘{self._fail} fail[/]")
            if self._skip:
                line += f"   [grey58]⊘{self._skip} skip[/]"
            if self._resumed:
                line += f"   [grey58]↻{self._resumed} already done[/]"
            t.add_row("documents", line)
        elif results:
            r = results[0]
            t.add_row("document", r.stem)
            if r.text_cov is not None:
                t.add_row("text", f"[dim]{r.text_cov}% coverage[/]")
            if r.verify_status:
                t.add_row("verify", f"[{_VCOLOR.get(r.verify_status, 'yellow')}]{r.verify_status}[/]")
            for iss in r.verify_issues or []:    # the why, so warn/fail is assessable here
                cell = Text.from_markup(f"{_ICON.get(iss['status'], '[yellow]⚠[/]')} ")
                cell.append(_clip(iss["summary"], 64), style="dim")
                t.add_row("", cell)
            if r.error:
                t.add_row("note", f"[yellow]{r.error}[/]")

        n_tbl = sum(r.tables for r in results)
        cov = None if batch else (results[0].table_cov if results else None)
        t.add_row("figures", f"[green]{sum(r.figures for r in results)} placed[/]")
        t.add_row("tables", f"[green]{n_tbl}[/]"
                  + (f"   [dim]{cov}% word coverage[/]" if cov is not None else ""))
        t.add_row("cost", f"[b]{fmt_eur(self._cost)}[/]")

        attention = [r for r in results if r.status in ("warn", "fail", "skip")]
        if batch and attention:
            t.add_row("", "")
            for r in attention:
                cell = Text.from_markup(f"{_ICON.get(r.status, '')} ")
                cell.append(r.stem, style="bold")
                cell.append(" — ", style="dim")
                cell.append(_clip(_attention_reason(r), 58), style="dim")
                t.add_row("attention", cell)
        elif not batch and results:
            t.add_row("output", f"[dim]{results[0].out_dir}[/]")

        title = "[b green]✔ Batch complete[/]" if batch else (
            f"{_ICON.get(results[0].status, '') if results else ''} done")
        border = "red" if self._fail else "green"
        return Panel(t, title=title, border_style=border, expand=False, padding=(0, 2))
