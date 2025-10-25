#!/bin/bash
set -e

echo "Installing uv..."
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

# Set link mode to avoid hardlink issues
export UV_LINK_MODE=copy

# Simplify the project for codespaces
echo "Building uv environment..."

uv remove sentence-transformers
rm -f uv.lock

# Now sync

uv sync

echo "Cleaning cache..."
uv cache clean

echo "Setup complete!"