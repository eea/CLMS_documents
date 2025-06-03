#!/bin/bash
set -euo pipefail

source "$(dirname "$0")/helpers/git-utils.sh"


echo "🚀 Starting validation..."
PROJECT_NAME=$(echo "$PUBLISH_BRANCH" | sed -E 's/^publish-(.+)-[0-9]{8}-[0-9]{6}$/\1/')
echo "Project: $PROJECT_NAME"

echo "🔎 Checking files inside publish branch (fast tree scan)..."
run_git "fetching develop branch" fetch origin develop
PUBLISH_COMMIT=$(git rev-parse origin/${PUBLISH_BRANCH})
echo "PUBLISH_COMMIT: $PUBLISH_COMMIT"

git ls-tree -r --name-only "$PUBLISH_COMMIT" > changed-files.txt
sed -i '/^\.gitignore$/d; /^\.github\/workflows\/trigger\.yml$/d' changed-files.txt
cat changed-files.txt

INVALID_FILES=$(grep -v "^DOCS/${PROJECT_NAME}/" changed-files.txt || true)
if [ -n "$INVALID_FILES" ]; then
  echo "❌ Changes outside DOCS/${PROJECT_NAME} detected:"
  echo "$INVALID_FILES"
  exit 1
fi

echo "✅ Folder validation passed."

echo "🔀 Preparing secure diff-aware merge into develop..."
git checkout develop
git pull origin develop
mkdir -p tmp_publish
git archive "$PUBLISH_COMMIT" DOCS/"$PROJECT_NAME" | tar -x -C tmp_publish

# ✅ Remove any GitHub workflows injected into the subtree
rm -rf tmp_publish/DOCS/"${PROJECT_NAME}"/.github
rm -rf tmp_publish/DOCS/"${PROJECT_NAME}"/.gitignore

echo "🔍 Finding modified and deleted files only..."
MODIFIED_FILES=()
while IFS= read -r file; do
  if [ ! -f "$file" ] || ! cmp -s "$file" "tmp_publish/$file"; then
    MODIFIED_FILES+=("$file")
  fi
done < <(find tmp_publish/DOCS/"$PROJECT_NAME" -type f | sed 's|tmp_publish/||')

DELETED_FILES=()
while IFS= read -r file; do
  if [ ! -f "tmp_publish/$file" ]; then
    DELETED_FILES+=("$file")
  fi
done < <(find DOCS/"$PROJECT_NAME" -type f)

if [ "${#MODIFIED_FILES[@]}" -eq 0 ] && [ "${#DELETED_FILES[@]}" -eq 0 ]; then
  echo "🟡 No real changes to DOCS/$PROJECT_NAME — skipping commit."
  exit 0
fi

echo "✅ Modified files:"
printf '%s\n' "${MODIFIED_FILES[@]}"
echo "🗑️ Deleted files:"
printf '%s\n' "${DELETED_FILES[@]}"

for file in "${MODIFIED_FILES[@]}"; do
  mkdir -p "$(dirname "$file")"
  cp "tmp_publish/$file" "$file"; 
done

if [ "${#DELETED_FILES[@]}" -gt 0 ]; then
    run_git "removing deleted files" rm "${DELETED_FILES[@]}"
fi
for file in "${MODIFIED_FILES[@]}"; do
   run_git "adding $file to staging" add "$file"
done

COMMIT_MSG=$(cat <<EOF
chore(ci): merge DOCS/$PROJECT_NAME from $PUBLISH_BRANCH

Triggered by: CI Workflow
Branch: $PUBLISH_BRANCH
Commit: $PUBLISH_COMMIT
Repo: https://github.com/$GITHUB_REPOSITORY/commit/$PUBLISH_COMMIT
EOF
)

run_git "committing changes to develop branch" commit -m "$COMMIT_MSG"
run_git "pushing changes to develop branch" push origin develop
