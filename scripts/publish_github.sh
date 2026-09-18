#!/usr/bin/env bash
set -euo pipefail

REPO_NAME="${1:-agentic-analytics-engineering}"
VISIBILITY="${2:-private}"

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is required. Install it first, then rerun this script."
  exit 1
fi

if ! gh auth status >/dev/null 2>&1; then
  echo "GitHub CLI is not authenticated. Run: gh auth login"
  exit 1
fi

case "$VISIBILITY" in
  private|public|internal) ;;
  *) echo "Visibility must be private, public, or internal"; exit 2 ;;
esac

cd "$(dirname "$0")/.."

if git remote get-url origin >/dev/null 2>&1; then
  echo "origin already exists: $(git remote get-url origin)"
  echo "Nothing to create."
  exit 0
fi

gh repo create "$REPO_NAME" "--$VISIBILITY" --source=. --remote=origin --push 
echo "Created and pushed: $(git remote get-url origin)"
