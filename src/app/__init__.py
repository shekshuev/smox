import sqlalchemy
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from werkzeug.utils import redirect
from database import db
from app.config import Config, DevelompentConfig
from app.api.access_profile import api as access_profile_api
from app.api.source import api as source_api
from app.api.post import api as post_api
from app.api.task import api as task_api
from app.api.target import api as target_api
from app.api.settings import api as settings_api
from auth.api import api as auth_api
from app.views import views as app_views
from auth.views import views as auth_views

app = Flask(__name__, static_url_path="", static_folder="templates/smox")
if app.config["ENV"] == "development":
    app.config.from_object(DevelompentConfig)
else:
    app.config.from_object(Config)
jwt = JWTManager(app)
@jwt.unauthorized_loader
def redirect_callback(jwt_payload):
    return redirect("/login")

CORS(app, supports_credentials=True)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(access_profile_api)
app.register_blueprint(source_api)
app.register_blueprint(post_api)
app.register_blueprint(task_api)
app.register_blueprint(auth_api)
app.register_blueprint(target_api)
app.register_blueprint(settings_api)
app.register_blueprint(app_views)
app.register_blueprint(auth_views)


from database.social.access_profile import AccessProfileModel
from database.social.post_attachment import PostAttachmentModel
from database.social.post_timestamp import PostTimestampModel
from database.social.post import PostModel
from database.social.source import SourceModel
from database.social.task_source import TaskSourceModel
from database.social.task import TaskModel
from database.social.target import TargetModel
from database.social.target import TargetPostModel