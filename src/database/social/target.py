from sqlalchemy.orm import backref
from database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from database.social.target_post import TargetPostModel

class TargetModel(db.Model):
    __tablename__ = 'target'
    id = db.Column(db.Integer, primary_key=True)
    keywords = db.Column(db.Text, nullable=False)
    begin_date = db.Column(db.DateTime, nullable=True)
    end_date = db.Column(db.DateTime, nullable=True)
    posts = db.relationship("PostModel", secondary=lambda: TargetPostModel.__table__, backref=db.backref('targets', lazy=True))
    result = db.Column(db.Float, nullable=True)
    reliability = db.Column(db.Float, nullable=True)

    def to_dict(self):
        return TargetSchema().dump(self)

class TargetSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TargetModel