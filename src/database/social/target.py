from flask_sqlalchemy import model
from sqlalchemy.orm import backref
from database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from database.social.target_post import TargetPostModel
import pandas as pd

class TargetModel(db.Model):
    __tablename__ = 'target'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False, default="Untitled")
    keywords = db.Column(db.Text, nullable=False)
    begin_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)
    posts = db.relationship("PostModel", secondary=lambda: TargetPostModel.__table__, backref=db.backref('targets', lazy=True))
    result = db.Column(db.Float, nullable=True)
    reliability = db.Column(db.Float, nullable=True)

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