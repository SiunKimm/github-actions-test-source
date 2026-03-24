#!/bin/bash
# Setup script for Test Migration Project

echo "Setting up Test Migration Project..."

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

echo "Setup complete!"
