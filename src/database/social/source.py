from database import SocialModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields
from sqlalchemy import Column, Integer, Text, String

class SourceModel(SocialModel):
    __tablename__ = "source"
    id = Column(Integer, primary_key=True)
    source_id = Column(Integer, nullable=False)
    name = Column(String(150), nullable=False)
    domain = Column(String(50), nullable=False)
    description = Column(Text, nullable=False)
    photo = Column(Text, nullable=False)

    def to_dict(self, rel=False):
        if rel:
            return SourceSchema().dump(self)
        else:
            return SourceSchemaNoRel().dump(self)

class SourceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = SourceModel
        include_relationships = True
        load_instance = True
    posts_count = fields.Function(lambda s: len(s.posts))

class SourceSchemaNoRel(SQLAlchemyAutoSchema):
    class Meta:
        model = SourceModel
        include_relationships = False
        load_instance = False



        