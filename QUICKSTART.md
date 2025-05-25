# Flask Python Template - Quick Start Guide

## 🚀 First Time Setup (Choose One)

### Option 1: Automatic Setup (Recommended)
```bash
# Windows
scripts\quickstart.bat

# Mac/Linux
chmod +x scripts/quickstart.sh
./scripts/quickstart.sh
```

### Option 2: Using Setup Script
```bash
python scripts/setup.py
```

### Option 3: Manual Setup
```bash
# Create virtual environment
python -m venv venv

# Activate it
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
python run.py
```

## 🔧 VS Code Setup

1. Open the project in VS Code
2. When prompted to select a Python interpreter, choose `./venv/Scripts/python.exe`
3. Press F5 to debug or Ctrl+Shift+B to run

## 📝 Common Commands

```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Run the application
python run.py

# Run tests
pytest

# Install new packages
pip install package-name
pip freeze > requirements.txt
```

## ❓ Troubleshooting

**"No module named flask"**
- You need to activate the virtual environment first
- Run: `venv\Scripts\activate` then `python run.py`

**VS Code can't find Flask**
- Ctrl+Shift+P → "Python: Select Interpreter"
- Choose `./venv/Scripts/python.exe`

**Port 5000 already in use**
- Set a different port: `set FLASK_PORT=8000` (Windows)
- Or: `export FLASK_PORT=8000` (Mac/Linux)
