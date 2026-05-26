-- Injects the standard EEA contact block (templates/contact_template.md) at the
-- top of each document. Wired up for HTML only — the Typst template renders the
-- contact itself (see _meta/theme/typst/typst-template.typ).

local filter_dir = debug.getinfo(1, "S").source:match("@?(.*/)") or ""
local template_path = filter_dir .. "../../templates/contact_template.md"

function read_contact_template()
  local file = io.open(template_path, "r")
  if not file then
    return nil
  end
  local content = file:read("*all")
  file:close()
  return content
end

function should_inject_contact(meta)
  -- Opt out with `contact: false` in the frontmatter; otherwise inject.
  if meta.contact and pandoc.utils.stringify(meta.contact) == "false" then
    return false
  end
  return true
end

function Pandoc(doc)
  if not should_inject_contact(doc.meta) then
    return doc
  end

  local contact_content = read_contact_template()
  if not contact_content then
    return doc  -- no template on disk → leave the document untouched
  end

  local contact_doc = pandoc.read(contact_content, "markdown")

  -- Prepend the contact blocks, then the document's own blocks.
  local new_blocks = {}
  for i, block in pairs(contact_doc.blocks) do
    table.insert(new_blocks, block)
  end
  for i, block in pairs(doc.blocks) do
    table.insert(new_blocks, block)
  end

  return pandoc.Pandoc(new_blocks, doc.meta)
end
