from flask import request, Blueprint
from database.social.post import PostModel
from common.api_extensions import success, error
from app.api.version import API_VERSION
from database.social.target import TargetModel 

from time import sleep

api = Blueprint("post_api", __name__)

post_route = f"/api/v{API_VERSION}/post"

@api.route(post_route, methods=["GET"])
def read_post():
    sleep(2)
    count = request.args.get("count", 100, type=int)
    offset = request.args.get("offset", 0, type=int)
    target_id = request.args.get("target_id", 0, type=int)
    print(count, offset, target_id)
    query = PostModel.query
    if target_id > 0:
        query = query.join(PostModel.targets).filter(TargetModel.id == target_id)
    return success({ 
        "posts": [ post.to_dict(rel=True) for post in query.offset(offset).limit(count) ],
        "count": query.count()
    })