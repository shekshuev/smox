from database import SocialModel
from sqlalchemy import Index
from sqlalchemy import Column, Integer, ForeignKey

class TargetPostModel(SocialModel):
    __tablename__ = "target_post"
    post_id = Column(Integer, ForeignKey("post.id", ondelete="RESTRICT", name="fk_post_id_target_post"), nullable=False, primary_key=True)
    target_id = Column(Integer, ForeignKey("target.id", ondelete="RESTRICT", name="fk_target_id_target_post"), nullable=False, primary_key=True)

    __table_args__ = (Index('pk_idx_target_post', "post_id", "target_id", unique=True), )