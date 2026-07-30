from datetime import datetime
from app.extensions import db


class Dataset(db.Model):
    __tablename__ = "datasets"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    api_url = db.Column(db.Text, nullable=False)

    headers = db.Column(db.JSON, nullable=True)

    auth_type = db.Column(db.String(50), nullable=True)

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    # Foreign Key
    owner_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    # Relationships
    owner = db.relationship(
        "User",
        back_populates="datasets"
    )

    records = db.relationship(
        "ImportedRecord",
        back_populates="dataset",
        cascade="all, delete-orphan",
        lazy=True
    )

    def __repr__(self):
        return f"<Dataset {self.name}>"