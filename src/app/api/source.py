from flask import request, Blueprint
from database import db
from database.social.source import SourceModel
from common.api_extensions import success, error
from app.api.version import API_VERSION, VK_API_VERSION
import vk

api = Blueprint("source_api", __name__)

source_route = f"/api/v{API_VERSION}/source"

@api.route(source_route, methods=["GET"])
def read_source():
    if not "id" in request.args:
        sources = [source.to_dict(rel=True) for source in SourceModel.query.all()]
        return success({ "sources": sources })
    id = request.args.get("id", 0, type=int)
    if id <= 0:
        return error({ "message": f"Wrong id = {request.args.get('id')}" })
    else:
        source = SourceModel.query.get(id)
        if source:
            return success({ "source": source.to_dict(rel=True) })
        else:
            return error({"Message": f"Wrong id = {id}"})

@api.route(source_route, methods=["POST"])
def create_source():
    if "access_token" in request.args:
        access_token = request.args.get("access_token")
        session = vk.Session(access_token=access_token)
        vk_api = vk.API(session, v=VK_API_VERSION)
        if "request" in request.args:
            res = vk_api.utils.resolveScreenName(screen_name=request.args.get("request"))
            if res.get("type") == "group":
                group = vk_api.groups.getById(group_id=res.get("object_id"), fields=[ "description" ])[0]
                source = SourceModel(source_id=-int(group.get("id")), 
                                        name=group.get("name"), 
                                        domain=group.get("screen_name"),
                                        description=group.get("description"),
                                        photo=group.get("photo_200"))
                db.session.add(source)
                db.session.commit()
                return success({ "source": source.to_dict(rel=True)})
        else:
            return error({ "Message": "Wrong request!" })
    else:
        return error({"Message": f"No access token provided!"})

@api.route(source_route, methods=["DELETE"])
def delete_source():
    id = request.args.get("id", 0, type=int)
    if id <= 0:
        return error({ "message": f"Wrong id = {request.args.get('id')}" })
    source = SourceModel.query.get(id)
    if source:
        db.session.delete(source)
        db.session.commit()
        return success({"id": id})
    else: 
        return error({ "message": f"Wrong id = {request.args.get('id')}" })
