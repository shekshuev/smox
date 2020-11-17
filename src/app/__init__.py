from flask import Flask
from flask_cors import CORS
from flask_openid import OpenID
from flask_login import LoginManager
from models import *
from database import dbhandle 
from app.api import api
from app.views import views

app = Flask(__name__)
app.register_blueprint(api)
app.register_blueprint(views)
CORS(app)

dbhandle.connect()
AccessProfileModel.create_table()
LogModel.create_table()
SourceModel.create_table()
TaskModel.create_table()
TaskSourceModel.create_table()
PostAttachmentModel.create_table()
PostTimestampModel.create_table()
PostModel.create_table()