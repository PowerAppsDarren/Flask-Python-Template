import os
from app import create_app
from config import config

config_name = os.environ.get('FLASK_CONFIG') or 'default'
app = create_app(config[config_name])

if __name__ == '__main__':
    # Allow setting host and port via environment variables
    host = os.environ.get('FLASK_HOST', '0.0.0.0')
    port = int(os.environ.get('FLASK_PORT', 5000))
    app.run(host=host, port=port)
