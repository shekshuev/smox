from flask import request, Blueprint
from database import db
import database
from database.social.access_profile import AccessProfileModel
from database.social.target import TargetModel
from database.social.post import PostModel
from common.api_extensions import success, error
from app.api.version import API_VERSION
from sqlalchemy import and_, Date, cast
from app.model import XGBModel
import datetime

api = Blueprint("target_api", __name__)

target_route = f"/api/v{API_VERSION}/target"

@api.route(target_route, methods=["GET"])
def read_target():
    if not "id" in request.args:
        targets = [ {**target.to_dict(), **{"posts_count": len(target.posts) }} for target in TargetModel.query.all()]
        return success({ "targets": targets })
    id = request.args.get("id", 0, type=int)
    if id <= 0:
        return error({ "message": f"Wrong id = {request.args.get('id')}" })
    else:
        target = TargetModel.query.get(id)
        if target:
            return success({ "target": target.to_dict() })
        else:
            return error({"Message": f"Wrong id = {id}"})

@api.route(target_route, methods=["POST"])
def create_target():
    title = request.args.get("title")
    if not title or title == "":
        title = "Untitled"
    keywords_str = request.args.get("keywords")
    if not keywords_str:
        return error({"message": "Keywords cannot be null or empty!"})
    begin_date = request.args.get("begin_date")
    if not begin_date:
        return error({"message": "Begin date cannot be null or empty!"})
    end_date = request.args.get("end_date")
    if not end_date:
        return error({"message": "End date cannot be null or empty!"})
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
    try:
        keywords = keywords_str.split("|")
        posts = PostModel.query.filter(and_(PostModel.text.ilike(f"%{word}%") for word in keywords), cast(PostModel.created_at, Date) >= begin_date, cast(PostModel.created_at, Date) <= end_date)
        target = TargetModel(title=title, keywords=keywords_str, begin_date=begin_date, end_date=end_date, posts=posts.all(), result=0, reliability=0)
        xgb = XGBModel()
        target.result = xgb.predict(target.to_dataframe())
        db.session.add(target)
        db.session.commit()
        return success({ "target": {**target.to_dict(), **{"posts_count": len(target.posts) }} })
    except Exception as e:
        return error({"message": str(e)})

@api.route(target_route, methods=["DELETE"])
def delete_target():
    id = request.args.get("id", 0, type=int)
    if id <= 0:
        return error({ "message": f"Wrong id = {request.args.get('id')}" })
    target = TargetModel.query.get(id)
    if target:
        db.session.delete(target)
        db.session.commit()
        return success({"id": id})
    else: 
        return error({ "message": f"Wrong id = {request.args.get('id')}" })