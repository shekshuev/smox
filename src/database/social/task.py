from database import db
from database.social.task_source import TaskSourceModel
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class TaskModel(db.Model):
    __tablename__ = "tasks"
    id = db.Column(db.Integer, primary_key=True)
    is_finished = db.Column(db.Boolean, nullable=False, default=False)
    begin_datetime = db.Column(db.DateTime, nullable=False)
    end_datetime = db.Column(db.DateTime, nullable=True)
    requests_count = db.Column(db.Integer, nullable=False, default=0)
    access_profile_id = db.Column(db.Integer, db.ForeignKey("access_profiles.id"), nullable=False)
    is_error = db.Column(db.Boolean, nullable=False, default=False)
    error = db.Column(db.Text, nullable=False, default="")
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

class TaskSchemaNoRel(SQLAlchemyAutoSchema):
    class Meta:
        model = TaskModel
        include_relationships = False
        load_instance = True