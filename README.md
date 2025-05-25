# Flask Python Template

A minimalistic template for creating web applications with Python and Flask.

## Features

- ✨ Clean and simple Flask application structure
- 📄 Template inheritance with Jinja2
- 🎨 Minimal CSS styling
- 🔧 Configuration management
- 📦 Minimal dependencies

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

4. Run the application:
   ```bash
   python app.py
   ```

5. Open your browser and navigate to `http://localhost:5000`

## Project Structure

```
Flask-Python-Template/
├── app.py              # Main Flask application
├── config.py           # Configuration settings
├── requirements.txt    # Python dependencies
├── static/
│   └── css/
│       └── style.css   # Minimal styling
├── templates/
│   ├── base.html       # Base template
│   ├── index.html      # Home page
│   ├── about.html      # About page
│   └── 404.html        # Error page
└── README.md           # This file
```

## Customization

- Modify `app.py` to add new routes
- Update templates in the `templates/` directory
- Add custom styles to `static/css/style.css`
- Configure settings in `config.py`

## Deployment

For production deployment:
1. Set a secure `SECRET_KEY` environment variable
2. Set `FLASK_DEBUG=False`
3. Use a production WSGI server like Gunicorn

## License

This template is open source and available under the MIT License.
