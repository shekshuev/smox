from flask_jwt_extended.utils import create_access_token
from flask import jsonify, request, make_response, Blueprint
from common.api_extensions import success, error

api = Blueprint("auth_api", __name__)

API_VERSION = 1.0

login_route = f"/api/v{API_VERSION}/login"
logout_route = f"/api/v{API_VERSION}/logout"

@api.route(login_route, methods=["POST"])
def login():
    username = request.args.get("username")
    if not username:
        return error({"message": "Username cannot be null or empty!"})
    password = request.args.get("password")
    if not password:
        return error({"message": "Password cannot be null or empty!"})
    token = authentificate(username, password)
    print(token)
    return success({ "token": token })
    

def authentificate(username, password):
    if (username == "admin" and password == "admin"):
        return create_access_token(identity={
            "role": "admin"
        }, expires_delta=False)