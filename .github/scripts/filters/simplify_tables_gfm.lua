-- Simplify raw-HTML tables in the gfm (.llms.md) output ONLY.
--
-- Complex tables (merged cells) are emitted as raw `<table>` HTML so the PDF/HTML
-- renders keep their layout. But the .llms.md companion feeds a RAG (Onyx), whose
-- ingestion reads markdown as PLAIN TEXT and embeds it with a bi-encoder — so the
-- inline presentational markup (`style="background-color:…"`, `class`, `colgroup`
-- widths, `data-quarto-postprocess`) is pure token noise that dilutes retrieval.
--
-- STAGE C (this filter, for now): strip the presentational attributes/elements but
-- keep the structural tags (table/tr/td/th, colspan/rowspan). Stage A will extend
-- this to full row-linearization for the merged-cell tables.
--
-- Wired under `gfm.filters` only, so HTML and Typst/PDF outputs are untouched. The
-- FORMAT guard is belt-and-suspenders in case the filter is ever mis-wired.

local function is_markdown_target()
  return FORMAT:match("gfm") or FORMAT:match("commonmark") or FORMAT:match("markdown")
end

-- Remove one HTML attribute (name="...") everywhere it appears.
local function strip_attr(html, name)
  return (html:gsub('%s+' .. name .. '%s*=%s*"[^"]*"', ""))
end

local function simplify_table_html(html)
  -- drop the whole <colgroup>…</colgroup> (pure column-width layout)
  html = html:gsub("<colgroup.-</colgroup>%s*", "")
  -- drop presentational / tooling attributes; keep colspan, rowspan, scope
  for _, attr in ipairs({ "style", "class", "bgcolor", "align", "valign",
                          "width", "height", "data%-quarto%-postprocess" }) do
    html = strip_attr(html, attr)
  end
  -- also drop any other data-* attribute
  html = html:gsub('%s+data%-[%w%-]+%s*=%s*"[^"]*"', "")
  return html
end

function RawBlock(el)
  if not is_markdown_target() then
    return el
  end
  if el.format:match("html") then
    local trimmed = el.text:gsub("^%s+", ""):gsub("%s+$", "")
    -- drop bare layout `<div …>` / `</div>` wrappers (e.g. the overflow-x scroll
    -- wrapper) — pure presentation, and they orphan once their table is linearized
    if trimmed:match("^</?div[^>]*>$") then
      return {}
    end
    if el.text:match("<table") then
      el.text = simplify_table_html(el.text)
      return el
    end
  end
  return el
end

-- Native pandoc Tables. A SIMPLE table renders as a clean gfm pipe table — we just
-- strip its styling (Stage C). A COMPLEX table (colspan/rowspan/multi-row header)
-- can't be a pipe table, so the writer would fall back to raw HTML; instead we
-- LINEARIZE it (Stage A) — each data row becomes a self-describing bullet carrying
-- its column-header context, so the row survives 512-token chunking and embeds as
-- clean prose for the RAG (Onyx reads .md as plain text + bi-encoder).

local function clear_cell_attrs(rows)
  for _, row in ipairs(rows) do
    for _, cell in ipairs(row.cells) do
      cell.attr = pandoc.Attr()
    end
  end
end

local function destyle(el)
  local specs = {}
  for _, spec in ipairs(el.colspecs) do
    table.insert(specs, { spec[1], nil })
  end
  el.colspecs = specs
  el.attr = pandoc.Attr()
  clear_cell_attrs(el.head.rows)
  for _, body in ipairs(el.bodies) do
    clear_cell_attrs(body.head)
    clear_cell_attrs(body.body)
  end
  clear_cell_attrs(el.foot.rows)
  return el
end

local function is_complex(el)
  if #el.head.rows > 1 then return true end          -- multi-row header
  local function spanned(rows)
    for _, row in ipairs(rows) do
      for _, cell in ipairs(row.cells) do
        if (cell.col_span or 1) > 1 or (cell.row_span or 1) > 1 then return true end
      end
    end
    return false
  end
  if spanned(el.head.rows) then return true end
  for _, body in ipairs(el.bodies) do
    if spanned(body.head) or spanned(body.body) then return true end
  end
  return spanned(el.foot.rows)
end

-- Expand a list of Rows into a dense grid (string per cell), filling colspan across
-- columns and rowspan down rows — the standard HTML table-grid algorithm.
local function gridify(rows)
  local grid, carries = {}, {}
  for r = 1, #rows do
    grid[r] = {}
    for col, car in pairs(carries) do
      grid[r][col] = car.text
      car.remaining = car.remaining - 1
      if car.remaining <= 0 then carries[col] = nil end
    end
    local c = 1
    for _, cell in ipairs(rows[r].cells) do
      while grid[r][c] ~= nil do c = c + 1 end
      local text = pandoc.utils.stringify(cell.contents):gsub("%s+", " "):gsub("^%s*(.-)%s*$", "%1")
      local cs, rs = (cell.col_span or 1), (cell.row_span or 1)
      for k = 0, cs - 1 do
        grid[r][c + k] = text
        if rs > 1 then carries[c + k] = { text = text, remaining = rs - 1 } end
      end
      c = c + cs
    end
  end
  return grid
end

local function ncols(grid)
  local n = 0
  for _, row in ipairs(grid) do
    for c in pairs(row) do if c > n then n = c end end
  end
  return n
end

-- Column header label = the header-grid values for that column joined down the header
-- rows (e.g. "Blind / 2012"), de-duplicated.
local function column_headers(hgrid, n)
  local headers = {}
  for c = 1, n do
    local parts, seen = {}, {}
    for r = 1, #hgrid do
      local v = hgrid[r][c]
      if v and v ~= "" and not seen[v] then
        seen[v] = true
        table.insert(parts, v)
      end
    end
    headers[c] = table.concat(parts, " / ")
  end
  return headers
end

local function linearize(el)
  local hgrid = gridify(el.head.rows)
  local body_rows = {}
  for _, body in ipairs(el.bodies) do
    for _, r in ipairs(body.head) do table.insert(body_rows, r) end
    for _, r in ipairs(body.body) do table.insert(body_rows, r) end
  end
  local bgrid = gridify(body_rows)
  local n = math.max(ncols(hgrid), ncols(bgrid))
  local headers = column_headers(hgrid, n)

  local items = {}
  for r = 1, #bgrid do
    local row = bgrid[r]
    -- a full-width section/banner row (one distinct value across all columns)
    local distinct = {}
    for c = 1, n do if row[c] and row[c] ~= "" then distinct[row[c]] = true end end
    local ndist = 0
    for _ in pairs(distinct) do ndist = ndist + 1 end
    if ndist == 1 and (row[1] and row[1] ~= "") then
      table.insert(items, pandoc.Plain({ pandoc.Strong(pandoc.Str(row[1])) }))
    else
      local label = (row[1] and row[1] ~= "") and row[1] or nil
      local pairs_txt = {}
      for c = (label and 2 or 1), n do
        local v = row[c]
        if v and v ~= "" then
          local h = headers[c]
          table.insert(pairs_txt, (h and h ~= "") and (h .. ": " .. v) or v)
        end
      end
      local line = (label and ("**" .. label .. "** — ") or "") .. table.concat(pairs_txt, "; ")
      if line ~= "" then
        table.insert(items, pandoc.Plain(pandoc.read(line, "markdown").blocks[1].content))
      end
    end
  end

  local blocks = {}
  local caption = el.caption and pandoc.utils.stringify(el.caption.long or {})
  if caption and caption ~= "" then
    table.insert(blocks, pandoc.Para({ pandoc.Emph(pandoc.Str(caption)) }))
  end
  if #items > 0 then
    table.insert(blocks, pandoc.BulletList(items))
  end
  return blocks
end

-- Fenced divs (`::: {#tbl-…}` table-figure wrappers, etc.) would be emitted as
-- `<div id=…>` by the gfm writer — pure structural noise in plain-text .llms.md.
-- Unwrap them to their inner blocks; for RAG the crossref anchor is irrelevant.
function Div(el)
  if not is_markdown_target() then
    return el
  end
  return el.content
end

-- Quarto wraps a captioned table in a crossref float (a Figure with a #tbl- id);
-- the gfm writer emits it as `<div id="tbl-…">`. Unwrap to the inner blocks (the
-- linearized rows + caption) so no bare wrapper div lands in the .llms.md.
function Figure(el)
  if not is_markdown_target() then
    return el
  end
  return el.content
end

function Table(el)
  if not is_markdown_target() then
    return el
  end
  if is_complex(el) then
    local ok, blocks = pcall(linearize, el)
    if ok and blocks and #blocks > 0 then
      return blocks
    end
    return destyle(el)        -- linearization failed → fall back to clean HTML
  end
  return destyle(el)
end
