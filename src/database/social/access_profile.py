from database import SocialModel
from database.social.task import TaskModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class AccessProfileModel(SocialModel):
    __tablename__ = "access_profile"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    access_token = Column(String(100), nullable=False)
    tasks = relationship(TaskModel, backref="access_profile", lazy=True)

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