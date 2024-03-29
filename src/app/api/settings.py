from flask import request, Blueprint
from common.api_extensions import success, error
import pickledb
from app.api.version import API_VERSION
import os
from app.config import basedir
from auth import jwt_required_user

api = Blueprint("settings_api", __name__)

settings_route = f"/api/v{API_VERSION}/settings"

@api.route(settings_route, methods=["GET"])
@jwt_required_user()
def read_settings():
    settings = pickledb.load(os.path.join(basedir, "settings.json"), True, sig=False)
    db = settings.get("db")
    if not db:
        return success({
            "db": {
                "host": "", 
                "login": "", 
                "name": "", 
                "password": ""
            }
        })
    return success({"db" : db})

@api.route(settings_route, methods=["PUT"])
@jwt_required_user()
def update_settings():
    settings = pickledb.load(os.path.join(basedir, "settings.json"), True, sig=False)
    db = {
        "host": request.args.get("host", "", type=str), 
        "login": request.args.get("name", "", type=str), 
        "name": request.args.get("login", "", type=str), 
        "password": request.args.get("password", "", type=str)
    }
    settings.set("db", db)
    return success()