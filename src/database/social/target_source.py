from database import db

class TargetSourceModel(db.Model):
    __tablename__ = "target_source"
    source_id = db.Column(db.Integer, db.ForeignKey("source.id"), nullable=False, primary_key=True)
    target_id = db.Column(db.Integer, db.ForeignKey("target.id"), nullable=False, primary_key=True)