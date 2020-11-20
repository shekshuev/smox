from peewee import SqliteDatabase
from flask_sqlalchemy import SQLAlchemy

dbhandle = SqliteDatabase("database.db")

db = SQLAlchemy()