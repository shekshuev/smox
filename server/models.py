from peewee import Model, PrimaryKeyField, CharField
from database import dbhandle

class BaseModel(Model):
    class Meta:
        database = dbhandle

class AccessProfileModel(BaseModel):
    id = PrimaryKeyField(null=False)
    name = CharField(max_length=100)
    access_token = CharField(max_length=100)

    class Meta:
        db_table = "access_profiles"

