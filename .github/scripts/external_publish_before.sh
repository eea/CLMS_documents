#!/bin/bash
set -euo pipefail

source "$(dirname "$0")/helpers/git-utils.sh"

echo "🛠️ Setting up SSH for deploy key..."
if [ ! -f ~/.ssh/id_ed25519 ]; then
    mkdir -p ~/.ssh
    echo "$CI_DEPLOY_KEY" > ~/.ssh/id_ed25519
    chmod 600 ~/.ssh/id_ed25519
    ssh-keyscan github.com >> ~/.ssh/known_hosts 2> /dev/null
fi

echo "🔧 Setting up Git environment..."
apt-get update -qq > /dev/null 2>&1 && apt-get install -y -qq yq > /dev/null 2>&1 || true

run_git "Configuring Git user name" config --global user.name "ci_docker_builder"
run_git "Configuring Git user email" config --global user.email "ci_docker_builder@users.noreply.github.com"

run_git "Setting remote URL" remote set-url origin git@github.com:${GITHUB_REPOSITORY}.git
#run_git "Fetching origin develop branch" fetch origin develop

echo "✅ Environment ready."
