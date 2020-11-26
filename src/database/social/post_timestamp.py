from database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class PostTimestampModel(db.Model):
    __tablename__ = "post_timestamp"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, primary_key=True)
    likes_count = db.Column(db.Integer, nullable=False, default=0)
    reposts_count = db.Column(db.Integer, nullable=False, default=0)
    views_count = db.Column(db.Integer, nullable=False, default=0)
    comments_count = db.Column(db.Integer, nullable=False, default=0)
    