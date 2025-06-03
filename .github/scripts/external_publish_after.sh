#!/bin/bash
set -euo pipefail

source "$(dirname "$0")/helpers/git-utils.sh"

echo "🧹 Cleaning up publish branch..."
run_git "deleting remote branch $PUBLISH_BRANCH" push origin --delete "$PUBLISH_BRANCH" || true
TAG_TO_DELETE="${PUBLISH_BRANCH#publish-}"
run_git "deleting remote tag $TAG_TO_DELETE" push origin --delete "v-$TAG_TO_DELETE" || true
