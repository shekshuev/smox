from flask import request, Blueprint
from database import db
from database.social.access_profile import AccessProfileModel
from common.api_extensions import success, error
from app.api.version import API_VERSION
from auth import jwt_required_user

api = Blueprint("access_profile_api", __name__)

access_profile_route = f"/api/v{API_VERSION}/access_profile"

@api.route(access_profile_route, methods=["GET"])
@jwt_required_user()
def read_access_profile():
    if not "id" in request.args:
        profiles = [profile.to_dict(rel=True) for profile in AccessProfileModel.query.all()]
        return success({ "access_profiles": profiles })
    id = request.args.get("id", 0, type=int)
    if id <= 0:
        return error({ "message": f"Wrong id = {request.args.get('id')}" })
    else:
        profile = AccessProfileModel.query.get(id)
        if profile:
            return success({ "access_profile": profile.to_dict(True) })
        else:
            return error({"Message": f"Wrong id = {id}"})

@api.route(access_profile_route, methods=["POST"])
@jwt_required_user()
def create_access_profile():
    name = request.args.get("name")
    if not name:
        return error({"message": "Name cannot be null or empty!"})
    access_token = request.args.get("access_token")
    if not access_token:
        return error({"message": "Access token cannot be null or empty!"})
    try:
        profile = AccessProfileModel(name=name, access_token=access_token)
        db.session.add(profile)
        db.session.commit()
        return success({ "access_profile": profile.to_dict()})
    except Exception as e:
        return error({"message": str(e)})

@api.route(access_profile_route, methods=["PUT"])
@jwt_required_user()
def update_access_profile():
    id = request.args.get("id")
    if not id:
        return error({"message": "Id cannot be null or empty!"})
    name = request.args.get("name")
    if not name:
        return error({"message": "Name cannot be null or empty!"})
    access_token = request.args.get("access_token")
    if not access_token:
        return error({"message": "Access token cannot be null or empty!"})
    try:
        profile = AccessProfileModel.query.get(id)
        if profile:
            profile.name = name
            profile.access_token = access_token
            db.session.commit()
            return success({ "access_profile": profile.to_dict(True) })
        else:
            return error({"Message": f"Wrong id = {id}"})
    except Exception as e:
        return error({"message": str(e)})

@api.route(access_profile_route, methods=["DELETE"])
@jwt_required_user()
def delete_access_profile():
    id = request.args.get("id", 0, type=int)
    if id <= 0:
        return error({ "message": f"Wrong id = {request.args.get('id')}" })
    profile = AccessProfileModel.query.get(id)
    if profile:
        db.session.delete(profile)
        db.session.commit()
        return success({"id": id})
    else: 
        return error({ "message": f"Wrong id = {request.args.get('id')}" })
