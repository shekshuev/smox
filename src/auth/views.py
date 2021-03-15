from flask import render_template
from flask import Blueprint
from flask_jwt_extended import jwt_optional, get_jwt_identity, verify_jwt_in_request_optional
from werkzeug.utils import redirect

views = Blueprint("auth_views", __name__)

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

