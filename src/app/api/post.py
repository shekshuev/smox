from flask import request, Blueprint
from database.social.post import PostModel
from common.api_extensions import success, error
from app.api.version import API_VERSION
from database.social.target import TargetModel
from auth import jwt_required_user
from database import db

api = Blueprint("post_api", __name__)

post_route = f"/api/v{API_VERSION}/post"


@api.route(post_route, methods=["GET"])
@jwt_required_user()
def read_post():
    count = request.args.get("count", 100, type=int)
    offset = request.args.get("offset", 0, type=int)
    target_id = request.args.get("target_id", 0, type=int)
    print(count, offset, target_id)
    query = PostModel.query
    if target_id > 0:
        query = query.join(PostModel.targets).filter(
            TargetModel.id == target_id)
    return success({
        "posts": [post.to_dict(rel=True) for post in query.offset(offset).limit(count)],
        "count": query.count()
    })


@api.route(post_route, methods=["PUT"])
@jwt_required_user()
def update_post():
    id = request.form["id"]
    if not id:
        return error({"message": "Id cannot be null or empty!"})
    fit_value = request.form["fit_value"]
    if not fit_value:
        return error({"message": "Fit value cannot be null or empty!"})
    try:
        post = PostModel.query.get(id)
        if post:
            post.fit_value = fit_value
            db.session.commit()
            return success({"post": post.to_dict(True)})
        else:
            return error({"Message": f"Wrong id = {id}"})
    except Exception as e:
        return error({"message": str(e)})
