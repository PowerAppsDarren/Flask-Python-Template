# Flask Python Template

A well-structured, minimalistic template for creating web applications with Python and Flask following best practices.

## Features

- ✨ Application factory pattern
- 📁 Modular structure with blueprints
- 🔧 Environment-based configuration
- 🧪 Testing setup included
- 🎨 Organized static files and templates
- 📦 Minimal dependencies
- 🚀 Production-ready structure

## Project Structure

```
Flask-Python-Template/
├── app/
│   ├── __init__.py         # Application factory
│   ├── main/              # Main blueprint
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── errors/            # Error handlers blueprint
│   │   ├── __init__.py
│   │   └── handlers.py
│   ├── static/            # Static files
│   │   ├── css/
│   │   │   └── main.css
│   │   └── js/
│   └── templates/         # Jinja2 templates
│       ├── base.html
│       ├── index.html
│       ├── about.html
│       └── errors/
│           ├── 404.html
│           └── 500.html
├── tests/                 # Test modules
│   ├── __init__.py
│   └── test_basic.py
├── scripts/              # Helper scripts
│   ├── dev.py           # Development helper
│   └── setup.py         # Setup script
├── .env.example          # Environment variables example
├── .gitignore           # Git ignore file
├── config.py            # Configuration module
├── requirements.txt     # Python dependencies
├── run.py              # Application entry point
└── README.md           # This file
```

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

## 🚀 First Time Setup

### Windows Users
```bash
# Clone and enter the repository
git clone https://github.com/PowerAppsDarren/Flask-Python-Template
cd Flask-Python-Template

# Run the quick start script
scripts\quickstart.bat
```

### Mac/Linux Users
```bash
# Clone and enter the repository
git clone https://github.com/PowerAppsDarren/Flask-Python-Template
cd Flask-Python-Template

# Make the script executable and run it
chmod +x scripts/quickstart.sh
./scripts/quickstart.sh
```

### Alternative: Manual Setup
```bash
# 1. Run the setup script
python scripts/setup.py

# 2. Activate the virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# 3. Run the application
python run.py
```

## Quick Start

### Option 1: Using the setup script (Recommended)

```bash
# Clone the repository
git clone https://github.com/PowerAppsDarren/Flask-Python-Template
cd Flask-Python-Template

# Run the setup script
python scripts/setup.py
```

### Option 2: Manual setup

1. Clone this repository:
   ```bash
   git clone https://github.com/PowerAppsDarren/Flask-Python-Template
   cd Flask-Python-Template
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Set up environment variables:
   ```bash
   # Windows
   copy .env.example .env
   
   # macOS/Linux
   cp .env.example .env
   ```

6. Run the application:
   ```bash
   python run.py
   ```

7. Open your browser and navigate to `http://localhost:5000`

## VS Code Setup

### 🚨 Important: First Time VS Code Setup

If you're having issues with VS Code not finding Flask or the Python interpreter:

```bash
# Run this special VS Code setup script
python setup-vscode.py
```

Then follow the on-screen instructions carefully.

### Manual VS Code Setup

1. **Create virtual environment first**:
   ```bash
   python -m venv venv
   ```

2. **Open VS Code**:
   ```bash
   code .
   ```

3. **Select Python Interpreter** (This is the crucial step!):
   - Look at the bottom-left corner of VS Code
   - Click on the Python version shown (or "Select Python Interpreter" if shown)
   - Choose: `.\venv\Scripts\python.exe` (Windows) or `./venv/bin/python` (Linux/Mac)
   - If you don't see this option:
     - Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
     - Type: "Python: Select Interpreter"
     - Click "Enter interpreter path..."
     - Browse to and select: `venv\Scripts\python.exe`

4. **Reload VS Code** (Important!):
   - Press `Ctrl+R` (or `Cmd+R` on Mac)
   - Or close and reopen VS Code

5. **Now F5 will work!**

### Keyboard Shortcuts

- **F5**: Start debugging Flask application
- **Ctrl+Shift+B**: Show build tasks menu
  - Default: Run Flask app locally
  - Docker: Build and Run
  - Run Tests
  - Install Dependencies

### Available Commands

#### Local Development
```bash
# Run Flask directly
python run.py

# Using the helper script
python scripts/dev.py flask
```

#### Docker Development
```bash
# Build and run with Docker Compose
docker compose up --build

# Run without rebuilding
docker compose up

# Stop containers
docker compose down

# Using the helper script
python scripts/dev.py docker
```

#### Testing
```bash
# Run tests
pytest

# Run with coverage
pytest --cov=app tests/

# Using the helper script
python scripts/dev.py test
```

## Troubleshooting

### "Failed to resolve env" error in VS Code

This is the most common issue. To fix:

1. **Run the VS Code setup script**:
   ```bash
   python setup-vscode.py
   ```

2. **Manually select the interpreter**:
   - Delete the `.vscode/settings.json` file
   - Restart VS Code
   - Press `Ctrl+Shift+P` → "Python: Select Interpreter"
   - Choose "Enter interpreter path..."
   - Navigate to `venv\Scripts\python.exe` and select it

3. **Alternative fix**:
   - Close VS Code completely
   - Delete the `.vscode` folder
   - Run: `python setup-vscode.py`
   - Open VS Code and select the interpreter when prompted

### "No module named flask" error

This means Flask is not installed. Make sure you:
1. Run the setup script first: `python scripts/setup.py`
2. Activate the virtual environment: `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Mac/Linux)
3. Then run the application: `python run.py`

### VS Code Issues

If VS Code is not using the virtual environment:
1. Open Command Palette (Ctrl+Shift+P)
2. Type "Python: Select Interpreter"
3. Choose the interpreter in `./venv/Scripts/python.exe` (Windows) or `./venv/bin/python` (Mac/Linux)
4. Restart VS Code

### Port already in use

If port 5000 is already in use, you can specify a different port:
```bash
python run.py
# or set environment variable
set FLASK_PORT=8000  # Windows
export FLASK_PORT=8000  # macOS/Linux
```

## Development

### Running Tests

```bash
pytest
# With coverage
pytest --cov=app tests/
```

### Adding New Features

1. Create a new blueprint in `app/` directory
2. Register the blueprint in `app/__init__.py`
3. Add templates in `app/templates/`
4. Add static files in `app/static/`

## Configuration

The application supports multiple configurations:

- `development` - Debug mode enabled
- `production` - Debug mode disabled, optimized for deployment
- `testing` - Special configuration for running tests

Set the configuration using the `FLASK_CONFIG` environment variable.

## Deployment

For production deployment:

1. Set environment variables:
   ```bash
   export FLASK_CONFIG=production
   export SECRET_KEY=your-secure-secret-key
   ```

2. Use a production WSGI server:
   ```bash
   gunicorn -w 4 -b 0.0.0.0:8000 run:app
   ```

3. Set up a reverse proxy (nginx/Apache)
4. Enable HTTPS
5. Set up logging and monitoring

## License

This template is open source and available under the MIT License.
