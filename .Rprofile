# CLMS Technical Library — local PDF preview font setup.
#
# Makes the bundled Typst fonts (_meta/theme/typst-fonts/) discoverable so that
# rendering a DOCS/*.qmd to PDF — e.g. via the RStudio "Render" button — uses the
# CLMS fonts (Lato, Liberation Sans, JetBrains Mono) without installing anything
# system-wide. Quarto's typst format has no font-path option, so we set Typst's
# native TYPST_FONT_PATHS env var here; RStudio runs this file on session start,
# and the quarto render it launches inherits the variable.
#
# Preview only — the CI build (build-docs.sh) does not use this.
local({
  font_dir <- normalizePath(
    file.path(getwd(), "_meta", "theme", "typst-fonts"),
    mustWork = FALSE
  )
  if (dir.exists(font_dir)) {
    existing <- Sys.getenv("TYPST_FONT_PATHS")
    paths <- if (nzchar(existing)) {
      strsplit(existing, .Platform$path.sep, fixed = TRUE)[[1]]
    } else {
      character(0)
    }
    if (!(font_dir %in% paths)) {
      Sys.setenv(
        TYPST_FONT_PATHS = paste(c(font_dir, paths), collapse = .Platform$path.sep)
      )
      message("CLMS: TYPST_FONT_PATHS set to bundled fonts for local PDF preview.")
    }
  }
})
