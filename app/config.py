import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()


class Config:
    """Base configuration."""

    # Flask
    SECRET_KEY = os.getenv("SECRET_KEY", "change-this-secret-key")

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv(
            "DATABASE_URL",
            "sqlite:///dataflow.db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "change-this-jwt-secret")

    # Supabase (will use in Phase 2)
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")