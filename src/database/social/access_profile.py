from database import db
from database.social.task import TaskModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class AccessProfileModel(db.Model):
    __tablename__ = "access_profile"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    access_token = db.Column(db.String(100), nullable=False)
    tasks = db.relationship(TaskModel, backref="access_profile", lazy=True)

    def to_dict(self, rel=False):
        if rel:
            return AccessProfileSchema().dump(self)
        else:
            return AccessProfileSchemaNoRel().dump(self)

class AccessProfileSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = AccessProfileModel
        include_relationships = True
        load_instance = True

class AccessProfileSchemaNoRel(SQLAlchemyAutoSchema):
    class Meta:
        model = AccessProfileModel
        include_relationships = False
        load_instance = True