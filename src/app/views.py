from flask import render_template
from flask import Blueprint
from article import generate_sources, generate_posts

views = Blueprint("app_views", __name__)

@views.route("/")
def index():
    return render_template("smox-app/index.html")

@views.route("/generate")
def generate():
    generate_posts()
    return "yes"