from database import db
from sqlalchemy import Index
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class TaskSourceModel(db.Model):
    __tablename__ = "task_source"
    source_id = db.Column(db.Integer, db.ForeignKey("source.id", ondelete="RESTRICT"), nullable=False, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey("task.id", ondelete="CASCADE"), nullable=False, primary_key=True)
    total_objects_downloaded = db.Column(db.Integer, nullable=False, default=0)
    offset = db.Column(db.Integer, nullable=False, default=0)
    count = db.Column(db.Integer, nullable=False, default=0)
    begin_count = db.Column(db.Integer, nullable=False, default=0)

    __table_args__ = (Index('pk_idx_task_source', "source_id", "task_id", unique=True), )

    def to_dict(self):
        return TaskSourceSchema().dump(self)

class TaskSourceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TaskSourceModel
        load_instance = True
        include_fk = True