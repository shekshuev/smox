from flask import request, Blueprint
from database.social.log import LogModel
from common.api_extensions import success, error
import pickledb
from app.api.version import API_VERSION

api = Blueprint("settings_api", __name__)

settings_route = f"/api/v{API_VERSION}/settings"

@api.route(settings_route, methods=["GET"])
def read_settings():
    settings = pickledb.load("settings.json", True, sig=False)
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
def update_settings():
    settings = pickledb.load("settings.json", True, sig=False)
    db = {
        "host": request.args.get("host", "", type=str), 
        "login": request.args.get("name", "", type=str), 
        "name": request.args.get("login", "", type=str), 
        "password": request.args.get("password", "", type=str)
    }
    settings.set("db", db)
    return success()