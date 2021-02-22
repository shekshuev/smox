from database import db
from sqlalchemy import Index
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from database.social.post_attachment import PostAttachmentModel
from database.social.post_timestamp import PostTimestampModel

class PostModel(db.Model):
    __tablename__ = "post"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, nullable=False, default=0)
    owner_id = db.Column(db.Integer, nullable=False, default=0)
    from_id = db.Column(db.Integer, nullable=False, default=0)
    source_id = db.Column(db.Integer, db.ForeignKey("source.id"), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=False, default="")
    value = db.Column(db.Integer, nullable=False, default=0)
    attachments = db.relationship(PostAttachmentModel, backref="post", lazy=True)
    timestamps = db.relationship(PostTimestampModel, backref="post", lazy=True)

    __table_args__ = (Index('unique_idx_post', "post_id", "owner_id", "from_id", unique=True), )

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