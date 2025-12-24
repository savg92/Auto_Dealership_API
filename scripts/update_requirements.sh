#!/usr/bin/env bash
set -euo pipefail

# Script to update and re-pin Python dependencies using `uv`.
# Usage: run from repo root: ./scripts/update_requirements.sh

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "Updating and compiling requirements with uv in: $ROOT_DIR"

# If your uv workflow supports an "upgrade" or similar command, enable it.
# Uncomment the next line if you want to attempt upgrading packages before compile.
# uv pip upgrade --all

# Compile the pinned requirements (this is the canonical file used by the project)
# If requirements.in exists, use it for upgrades; otherwise use requirements.txt
if [ -f requirements.in ]; then
    uv pip compile requirements.in --output-file requirements.txt
else
    uv pip compile requirements.txt --output-file requirements.txt
fi

echo "requirements.txt regenerated. Review and commit the changes."
