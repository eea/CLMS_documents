#!/bin/bash
set -euo pipefail

source "$(dirname "$0")/helpers/git-utils.sh"

# Only run if this was a merge from a publish-* branch
MERGE_COMMIT_MSG=$(git log -1 --pretty=%B)

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
if [[ "$CURRENT_BRANCH" != "develop" ]] || ! echo "$MERGE_COMMIT_MSG" | grep -qE "from publish-"; then
  echo "❎ Not a publish-* → develop merge. Skipping issue creation."
  exit 0
fi

echo "🔍 Detected publish-* → develop failed merge."

# Get log tail if available
LOG_SNIPPET=""
if [[ -f job.log ]]; then
  LOG_SNIPPET=$(tail -n 40 job.log | sed 's/"/\\"/g')
fi

# Prepare notification content
USER_MENTION="@${GITHUB_ACTOR}"
REPO_URL="https://github.com/${GITHUB_REPOSITORY}"
ISSUE_BODY="$(cat <<EOF
The publish pipeline failed.

**Triggered by**: ${USER_MENTION}  
**Branch**: \`${GITHUB_REF_NAME}\`  
**Commit**: [${GITHUB_SHA}](${REPO_URL}/commit/${GITHUB_SHA})

---

### 🔍 Error log excerpt:
\`\`\`log
${LOG_SNIPPET}
\`\`\`

Please check and re-submit after addressing the problem.
EOF
)"



# Create JSON payload using jq to escape properly
JSON_PAYLOAD=$(jq -n \
  --arg title "🚨 Publish Failed [${GITHUB_REF_NAME}]" \
  --arg body "$ISSUE_BODY" \
  '{title: $title, body: $body}')

# Create GitHub issue
CREATE_RESPONSE=$(curl -s -X POST \
  -H "Authorization: token ${GITHUB_TOKEN}" \
  -H "Accept: application/vnd.github+json" \
  -d "$JSON_PAYLOAD" \
  https://api.github.com/repos/${GITHUB_REPOSITORY}/issues)

# Extract issue number
ISSUE_NUMBER=$(echo "$CREATE_RESPONSE" | jq -r '.number')

if [ "$ISSUE_NUMBER" = "null" ]; then
  echo "❌ Failed to create issue"
  echo "$CREATE_RESPONSE"
  exit 1
fi

echo "issue_number: ${ISSUE_NUMBER}"

# Wait briefly to ensure GitHub sends the notification
sleep 10

# Close the issue (auto-dismiss)
curl -s -X PATCH \
 -H "Authorization: token ${GITHUB_TOKEN}" \
 -H "Accept: application/vnd.github+json" \
 https://api.github.com/repos/${GITHUB_REPOSITORY}/issues/${ISSUE_NUMBER} \
 -d '{"state":"closed"}'

echo "✅ Issue #${ISSUE_NUMBER} created and closed to notify ${USER_MENTION}."
