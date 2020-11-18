from flask import render_template
from flask import Blueprint

views = Blueprint("auth_views", __name__)

@views.route("/auth")
def auth():
    return render_template("smox-auth/index.html")

