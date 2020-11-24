from flask import request, Blueprint
from database.social.post import PostModel
from common.api_extensions import success, error
from app.api.version import API_VERSION
import datetime

api = Blueprint("post_api", __name__)

post_route = f"/api/v{API_VERSION}/post"

@api.route(post_route, methods=["GET"])
def read_post():
    page = request.args.get("page", 1, type=int)
    count = request.args.get("count", 10, type=int)
    start_date = datetime.datetime.fromtimestamp(request.args.get("start_date", 0, type=float))
    end_date = datetime.datetime.fromtimestamp(request.args.get("end_date", 2147483647, type=float))
    query = PostModel.query.filter(PostModel.posted_date >= start_date).filter(PostModel.posted_date <= end_date)
    return success({ 
        "posts": [post.to_dict() for post in query.offset((page - 1) * count).limit(count)],
        "count": query.count()
    })