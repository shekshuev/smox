import sqlalchemy
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from database import db
from database.social.models import *
from app.config import Config
from app.api import api as app_api
from app.api2 import api as app_api2
from auth.api import api as auth_api
from app.views import views as app_views
from auth.views import views as auth_views


app = Flask(__name__)
app.register_blueprint(app_api)
app.register_blueprint(app_api2)
app.register_blueprint(auth_api)
app.register_blueprint(app_views)
app.register_blueprint(auth_views)
app.config.from_object(Config)
jwt = JWTManager(app)
CORS(app)

db.init_app(app)
    #migrate = Migrate(app, db)
    #from database.social.models2 import *