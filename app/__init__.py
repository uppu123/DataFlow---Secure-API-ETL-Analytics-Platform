from flask import Flask

from app.config import Config
from app.extensions import db, jwt, bcrypt


def create_app():
    """
    Application Factory Function
    Creates and configures the Flask application.
    """

    app = Flask(__name__)

    # Load configuration
    app.config.from_object(Config)

    # Initialize Flask Extensions
    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    # Register Blueprints
    from app.routes.home import home_bp

    app.register_blueprint(home_bp)

    return app