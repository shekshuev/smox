from flask import request, Blueprint
from database import db
from database.social.source import SourceModel
from common.api_extensions import success, error
from app.api.version import API_VERSION, VK_API_VERSION
import vk
from flask_jwt_extended import jwt_required

api = Blueprint("source_api", __name__)

source_route = f"/api/v{API_VERSION}/source"

@api.route(source_route, methods=["GET"])
@jwt_required
def read_source():
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
                return success({ "source": source.to_dict(rel=True)})
        else:
            return error({ "Message": "Wrong request!" })
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
@jwt_required
def create_source():
    source_id = request.args.get("source_id")
    if not source_id:
        return error({"message": "Source id cannot be null or empty!"})
    name = request.args.get("name", "", type=str)
    domain = request.args.get("domain", "", type=str)
    description = request.args.get("description", "", type=str)
    photo = request.args.get("photo", "", type=str)
    source = SourceModel(source_id=source_id, name=name, domain=domain, description=description, photo=photo)
    db.session.add(source)
    db.session.commit()
    return success({ "source": source.to_dict() })

@api.route(source_route, methods=["DELETE"])
@jwt_required
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

