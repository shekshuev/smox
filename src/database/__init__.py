from sqlalchemy.schema import CreateSchema
from sqlalchemy.orm import query, sessionmaker, scoped_session
from sqlalchemy import MetaData
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
SocialModel = db.Model