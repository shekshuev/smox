from database import SocialModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from database.social.target_post import TargetPostModel
import pandas as pd
from sqlalchemy import Column, Integer, Text, Float, DateTime
from sqlalchemy.orm import relationship, backref

class TargetModel(SocialModel):
    __tablename__ = 'target'
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False, default="Untitled")
    keywords = Column(Text, nullable=False)
    begin_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    posts = relationship("PostModel", secondary=lambda: TargetPostModel.__table__, backref=backref('targets', lazy=True))
    result = Column(Float, nullable=True)
    reliability = Column(Float, nullable=True)

    def to_dict(self):
        return TargetSchema().dump(self)

    def to_dataframe(self):
        rows = []
        for post in self.posts:
            for post_ts in post.timestamps:
                row = [ post.id, post.post_id, post.owner_id, post.from_id, post_ts.created_at, post_ts.likes_count, post_ts.reposts_count, post_ts.views_count, post_ts.comments_count ]
                rows.append(row)
        return pd.DataFrame(rows, columns=["id", "post_id", "owner_id", "from_id", "created_at", "likes", "reposts", "views", "comments"])
        

class TargetSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TargetModel