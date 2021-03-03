from database import db
from marshmallow import fields
from database.social.task_source import TaskSourceModel, TaskSourceSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from database.social.source import SourceModel, SourceSchema

class TaskModel(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False, default="Untitled")
    is_finished = db.Column(db.Boolean, nullable=False, default=False)
    begin_datetime = db.Column(db.DateTime, nullable=False)
    end_datetime = db.Column(db.DateTime, nullable=True)
    requests_count = db.Column(db.Integer, nullable=False, default=0)
    access_profile_id = db.Column(db.Integer, db.ForeignKey("access_profile.id", ondelete="RESTRICT"), nullable=False)
    is_error = db.Column(db.Boolean, nullable=False, default=False)
    error = db.Column(db.Text, nullable=False, default="")
    sources = db.relationship(SourceModel, secondary=lambda: TaskSourceModel.__table__, backref=db.backref('tasks', lazy=True))
    task_sources = db.relationship(TaskSourceModel, backref="task", lazy=True)
    
    def to_dict(self, rel=False):
        if rel:
            return TaskSchema().dump(self)
        else:
            return TaskSchemaNoRel().dump(self)

class TaskSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TaskModel
        include_relationships = True
        load_instance = True
        exclude = ["sources"]
    task_sources = fields.Nested(TaskSourceSchema, many=True)
    #sources = fields.Nested(SourceSchema, many=True)

class TaskSchemaNoRel(SQLAlchemyAutoSchema):
    class Meta:
        model = TaskModel
        include_relationships = False
        load_instance = True