from flask import request, Blueprint
from database.social.post import PostModel
from common.api_extensions import success, error
from app.api.version import API_VERSION
import datetime

api = Blueprint("post_api", __name__)

post_route = f"/api/v{API_VERSION}/post"

@api.route(post_route, methods=["GET"])
def read_post():
    count = request.args.get("count", 100, type=int)
    start_date = datetime.datetime.fromtimestamp(request.args.get("start_date", 0, type=float))
    end_date = datetime.datetime.fromtimestamp(request.args.get("end_date", 2147483647, type=float))
    query = PostModel.query.filter(PostModel.created_at >= start_date).filter(PostModel.created_at <= end_date)
    return success({ 
        "posts": [post.to_dict(rel=True) for post in query.limit(count)],
        "count": query.count()
    })