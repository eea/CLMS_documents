#!/bin/bash
set -euo pipefail

source "$(dirname "$0")/helpers/git-utils.sh"

PROJECT_NAME=$(echo "$PUBLISH_BRANCH" | sed -E 's/^publish-(.+)-[0-9]{8}-[0-9]{6}$/\1/')
PUBLISH_COMMIT=$(git rev-parse origin/${PUBLISH_BRANCH})
TEMP_WORKSPACE="tmp_publish"

echo "Project: $PROJECT_NAME"
echo "PUBLISH_COMMIT: $PUBLISH_COMMIT"

get_changed_files() {
    git ls-tree -r --name-only "$PUBLISH_COMMIT" > changed-files.txt
    # Remove specific files we want to ignore
    sed -i '/^\.gitignore$/d; /^\.github\/workflows\/trigger\.yml$/d' changed-files.txt
    cat changed-files.txt
}

check_files_within_project() {
    local invalid_files
    
    invalid_files=$(grep -v "^DOCS/${PROJECT_NAME}/" changed-files.txt || true)
    
    if [ -n "$invalid_files" ]; then
        echo "❌ Changes outside DOCS/${PROJECT_NAME} detected:"
        echo "$invalid_files"
        return 1
    fi
    
    echo "✅ All changes within project boundaries"
    return 0
}

prepare_merge_environment() {
    echo "🔀 Preparing secure diff-aware merge into develop..."
    git checkout develop
    git pull origin develop
    mkdir -p "$TEMP_WORKSPACE"
    git archive "$PUBLISH_COMMIT" DOCS/"$PROJECT_NAME" | tar -x -C $TEMP_WORKSPACE
}

# Remove any GitHub workflows injected into the subtree
cleanup_extracted_files() {
    echo "🧹 Cleaning up extracted files..."
    rm -rf "$TEMP_WORKSPACE"/DOCS/"${PROJECT_NAME}"/.github
    rm -rf "$TEMP_WORKSPACE"/DOCS/"${PROJECT_NAME}"/.gitignore
}

find_file_changes() {    
    echo "🔍 Finding modified and deleted files..."
    
    # Find modified files
    MODIFIED_FILES=()
    while IFS= read -r file; do
        if [ ! -f "$file" ] || ! cmp -s "$file" "$TEMP_WORKSPACE/$file"; then
            MODIFIED_FILES+=("$file")
        fi
    done < <(find "$TEMP_WORKSPACE"/DOCS/"$PROJECT_NAME" -type f | sed "s|$TEMP_WORKSPACE/||")

    # Find deleted files
    DELETED_FILES=()
    while IFS= read -r file; do
        if [ ! -f "$TEMP_WORKSPACE/$file" ]; then
            DELETED_FILES+=("$file")
        fi
    done < <(find DOCS/"$PROJECT_NAME" -type f)
}

check_for_changes() {
    if [ "${#MODIFIED_FILES[@]}" -eq 0 ] && [ "${#DELETED_FILES[@]}" -eq 0 ]; then
        echo "🟡 No real changes to DOCS/$PROJECT_NAME — skipping commit."
        return 1 
    fi
    
    echo "✅ Modified files:"
    printf '%s\n' "${MODIFIED_FILES[@]}"
    echo "🗑️ Deleted files:" 
    printf '%s\n' "${DELETED_FILES[@]}"
    
    return 0
}

apply_file_changes() {
    echo "📝 Applying file changes..."
    
    # Copy modified files
    for file in "${MODIFIED_FILES[@]}"; do
        mkdir -p "$(dirname "$file")"
        cp "$TEMP_WORKSPACE/$file" "$file"
    done
    
    # Remove deleted files
    if [ "${#DELETED_FILES[@]}" -gt 0 ]; then
        run_git "removing deleted files" rm "${DELETED_FILES[@]}"
    fi
    
    # Stage modified files
    for file in "${MODIFIED_FILES[@]}"; do
        run_git "adding $file to staging" add "$file"
    done
}

generate_commit_message() {    
    cat <<EOF
chore(ci): merge DOCS/$PROJECT_NAME from $PUBLISH_BRANCH

Triggered by: CI Workflow
Branch: $PUBLISH_BRANCH
Commit: $PUBLISH_COMMIT
Repo: https://github.com/$GITHUB_REPOSITORY/commit/$PUBLISH_COMMIT
EOF
}

commit_and_push_changes() {
    local commit_msg
    commit_msg=$(generate_commit_message)
    
    echo "💾 Committing and pushing changes..."
    run_git "committing changes to develop branch" commit -m "$commit_msg"
    run_git "pushing changes to develop branch" push origin develop
}

########## Main logic ##########

# 1. Get changed files in the publish branch
echo "🔎 Checking files inside publish branch (fast tree scan)..."
run_git "fetching develop branch" fetch origin develop

get_changed_files

# 2. Validate that the changes are correctly scoped to the project and are correct
check_files_within_project || exit 1
python .github/scripts/validate_qmd_files.py || exit 1

# 3. Merge the changes into develop
prepare_merge_environment
cleanup_extracted_files
find_file_changes

if ! check_for_changes; then
    exit 0
fi

apply_file_changes
commit_and_push_changes