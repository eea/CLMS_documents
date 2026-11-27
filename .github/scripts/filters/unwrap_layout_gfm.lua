-- Drop layout attributes (layout-ncol, layout-nrow, layout, ...) in the gfm
-- (.llms.md) output ONLY.
--
-- Quarto has no gfm renderer for an id-less panel layout: it warns
-- "Don't know how to render PanelLayout without a float" and emits an EMPTY
-- <div>, losing every image, caption and baked-in description inside. With the
-- attributes gone the div is a plain container and its images render in sequence.
--
-- Wired under `gfm.filters` only, so HTML and Typst/PDF keep their grid layouts.

-- Quarto reports the gfm target as FORMAT=commonmark, so match all markdown.
if not (FORMAT:match("gfm") or FORMAT:match("commonmark") or FORMAT:match("markdown")) then
  return {}
end

function Div(el)
  local changed = false
  for k, _ in pairs(el.attributes) do
    if k == "layout" or k:match("^layout%-") then
      el.attributes[k] = nil
      changed = true
    end
  end
  if changed then
    return el
  end
end
