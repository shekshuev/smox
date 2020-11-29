from database import db
from database.social.task_source import TaskSourceModel
from database.social.post import PostModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class SourceModel(db.Model):
    __tablename__ = "source"
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    domain = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.Text, nullable=False)
    task_sources = db.relationship(TaskSourceModel, backref="source", lazy=True)
    posts = db.relationship(PostModel, backref="source", lazy=True)

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

class SourceSchemaNoRel(SQLAlchemyAutoSchema):
    class Meta:
        model = SourceModel
        include_relationships = True
        load_instance = False
        