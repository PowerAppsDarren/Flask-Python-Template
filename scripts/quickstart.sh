#!/bin/bash

echo "Flask Python Template - Quick Start"
echo "=================================="
echo

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
    echo "Virtual environment created."
    echo
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo

# Copy .env if it doesn't exist
if [ ! -f ".env" ]; then
    if [ -f ".env.example" ]; then
        cp .env.example .env
        echo "Environment file created from .env.example"
    fi
fi

# Launch VS Code if available
if command -v code &> /dev/null; then
    echo "Launching VS Code..."
    code .
    echo
    echo "VS Code launched. Press Cmd+Shift+P and select 'Python: Select Interpreter'"
    echo "Then choose the interpreter from venv/bin/python"
else
    echo "VS Code not found in PATH"
fi

echo
echo "Setup complete! To run the app:"
echo "  1. Run: source venv/bin/activate"
echo "  2. Run: python run.py"
echo
