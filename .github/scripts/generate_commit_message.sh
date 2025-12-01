#!/bin/bash
# Generate detailed commit message body from PR changed files
# Usage: generate_commit_message.sh <pr_number>

set -e

PR_NUMBER=$1

if [ -z "$PR_NUMBER" ]; then
  echo "Usage: $0 <pr_number>"
  exit 1
fi

# Get changed .qmd files only
changed_files=$(gh pr view "$PR_NUMBER" --json files -q '.files[].path' | grep '^DOCS/.*\.qmd$' || echo "")

if [ -z "$changed_files" ]; then
  echo "No documentation files (.qmd) changed"
  exit 0
fi

# Group files by category subdirectory
declare -A categories
while IFS= read -r file; do
  [ -z "$file" ] && continue
  # Extract category (first directory after DOCS/)
  category=$(echo "$file" | sed 's|^DOCS/\([^/]*\)/.*|\1|')
  # Extract filename without path and .qmd extension
  filename=$(basename "$file" .qmd)
  
  # Add to category array
  if [ -n "${categories[$category]}" ]; then
    categories[$category]="${categories[$category]}\n- ${filename}"
  else
    categories[$category]="- ${filename}"
  fi
done <<< "$changed_files"

# Build message body, sorted by category name
body=""
for category in $(echo "${!categories[@]}" | tr ' ' '\n' | sort); do
  # Format category name (replace underscores with spaces, title case)
  formatted_category=$(echo "$category" | sed 's/_/ /g')
  body="${body}\n\n${formatted_category}:"
  body="${body}\n${categories[$category]}"
done

# Output the body
echo -e "$body"
