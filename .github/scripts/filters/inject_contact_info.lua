-- inject_contact_info.lua
-- Quarto filter to automatically inject standard contact information
-- after the YAML header in documents

local filter_dir = debug.getinfo(1, "S").source:match("@?(.*/)") or ""
local template_path = filter_dir .. "../../templates/contact_template.md"

-- Function to read the contact template
function read_contact_template()
  local file = io.open(template_path, "r")
  if not file then
    return nil
  end
  local content = file:read("*all")
  file:close()
  return content
end

-- Function to check if contact should be injected
function should_inject_contact(meta)
  -- Check if contact injection is explicitly disabled
  if meta.contact and pandoc.utils.stringify(meta.contact) == "false" then
    return false
  end
  
  -- Default: inject contact unless explicitly disabled
  return true
end

-- Main filter function
function Pandoc(doc)
  -- Check if we should inject contact info
  if not should_inject_contact(doc.meta) then
    return doc
  end
  
  -- Read the contact template
  local contact_content = read_contact_template()
  if not contact_content then
    -- If template doesn't exist, skip injection
    return doc
  end
  
  -- Parse the contact template as markdown
  local contact_doc = pandoc.read(contact_content, "markdown")
  
  -- Insert contact blocks at the beginning of the document
  local new_blocks = {}
  
  -- Add contact blocks first
  for i, block in pairs(contact_doc.blocks) do
    table.insert(new_blocks, block)
  end
  
  -- Add original document blocks
  for i, block in pairs(doc.blocks) do
    table.insert(new_blocks, block)
  end
  
  -- Return document with injected contact info
  return pandoc.Pandoc(new_blocks, doc.meta)
end