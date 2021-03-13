from flask import render_template
from flask import Blueprint
from flask_jwt_extended import jwt_required, jwt_optional, verify_jwt_in_request_optional
from flask_jwt_extended.utils import get_jwt_identity
from werkzeug.utils import redirect

views = Blueprint("app_views", __name__)


def get_identity_if_logedin():
    try:
        verify_jwt_in_request_optional()
        return get_jwt_identity()
    except Exception:
        print("fuck")


@views.route("/")
@views.route("/analytics")
@views.route("/posts")
@views.route("/tasks")
@views.route("/settings")
@jwt_required
def index():
    return render_template("smox/index.html")


@views.route("/login")
@jwt_optional
def login():
    try:
        verify_jwt_in_request_optional()
        user = get_jwt_identity()
        if user != None:
            return redirect("/")
        else:
            return render_template("smox/auth.html")
    except:
        return render_template("smox/auth.html")