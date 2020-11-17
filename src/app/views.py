from flask import render_template
from flask import Blueprint

views = Blueprint("views", __name__)

@views.route("/")
def index():
    return render_template("smox-app/index.html")