from database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from database.social.post_attachment import PostAttachmentModel
from database.social.post_timestamp import PostTimestampModel

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
    attachments = db.relationship(PostAttachmentModel, backref="post", lazy=True)
    time_stamps = db.relationship(PostTimestampModel, backref="post", lazy=True)

    def to_dict(self, rel=False):
        if rel:
            return PostSchema().dump(self)
        else:
            return PostSchemaNoRel().dump(self)

class PostSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PostModel
        include_relationships = True
        load_instance = True

class PostSchemaNoRel(SQLAlchemyAutoSchema):
    class Meta:
        model = PostModel
        include_relationships = True
        load_instance = False