from database import SocialModel
from sqlalchemy import Index
from marshmallow import fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from database.social.post_attachment import PostAttachmentModel
from database.social.post_timestamp import PostTimestampModel, PostTimestampSchema
from database.social.source import SourceModel, SourceSchemaNoRel
from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class PostModel(SocialModel):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, nullable=False, default=0)
    owner_id = Column(Integer, nullable=False, default=0)
    from_id = Column(Integer, nullable=False, default=0)
    source_id = Column(Integer, ForeignKey("source.id", ondelete="RESTRICT", name="fk_source_id_post"), nullable=False)
    source = relationship(SourceModel, backref="posts")
    created_at = Column(DateTime, nullable=False)
    text = Column(Text, nullable=False, default="")
    value = Column(Integer, nullable=False, default=-1)
    fit_value = Column(Integer, nullable=False, default=-1)
    attachments = relationship(PostAttachmentModel, backref="post", lazy=True)
    timestamps = relationship(PostTimestampModel, backref="post", lazy=True)

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
    timestamps = fields.Nested(PostTimestampSchema, many=True)
    source = fields.Nested(SourceSchemaNoRel)

class PostSchemaNoRel(SQLAlchemyAutoSchema):
    class Meta:
        model = PostModel
        include_relationships = False
        load_instance = False