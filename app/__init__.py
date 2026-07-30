from flask import Flask, app

from app.config import Config
from app.extensions import db, jwt, bcrypt, migrate
# from app.auth.register import register_bp

# app.register_blueprint(register_bp)

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
    migrate.init_app(app, db)

    # Register Blueprints
    from app.routes.home import home_bp

    app.register_blueprint(home_bp)

    from app.auth.register import register_bp

    app.register_blueprint(register_bp)

    from app.auth.login import login_bp

    app.register_blueprint(login_bp)

    from app.auth.profile import profile_bp

    app.register_blueprint(profile_bp)

    # Import models so Flask-Migrate detects them
    from app.models import User, Dataset, ImportedRecord
    return app