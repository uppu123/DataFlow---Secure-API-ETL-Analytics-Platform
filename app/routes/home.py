from flask import Blueprint, render_template

# Create Blueprint
home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    """
    Home Page
    """
    return render_template("index.html")