"""App Module."""
from flask import Flask
from flask_cors import CORS
from app.routes import setup_routes


def create_app():
    """Crea y configura la app."""
    app = Flask(__name__)
    CORS(app)
    setup_routes(app)
    return app
