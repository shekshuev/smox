from database import db
from sqlalchemy import Index
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class PostTimestampModel(db.Model):
    __tablename__ = "post_timestamp"
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, primary_key=True)
    likes_count = db.Column(db.Integer, nullable=False, default=0)
    reposts_count = db.Column(db.Integer, nullable=False, default=0)
    views_count = db.Column(db.Integer, nullable=False, default=0)
    comments_count = db.Column(db.Integer, nullable=False, default=0)

    __table_args__ = (Index('pk_idx_post_timestamp', "post_id", "created_at", unique=True), )

class PostTimestampSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PostTimestampModel
        include_relationships = True
        load_instance = True
    