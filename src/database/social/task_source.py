from database import SocialModel
from marshmallow import fields
from sqlalchemy import Index
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from database.social.source import SourceModel, SourceSchema
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class TaskSourceModel(SocialModel):
    __tablename__ = "task_source"
    source_id = Column(Integer, ForeignKey("source.id", ondelete="RESTRICT", name="fk_source_id_task_source"), nullable=False, primary_key=True)
    source = relationship(SourceModel)
    task_id = Column(Integer, ForeignKey("task.id", ondelete="CASCADE", name="fk_task_id_task_source"), nullable=False, primary_key=True)
    total_objects_downloaded = Column(Integer, nullable=False, default=0)
    offset = Column(Integer, nullable=False, default=0)
    count = Column(Integer, nullable=False, default=0)
    begin_count = Column(Integer, nullable=False, default=0)

    __table_args__ = (Index('pk_idx_task_source', "source_id", "task_id", unique=True), )

    def to_dict(self):
        return TaskSourceSchema().dump(self)

class TaskSourceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TaskSourceModel
        load_instance = True
        include_fk = True
    source = fields.Nested(SourceSchema)