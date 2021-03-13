from flask_jwt_extended.utils import create_access_token, set_access_cookies, unset_access_cookies
from flask import jsonify, request, make_response, Blueprint
from common.api_extensions import success, error, make_api_response
from app.api.version import API_VERSION
from werkzeug.utils import redirect

api = Blueprint("auth_api", __name__)

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
    if token:
        response = success({ "token": token })
        set_access_cookies(response, token)
        return response
    else: 
        return make_api_response(False, {"message": "Wrong login or password!"}, 401)
    

def authentificate(username, password):
    if (username == "usgrant" and password == "usgrantsmox"):
        return create_access_token(identity={
            "username": username,
            "role": "admin"
        }, expires_delta=False)

@api.route("/logout")
def logout():
    response = redirect("/login")
    unset_access_cookies(response)
    return response