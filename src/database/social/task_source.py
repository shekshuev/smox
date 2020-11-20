from database import db
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

class TaskSourceModel(db.Model):
    __tablename__ = "task_sources"
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, db.ForeignKey("sources.id"), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey("tasks.id"), nullable=False)
    total_objects_downloaded = db.Column(db.Integer, nullable=False, default=0)
    offset = db.Column(db.Integer, nullable=False, default=0)
    count = db.Column(db.Integer, nullable=False, default=0)
    begin_count = db.Column(db.Integer, nullable=False, default=0)

    def to_dict(self):
        return {}
        #return TaskSourceSchema().dump(self)
"""
class TaskSourceSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = TaskSourceModel
        load_instance = True
        include_fk = True"""