from sqlalchemy.orm import backref
from app import db
from enum import IntEnum

class LogType(IntEnum):
    info = 0
    error = 1

class AttachmentType(IntEnum):
    photo = 1
    video = 2
    audio = 3
    document = 4
    link = 5
    undefined = 0

class AccessProfileModel(db.Model):
    __tablename__ = 'access_profiles'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    access_token = db.Column(db.String(100), nullable=False)
    tasks = db.relationship("TaskModel", backref="access_profile", lazy=True)

class LogModel(db.Model):
    __tablename__ = 'logs'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.Text, nullable=False)
    datetime = db.Column(db.DateTime, nullable=False)
    type = db.Column(db.SmallInteger, nullable=False, default=0)

class SourceModel(db.Model):
    __tablename__ = "sources"
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(150), nullable=False)
    domain = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text, nullable=False)
    photo = db.Column(db.Text, nullable=False)
    task_sources = db.relationship("TaskSourceModel", backref="source", lazy=True)
    posts = db.relationship("PostModel", backref="source", lazy=True)

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
    task_sources = db.relationship("TaskSourceModel", backref="task", lazy=True)

class TaskSourceModel(db.Model):
    __tablename__ = "task_sources"
    id = db.Column(db.Integer, primary_key=True)
    source_id = db.Column(db.Integer, db.ForeignKey("sources.id"), nullable=False)
    task_id = db.Column(db.Integer, db.ForeignKey("tasks.id"), nullable=False)
    total_objects_downloaded = db.Column(db.Integer, nullable=False, default=0)
    offset = db.Column(db.Integer, nullable=False, default=0)
    count = db.Column(db.Integer, nullable=False, default=0)
    begin_count = db.Column(db.Integer, nullable=False, default=0)

class PostModel(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, nullable=False, default=0)
    owner_id = db.Column(db.Integer, nullable=False, default=0)
    from_id = db.Column(db.Integer, nullable=False, default=0)
    source_id = db.Column(db.Integer, db.ForeignKey("sources.id"), nullable=False)
    posted_date = db.Column(db.DateTime, nullable=False)
    text = db.Column(db.Text, nullable=False, default="")
    target = db.Column(db.Integer, nullable=False, default=0)
    attachments = db.relationship("PostAttachmentModel", backref="post", lazy=True)
    time_stamps = db.relationship("PostTimestampModel", backref="post", lazy=True)

class PostAttachmentModel(db.Model):
    __tablename__ = "post_attachment"
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)
    type = db.Column(db.Integer, nullable=False, default=0)
    title = db.Column(db.Text)
    text = db.Column(db.Text)
    url = db.Column(db.Text, nullable=False, default="")

class PostTimestampModel(db.Model):
    __tablename__ = "post_timestamp"
    id = db.Column(db.Integer, primary_key=True)
    downloaded_date = db.Column(db.DateTime, nullable=False)
    likes_count = db.Column(db.Integer, nullable=False, default=0)
    reposts_count = db.Column(db.Integer, nullable=False, default=0)
    views_count = db.Column(db.Integer, nullable=False, default=0)
    comments_count = db.Column(db.Integer, nullable=False, default=0)
    post_id = db.Column(db.Integer, db.ForeignKey("posts.id"), nullable=False)