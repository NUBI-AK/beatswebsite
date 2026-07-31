##CONFIGURE TABLES

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Beat(db.Model):
    __tablename__ = "beats"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    preview_url = db.Column(db.String(250), nullable=False)
    image_url = db.Column(db.String(250))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
