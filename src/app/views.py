from flask import render_template
from flask import Blueprint

views = Blueprint("app_views", __name__)

@views.route("/")
@views.route("/analytics")
@views.route("/posts")
@views.route("/tasks")
@views.route("/settings")
def index():
    return render_template("smox-app/index.html")