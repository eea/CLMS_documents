local images = {}

-- Extract images from the document
function Image(el)
  local caption_text = ""

  -- Extract caption correctly (works with ![Caption](image.png) syntax)
  if el.caption and type(el.caption) == "table" then
    for _, inline in ipairs(el.caption) do
      if inline.t == "Str" then
        caption_text = caption_text .. inline.text .. " "
      elseif inline.t == "Space" then
        caption_text = caption_text .. " "
      end
    end
    caption_text = caption_text:gsub("%s+$", "")
  end

  table.insert(images, {
    url = el.src,
    caption = caption_text,
    width = el.attributes.width or nil,
    height = el.attributes.height or nil
  })

  return el
end

-- Function to inject JSON-LD before the first heading or at the end
function Pandoc(doc)
  if #images == 0 then
    return doc
  end

  -- Ensure `site_url` exists; otherwise, use empty string
  local site_url = doc.meta.site_url or ""
  if site_url ~= "" and not site_url:match("/$") then
    site_url = site_url .. "/"
  end

  local jsonld_images = {
    ["@context"] = "https://schema.org",
    ["@type"] = "ItemList",
    itemListElement = {}
  }

  for _, img in ipairs(images) do
    local absolute_url = img.url
    if not absolute_url:match("^https?://") then
      absolute_url = site_url .. img.url:gsub("^%./", "")
    end

    table.insert(jsonld_images.itemListElement, {
      ["@type"] = "ImageObject",
      url = absolute_url,
      caption = img.caption,
      width = img.width,
      height = img.height
    })
  end

  -- Convert JSON-LD to a script tag
  local jsonld_script = pandoc.RawBlock("html", "<script type=\"application/ld+json\">\n"
    .. quarto.json.encode(jsonld_images, { pretty = true }) .. "\n</script>")

  -- Inject JSON-LD **before the first <h1> or at the end**
  local inserted = false
  for i, block in ipairs(doc.blocks) do
    if block.t == "Header" and block.level == 1 then
      table.insert(doc.blocks, i, jsonld_script)
      inserted = true
      break
    end
  end

  -- If no <h1> was found, append JSON-LD at the end
  if not inserted then
    table.insert(doc.blocks, jsonld_script)
  end

  return doc
end
