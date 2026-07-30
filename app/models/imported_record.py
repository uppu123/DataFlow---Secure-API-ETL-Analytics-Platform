from datetime import datetime
from app.extensions import db


class ImportedRecord(db.Model):
    __tablename__ = "imported_records"

    id = db.Column(db.Integer, primary_key=True)

    data = db.Column(
        db.JSON,
        nullable=False
    )

    imported_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    dataset_id = db.Column(
        db.Integer,
        db.ForeignKey("datasets.id"),
        nullable=False
    )

    dataset = db.relationship(
        "Dataset",
        back_populates="records"
    )

    def __repr__(self):
        return f"<ImportedRecord {self.id}>"