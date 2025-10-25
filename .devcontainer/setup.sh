#!/bin/bash
set -e

echo "Installing uv..."
curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH"

echo "Installing dependencies with CPU-only PyTorch..."
# Set link mode to avoid hardlink issues
export UV_LINK_MODE=copy

# Install with CPU-only PyTorch by using the CPU index
# This only affects this installation, not the project config
uv sync --extra-index-url https://download.pytorch.org/whl/cpu

echo "Cleaning cache..."
uv cache clean

echo "Setup complete!"