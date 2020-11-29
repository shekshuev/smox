from database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from enum import IntEnum

class AttachmentType(IntEnum):
    photo = 1
    video = 2
    audio = 3
    document = 4
    link = 5
    undefined = 0


class PostAttachmentModel(db.Model):
    __tablename__ = "post_attachment"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    type = db.Column(db.Integer, nullable=False, default=0)
    title = db.Column(db.Text, nullable=False)
    text = db.Column(db.Text, nullable=False)
    url = db.Column(db.Text, nullable=False, default="")