local pipe     = pandoc.pipe
local sha1     = pandoc.utils.sha1
local mediabag = pandoc.mediabag

local NODE = "node"
local filter_dir = debug.getinfo(1, "S").source:match("@?(.*/)") or ""
local TEX2PNG = filter_dir .. "tex2png.js"

-- Config ----
local ONELINE_HEIGHT_CM = 0.60
local INLINE_LINE_HEIGHT_CM = 0.25

local function has(s, needle) return s:find(needle, 1, true) ~= nil end

local function count_lines(tex)
  -- Count explicit "\\" breaks
  local lines, i = 1, 1
  while true do
    local s, e = tex:find("\\\\", i, true)
    if not s then break end
    lines = lines + 1
    i = e + 1
  end
  -- If known multiline env present, ensure at least 2 lines
  if has(tex, "\\begin{cases}") or has(tex, "\\begin{aligned}") or
     has(tex, "\\begin{align}") or has(tex, "\\begin{split}") or
     has(tex, "\\begin{gathered}") or has(tex, "\\begin{gather}") then
    if lines < 2 then lines = 2 end
  end
  return lines
end

local function tex_to_png(tex, display)
  local args = { TEX2PNG }
  if display then table.insert(args, "--display") end
  return pipe(NODE, args, tex)
end

local function build_image(name, bytes,  height_cm)
  pcall(function() mediabag.insert(name, "image/png", bytes) end)
  local img = pandoc.Image({}, name)
  img.attributes = img.attributes or {}
  -- set only height; Word keeps aspect ratio
  img.attributes.height = string.format("%.2fcm", height_cm)
  return img
end

local function has(s, needle) return s:find(needle, 1, true) ~= nil end

local function count_lines(tex)
  local lines, i = 1, 1
  while true do
    local s, e = tex:find("\\\\", i, true)  -- literal '\\'
    if not s then break end
    lines = lines + 1
    i = e + 1
  end
  -- Treat common multiline environments as at least 2 lines
  if has(tex, "\\begin{cases}") or has(tex, "\\begin{aligned}") or
     has(tex, "\\begin{align}") or has(tex, "\\begin{split}") or
     has(tex, "\\begin{gathered}") or has(tex, "\\begin{gather}") then
    if lines < 2 then lines = 2 end
  end
  return lines
end

function Math(m)
  
  local is_inline = (m.mathtype == pandoc.MathInline) or (tostring(m.mathtype) == "InlineMath")

  -- Set size from line count
  if is_inline then
    height_cm = INLINE_LINE_HEIGHT_CM
  else 
    local lines = count_lines(m.text)
    if lines == 1 then
      height_cm = ONELINE_HEIGHT_CM
    else
      height_cm = lines * ONELINE_HEIGHT_CM * 1.2
    end
  end

  -- Render PNG and embed with explicit size
  local png  = tex_to_png(m.text, m.mathtype == pandoc.MathDisplay)
  local name = "eq-" .. sha1(png) .. ".png"
  local img  = build_image(name, png, height_cm)

  -- Block vs inline placement
  if m.mathtype == pandoc.MathDisplay then
    return pandoc.Para{ img }
  end
  return img
  
end
