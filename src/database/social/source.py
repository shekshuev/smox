from database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from marshmallow import fields

class SourceModel(db.Model):
    __tablename__ = "source"
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    domain = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.Text, nullable=False)

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



        