"""Application main file"""
import secrets

from flask import Flask


def create_app():
    """Factory function to create and configure the Flask app."""
    app = Flask(__name__)
    app.config['ENV'] = 'development'
    app.config['SECRET_KEY'] = secrets.token_hex(64)

    @app.route("/")
    def hello_world():
        """Hello World endpoint"""
        return "<p>Hello, World!!</p>"

    return app


if __name__ == "__main__":  # pragma: no cover
    # Sólo ejecuta la aplicación si este archivo se ejecuta directamente
    flask_app = create_app()
    flask_app.run(host="0.0.0.0", debug=True, port=8000)  # pragma: no cover
