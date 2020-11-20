from database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from enum import IntEnum

class LogType(IntEnum):
    info = 0
    error = 1

class LogModel(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.SmallInteger, nullable=False, default=0)

    def to_dict(self):
        return LogSchema().dump(self)

class LogSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = LogModel