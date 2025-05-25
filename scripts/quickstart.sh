#!/bin/bash
echo "Flask Python Template - Quick Start"
echo "=================================="
echo

# Check if venv exists
if [ -d "venv" ]; then
    echo "Virtual environment found."
    echo "Activating virtual environment..."
    source venv/bin/activate
    echo
    echo "Running Flask application..."
    python run.py
else
    echo "No virtual environment found."
    echo "Running setup script first..."
    echo
    python scripts/setup.py
    echo
    echo "Setup complete! Please run this script again or use:"
    echo "  source venv/bin/activate"
    echo "  python run.py"
fi
