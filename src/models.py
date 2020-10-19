from peewee import DateTimeField, IntegerField, Model, PrimaryKeyField, CharField, SmallIntegerField, TextField
from database import dbhandle

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
    date_time = DateTimeField()
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


