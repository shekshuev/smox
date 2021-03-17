from database import SocialModel
from marshmallow import fields
from database.social.task_source import TaskSourceModel, TaskSourceSchema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from database.social.source import SourceModel
from sqlalchemy import Column, Integer, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship, backref

class TaskModel(SocialModel):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True)
    title = Column(Text, nullable=False, default="Untitled")
    is_finished = Column(Boolean, nullable=False, default=False)
    begin_datetime = Column(DateTime, nullable=False)
    end_datetime = Column(DateTime, nullable=True)
    requests_count = Column(Integer, nullable=False, default=0)
    access_profile_id = Column(Integer, ForeignKey("access_profile.id", ondelete="RESTRICT", name='fk_access_profile_id_task'), nullable=False)
    is_error = Column(Boolean, nullable=False, default=False)
    error = Column(Text, nullable=False, default="")
    sources = relationship(SourceModel, secondary=lambda: TaskSourceModel.__table__, backref=backref('tasks', lazy=True))
    task_sources = relationship(TaskSourceModel, backref="task", lazy=True)

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