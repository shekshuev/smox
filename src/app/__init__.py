import sqlalchemy
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_sqlalchemy import SQLAlchemy
from database.social.models import *
from database import dbhandle 
from app.api import api as app_api
from auth.api import api as auth_api
from app.views import views as app_views
from auth.views import views as auth_views

app = Flask(__name__)
app.register_blueprint(app_api)
app.register_blueprint(auth_api)
app.register_blueprint(app_views)
app.register_blueprint(auth_views)
app.config["JWT_SECRET_KEY"] = "Fuck them all!"
jwt = JWTManager(app)
CORS(app)

usersdb = SQLAlchemy(app)

dbhandle.connect()
AccessProfileModel.create_table()
LogModel.create_table()
SourceModel.create_table()
TaskModel.create_table()
TaskSourceModel.create_table()
PostAttachmentModel.create_table()
PostTimestampModel.create_table()
PostModel.create_table()