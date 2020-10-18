from peewee import DateTimeField, Model, PrimaryKeyField, CharField, SmallIntegerField, TextField
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


