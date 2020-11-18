from app import usersdb as db
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
    name = db.Column(db.String(100), index=True, unique=True)
    access_token = db.Column(db.String(100), index=True, unique=True)