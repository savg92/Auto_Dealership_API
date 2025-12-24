# Script to update and sync Python dependencies using `uv`.
# Usage: run from repo root: ./scripts/update_requirements.sh

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

echo "Updating and syncing dependencies with uv in: $ROOT_DIR"

# Upgrade dependencies to latest versions and update uv.lock
uv lock --upgrade

echo "uv.lock updated. Review and commit the changes."
