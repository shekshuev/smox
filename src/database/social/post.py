from database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class PostModel(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, nullable=False, default=0)
    owner_id = db.Column(db.Integer, nullable=False, default=0)
    from_id = db.Column(db.Integer, nullable=False, default=0)
    source_id = db.Column(db.Integer, db.ForeignKey("sources.id"), nullable=False)
    posted_date = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=False, default="")
    target = db.Column(db.Integer, nullable=False, default=0)
    attachments = db.relationship("PostAttachmentModel", backref="post", lazy=True)
    time_stamps = db.relationship("PostTimestampModel", backref="post", lazy=True)