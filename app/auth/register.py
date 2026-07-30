from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User
from app.auth.jwt_handler import hash_password

register_bp = Blueprint("register", __name__)

@register_bp.route("/api/auth/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if not all([name, email, password]):
        return jsonify({"message": "All fields are required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already exists"}), 400

    user = User(
        name=name,
        email=email,
        password_hash=hash_password(password)
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201