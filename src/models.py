from peewee import BooleanField, DateTimeField, ForeignKeyField, IntegerField, Model, PrimaryKeyField, CharField, SmallIntegerField, TextField
from database import dbhandle
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


class BaseModel(Model):
    class Meta:
        database = dbhandle



class AccessProfileModel(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=100, null=False)
    access_token = CharField(max_length=100, null=False)
    
    class Meta:
        db_table = "access_profiles"



class LogModel(BaseModel):
    id = PrimaryKeyField(null=False)
    message = TextField(null=False)
    datetime = DateTimeField()
    type = SmallIntegerField(null=False, default=0)

    class Meta:
        db_table = "logs"



class SourceModel(BaseModel):
    id = PrimaryKeyField(null=False)
    source_id = IntegerField(null=False)
    name = CharField(max_length=150, null=False)
    domain = CharField(max_length=50, null=False)
    description = TextField(null=False)
    photo = TextField(null=False)

    class Meta:
        db_table = "sources"



class TaskModel(BaseModel):
    id = PrimaryKeyField(null=False)
    is_finished = BooleanField(null=False, default=False)
    begin_datetime = DateTimeField(null=False)
    end_datetime = DateTimeField(null=True)
    requests_count = IntegerField(null=False, default=0)
    access_profile = ForeignKeyField(AccessProfileModel, backref="tasks")
    is_error = BooleanField(null=False, default=False)
    error = TextField(null=False, default="")

    class Meta:
        db_table = "tasks"



class TaskSourceModel(BaseModel):
    id = PrimaryKeyField(null=False)
    source = ForeignKeyField(SourceModel, backref="task_sources")
    task = ForeignKeyField(TaskModel, backref="task_sources", on_delete='CASCADE')
    total_objects_downloaded = IntegerField(null=False, default=0)
    offset = IntegerField(null=False, default=0)
    count = IntegerField(null=False, default=0)
    begin_count = IntegerField(null=False, default=0)

    class Meta:
        db_table = "task_sources"



class PostModel(BaseModel):
    id = PrimaryKeyField(null=False)
    post_id = IntegerField(null=False, default=0)
    owner_id = IntegerField(null=False, default=0)
    from_id = IntegerField(null=False, default=0)
    source = ForeignKeyField(SourceModel, backref="posts")
    posted_date = DateTimeField()
    text = TextField()
    target = IntegerField(null=False, default=0)

    class Meta:
        db_table = "posts"



class PostAttachmentModel(BaseModel):
    id = PrimaryKeyField(null=False)
    post = ForeignKeyField(PostModel, backref="attachments")
    type = IntegerField(null=False)
    title = TextField()
    text = TextField()
    url = TextField(null=False)

    class Meta:
        db_table = "post_attachment"


    
class PostTimestampModel(BaseModel):
    id = PrimaryKeyField(null=False)
    downloaded_date = DateTimeField()
    likes_count = IntegerField(null=False, default=0)
    reposts_count = IntegerField(null=False, default=0)
    views_count = IntegerField(null=False, default=0)
    comments_count = IntegerField(null=False, default=0)
    post = ForeignKeyField(PostModel, backref="time_stamps")

    class Meta:
        db_table = "post_timestamp"


