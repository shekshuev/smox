from database import SocialModel
from sqlalchemy import Index
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, Integer, ForeignKey, DateTime

class PostTimestampModel(SocialModel):
    __tablename__ = "post_timestamp"
    post_id = Column(Integer, ForeignKey("post.id", ondelete="RESTRICT", name="fk_post_id_post_timestamp"), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, primary_key=True)
    likes_count = Column(Integer, nullable=False, default=0)
    reposts_count = Column(Integer, nullable=False, default=0)
    views_count = Column(Integer, nullable=False, default=0)
    comments_count = Column(Integer, nullable=False, default=0)

    __table_args__ = (Index('pk_idx_post_timestamp', "post_id", "created_at", unique=True), )

class PostTimestampSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = PostTimestampModel
        include_relationships = True
        load_instance = True
    