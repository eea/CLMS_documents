-- inject-image-descriptions.lua
--
-- Adds LLM-generated descriptions to images. Descriptions are produced by
-- .github/scripts/ai/describe_images.py and cached as JSON files under
-- .llm_cache/images/<md5>.json (key = md5 of image file bytes).
--
-- Per output format:
--   html / docx / latex (pdf):
--       sets attributes["fig-alt"] (becomes the <img alt>) and the image
--       title (becomes <img title>, browser tooltip on hover). Descriptions
--       are NOT visible to readers, but readable by screen readers, search
--       engines, and LLM crawlers.
--   markdown writers (gfm / commonmark / markdown) — used by Quarto for the
--       .llms.md sidecar companions:
--       appends a Para after each block containing an image so the description
--       is visible plain text in the .llms.md file (which is what LLM
--       consumers reading the sitemap-llm.xml end up parsing).
--
-- The visible figure caption (the [...] slot in markdown image syntax) is
-- NEVER touched — it stays as the figcaption that produces "Fig. 1 …".

-- Locate .llm_cache/images relative to this filter file. The filter lives at
-- <repo>/.github/scripts/filters/inject-image-descriptions.lua, so the repo
-- root is four directory levels up. This avoids any assumption about Quarto's
-- cwd at render time.
local function compute_cache_dir()
  local src = debug.getinfo(1, "S").source
  if src:sub(1, 1) == "@" then src = src:sub(2) end
  -- Walk up: filter file → filters/ → scripts/ → .github/ → repo root
  local dir = src
  for _ = 1, 4 do
    dir = dir:match("^(.+)/[^/]*$") or dir
  end
  return dir .. "/.llm_cache/images"
end
local CACHE_DIR = compute_cache_dir()
io.stderr:write("[inject-image-descriptions] cache dir resolved to: " .. CACHE_DIR .. "\n")


-- ─── md5 (pure Lua, no external deps) ─────────────────────────────────────
-- Matches Python's hashlib.md5 — verified against RFC 1321 test vectors and
-- md5sum output. Implementation requires Lua 5.3+ for native bitwise ops,
-- which Pandoc 3+ (Quarto 1.5+) provides.

local T = {
  0xd76aa478, 0xe8c7b756, 0x242070db, 0xc1bdceee,
  0xf57c0faf, 0x4787c62a, 0xa8304613, 0xfd469501,
  0x698098d8, 0x8b44f7af, 0xffff5bb1, 0x895cd7be,
  0x6b901122, 0xfd987193, 0xa679438e, 0x49b40821,
  0xf61e2562, 0xc040b340, 0x265e5a51, 0xe9b6c7aa,
  0xd62f105d, 0x02441453, 0xd8a1e681, 0xe7d3fbc8,
  0x21e1cde6, 0xc33707d6, 0xf4d50d87, 0x455a14ed,
  0xa9e3e905, 0xfcefa3f8, 0x676f02d9, 0x8d2a4c8a,
  0xfffa3942, 0x8771f681, 0x6d9d6122, 0xfde5380c,
  0xa4beea44, 0x4bdecfa9, 0xf6bb4b60, 0xbebfbc70,
  0x289b7ec6, 0xeaa127fa, 0xd4ef3085, 0x04881d05,
  0xd9d4d039, 0xe6db99e5, 0x1fa27cf8, 0xc4ac5665,
  0xf4292244, 0x432aff97, 0xab9423a7, 0xfc93a039,
  0x655b59c3, 0x8f0ccc92, 0xffeff47d, 0x85845dd1,
  0x6fa87e4f, 0xfe2ce6e0, 0xa3014314, 0x4e0811a1,
  0xf7537e82, 0xbd3af235, 0x2ad7d2bb, 0xeb86d391,
}
local S = {
  7,12,17,22, 7,12,17,22, 7,12,17,22, 7,12,17,22,
  5, 9,14,20, 5, 9,14,20, 5, 9,14,20, 5, 9,14,20,
  4,11,16,23, 4,11,16,23, 4,11,16,23, 4,11,16,23,
  6,10,15,21, 6,10,15,21, 6,10,15,21, 6,10,15,21,
}

local function rotl(x, n)
  x = x & 0xFFFFFFFF
  return ((x << n) | (x >> (32 - n))) & 0xFFFFFFFF
end

local function band_not(x)
  return (~x) & 0xFFFFFFFF
end

local function md5_string(message)
  local A0, B0, C0, D0 = 0x67452301, 0xEFCDAB89, 0x98BADCFE, 0x10325476
  local len = #message
  local pad_len = (55 - len) % 64
  local padded = message
    .. string.char(0x80)
    .. string.rep(string.char(0), pad_len)
    .. string.pack("<I8", len * 8)

  for chunk_start = 1, #padded, 64 do
    local M = {}
    for j = 0, 15 do
      M[j] = string.unpack("<I4", padded, chunk_start + j * 4)
    end
    local A, B, C, D = A0, B0, C0, D0
    for i = 0, 63 do
      local F, g
      if i < 16 then
        F = (B & C) | (band_not(B) & D)
        g = i
      elseif i < 32 then
        F = (D & B) | (band_not(D) & C)
        g = (5 * i + 1) % 16
      elseif i < 48 then
        F = B ~ C ~ D
        g = (3 * i + 5) % 16
      else
        F = C ~ (B | band_not(D))
        g = (7 * i) % 16
      end
      local temp = D
      D = C
      C = B
      B = (B + rotl((A + F + T[i + 1] + M[g]) & 0xFFFFFFFF, S[i + 1])) & 0xFFFFFFFF
      A = temp
    end
    A0 = (A0 + A) & 0xFFFFFFFF
    B0 = (B0 + B) & 0xFFFFFFFF
    C0 = (C0 + C) & 0xFFFFFFFF
    D0 = (D0 + D) & 0xFFFFFFFF
  end

  return string.format(
    "%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x%02x",
    A0 & 0xFF, (A0 >> 8) & 0xFF, (A0 >> 16) & 0xFF, (A0 >> 24) & 0xFF,
    B0 & 0xFF, (B0 >> 8) & 0xFF, (B0 >> 16) & 0xFF, (B0 >> 24) & 0xFF,
    C0 & 0xFF, (C0 >> 8) & 0xFF, (C0 >> 16) & 0xFF, (C0 >> 24) & 0xFF,
    D0 & 0xFF, (D0 >> 8) & 0xFF, (D0 >> 16) & 0xFF, (D0 >> 24) & 0xFF
  )
end


-- ─── helpers ──────────────────────────────────────────────────────────────

local function md5_of_file(path)
  local f = io.open(path, "rb")
  if not f then return nil end
  local content = f:read("*a")
  f:close()
  return md5_string(content)
end


-- Parse a tiny JSON file of the shape:
--   {"image_type": "...", "description": "..."}
-- Prefer pandoc.json (Pandoc 3+); fall back to a pattern that handles the
-- json.dump output of describe_images.py (which uses ensure_ascii=False and
-- escapes \", \n, \\).
local function parse_description(content)
  local ok, data = pcall(function() return pandoc.json.decode(content) end)
  if ok and type(data) == "table" and data.description then
    return data.description
  end
  local desc = content:match('"description"%s*:%s*"(.-)"%s*}%s*$')
  if not desc then return nil end
  -- Unescape JSON string escapes that describe_images.py is known to produce.
  return desc
    :gsub('\\n', '\n')
    :gsub('\\"', '"')
    :gsub('\\\\', '\\')
end


-- Per-render cache so we hit each .json file at most once.
local desc_by_md5 = {}

local function load_description(md5)
  if desc_by_md5[md5] ~= nil then
    return desc_by_md5[md5] or nil
  end
  local f = io.open(CACHE_DIR .. "/" .. md5 .. ".json", "r")
  if not f then
    desc_by_md5[md5] = false
    return nil
  end
  local content = f:read("*a")
  f:close()
  local desc = parse_description(content or "")
  desc_by_md5[md5] = desc or false
  return desc
end


-- Resolve an Image src to a local file path readable from cwd.
-- Returns nil for remote URLs or files we can't find on disk.
local function resolve_image_path(src)
  if src:match("^https?://") or src:match("^data:") then return nil end

  -- URL-decode (%20 etc.)
  src = src:gsub("%%(%x%x)", function(h) return string.char(tonumber(h, 16)) end)

  -- Absolute path
  if src:sub(1, 1) == "/" then
    local f = io.open(src, "rb")
    if f then f:close(); return src end
    return nil
  end

  -- Try as-is (relative to cwd).
  local f = io.open(src, "rb")
  if f then f:close(); return src end

  -- Otherwise resolve relative to the input .qmd's directory.
  local input_files = PANDOC_STATE and PANDOC_STATE.input_files
  if input_files and input_files[1] then
    local doc_dir = tostring(input_files[1]):match("^(.*[/\\])")
    if doc_dir then
      local candidate = doc_dir .. src
      f = io.open(candidate, "rb")
      if f then f:close(); return candidate end
    end
  end
  return nil
end


-- Format detection: which writer is producing the current output?
local function is_markdown_writer()
  if not FORMAT then return false end
  return FORMAT == "gfm"
      or FORMAT == "commonmark"
      or FORMAT == "commonmark_x"
      or FORMAT:match("^markdown")
end


-- ─── filter state + filters ───────────────────────────────────────────────

-- src → description for images we annotated in this document. Used by the
-- Blocks pass to insert visible description paragraphs after the image when
-- writing markdown.
local desc_by_src = {}

function Image(el)
  local src = el.src
  if not src or src == "" then return el end

  local path = resolve_image_path(src)
  if not path then return el end

  local md5 = md5_of_file(path)
  if not md5 then
    io.stderr:write("[inject-image-descriptions] cannot compute md5: " .. path .. "\n")
    return el
  end

  local desc = load_description(md5)
  if not desc then
    io.stderr:write(
      "[inject-image-descriptions] no cached description for " .. src
      .. " (md5=" .. md5 .. ")\n"
    )
    return el
  end

  desc_by_src[src] = desc

  -- HTML/DOCX/PDF path: alt + title. Quarto maps fig-alt → <img alt>.
  -- Caption (el.caption) is left untouched so figcaption keeps working.
  el.attributes["fig-alt"] = desc
  el.title = desc

  return el
end


-- For markdown writers (the .llms.md sidecars), append a visible Para with
-- the description after each block that contains an annotated image. The
-- alt/title we set above tend to be dropped by gfm/commonmark writers, so
-- this is how the description reaches LLM consumers reading .llms.md.
local function image_in_inlines(inlines)
  for i = 1, #inlines do
    if inlines[i].t == "Image" then return inlines[i] end
  end
  return nil
end


function Blocks(blocks)
  if not is_markdown_writer() then return blocks end

  local out = {}
  local i = 1
  while i <= #blocks do
    local b = blocks[i]
    out[#out + 1] = b

    local img = nil
    if b.t == "Para" or b.t == "Plain" then
      img = image_in_inlines(b.content)
    elseif b.t == "Figure" then
      -- Pandoc 2.16+ Figure block: its content is a list of blocks; the
      -- image lives inside a Plain in there.
      for _, fblock in ipairs(b.content) do
        if (fblock.t == "Plain" or fblock.t == "Para") and not img then
          img = image_in_inlines(fblock.content)
        end
      end
    end

    if img and desc_by_src[img.src] then
      out[#out + 1] = pandoc.Para({ pandoc.Str(desc_by_src[img.src]) })
    end

    i = i + 1
  end
  return out
end
