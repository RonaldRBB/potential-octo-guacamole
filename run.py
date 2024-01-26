"""Main."""
from app import create_app
from config import APP_HOST, APP_PORT, APP_DEBUG

if __name__ == "__main__":
    app = create_app()
    app.run(host=APP_HOST, port=APP_PORT, debug=APP_DEBUG)
