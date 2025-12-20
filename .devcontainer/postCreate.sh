#!/usr/bin/env bash
set -e

echo "==> Setting up Python virtual env..."
if [ ! -d ".venv" ]; then
  python3 -m venv .venv
fi

# Activar venv
source .venv/bin/activate

echo "==> Upgrading pip..."
python -m pip install --upgrade pip

if [ -f "requirements.txt" ]; then
  echo "==> Installing Python requirements..."
  pip install -r requirements.txt
fi

echo "==> Installing Node dependencies (if package.json exists)..."
if [ -f "package.json" ]; then
  npm install
fi

echo "==> Done."