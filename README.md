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
├── .env.example          # Environment variables example
├── .gitignore           # Git ignore file
├── config.py            # Configuration module
├── requirements.txt     # Python dependencies
├── run.py              # Application entry point
└── README.md           # This file
```

## Quick Start

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd Flask-Python-Template
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # macOS/Linux
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

5. Run the application:
   ```bash
   flask run
   # or
   python run.py
   ```

6. Open your browser and navigate to `http://localhost:5000`

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
