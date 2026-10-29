-- Typst fails the whole PDF on a link to a label that isn't in the document
-- ("label `<x>` does not exist in the document"). Word-converted docs are full
-- of those: `_Ref…` bookmarks the converter never exported, or anchors sitting
-- in table captions that don't survive into the Typst output. So each internal
-- link becomes "link if the label exists, else plain text" - working links look
-- the same, dangling ones degrade instead of breaking the build.
-- Typst only; HTML shrugs off a dangling #anchor.

local function lbl(id)
  return 'label("' .. id:gsub('[\\"]', '\\%0') .. '")'
end

function Link(el)
  local id = el.target:match("^#(.+)$")
  if not id then
    return nil
  end
  local out = pandoc.List({
    pandoc.RawInline("typst",
      "#context if query(" .. lbl(id) .. ").len() > 0 { link(" .. lbl(id) .. ")["),
  })
  out:extend(el.content)
  out:insert(pandoc.RawInline("typst", "] } else ["))
  out:extend(el.content)
  -- The ';' ends the embedded expression, so a following ".word" isn't read
  -- as field access on the result.
  out:insert(pandoc.RawInline("typst", "];"))
  return out
end
