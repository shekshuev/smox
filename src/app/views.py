from flask import render_template
from flask import Blueprint
from flask_jwt_extended import jwt_required
from auth import jwt_required_user

views = Blueprint("app_views", __name__)

@views.route("/")
@views.route("/analytics")
@views.route("/posts")
@views.route("/tasks")
@views.route("/settings")
@jwt_required_user()
def index():
    return render_template("smox/index.html")