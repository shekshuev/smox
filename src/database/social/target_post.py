from database import db

class TargetPostModel(db.Model):
    __tablename__ = "target_post"
    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False, primary_key=True)
    target_id = db.Column(db.Integer, db.ForeignKey("target.id"), nullable=False, primary_key=True)