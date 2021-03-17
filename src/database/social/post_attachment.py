from database import SocialModel
from enum import IntEnum
from sqlalchemy import Column, Integer, Text, ForeignKey

class AttachmentType(IntEnum):
    photo = 1
    video = 2
    audio = 3
    document = 4
    link = 5
    undefined = 0


class PostAttachmentModel(SocialModel):
    __tablename__ = "post_attachment"
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey("post.id", ondelete="RESTRICT", name="fk_post_id_post_attachment"), nullable=False)
    type = Column(Integer, nullable=False, default=0)
    title = Column(Text, nullable=False, default="untitled")
    text = Column(Text, nullable=False, default="")
    url = Column(Text, nullable=False, default="")