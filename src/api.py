from flask_restful import Resource, abort
from flask import jsonify, request, make_response
from playhouse.shortcuts import model_to_dict, dict_to_model
from models import *

def make_api_response(success, response, status):
    return make_response(jsonify({ "success": success, "response": response }), status)

def success(response="", status=200):
    return make_api_response(True, response, status)

def error(response="", status=400):
    return make_api_response(False, response, status)

class AccessProfile(Resource):
    def get(self):
        if not "id" in request.args:
            return success({ "access_profiles": list(AccessProfileModel.select().dicts() ) })
        id = request.args.get("id", 0, type=int)
        if id <= 0:
            return error({ "message": f"Wrong id = {request.args.get('id')}" })
        else:
            query = AccessProfileModel.select().where(AccessProfileModel.id == id)
            if query.exists():
                return success({ "access_profile": model_to_dict(query.get()) })
            else:
                return error({"Message": f"Wrong id = {id}"})

    def post(self):
        name = request.args.get("name")
        if not name:
            return error({"message": "Name cannot be null or empty!"})
        access_token = request.args.get("access_token")
        if not access_token:
            return error({"message": "Access token cannot be null or empty!"})
        try:
            profile = AccessProfileModel.create(**{ "name": name, "access_token": access_token })
            return success({ "access_profile": model_to_dict(profile) })
        except Exception as e:
            return error({"message": str(e)})

    def put(self):
        try:
            profile = dict_to_model(AccessProfileModel, request.args.to_dict())
            if not profile.name:
                return error({"message": "Name cannot be null or empty!"})
            if not profile.access_token:
                return error({"message": "Access token cannot be null or empty!"})
            result = profile.save()
            return success({ "access_profile": model_to_dict(profile), "updated": bool(result) })
        except Exception as e:
            return error({"message": str(e)})

    def delete(self):
        id = request.args.get("id", 0, type=int)
        if id <= 0:
            return error({ "message": f"Wrong id = {request.args.get('id')}" })
        res = AccessProfileModel.delete_by_id(id)
        if bool(res):
            return success({"id": id})
        else: 
            return error({ "message": f"Wrong id = {request.args.get('id')}" })



class Log(Resource):
    def get(self):
        if not "id" in request.args:
            return success({ "logs": list(LogModel.select().dicts() ) })
        id = request.args.get("id", 0, type=int)
        if id <= 0:
            return error({ "message": f"Wrong id = {request.args.get('id')}" })
        else:
            query = LogModel.select().where(LogModel.id == id)
            if query.exists():
                return success({ "log": model_to_dict(query.get()) })
            else:
                return error({"Message": f"Wrong id = {id}"})
        


class Source(Resource):
    def get(self):
        if not "id" in request.args:
            return success({ "sources": list(SourceModel.select().dicts() ) })
        id = request.args.get("id", 0, type=int)
        if id <= 0:
            return error({ "message": f"Wrong id = {request.args.get('id')}" })
        else:
            query = SourceModel.select().where(SourceModel.id == id)
            if query.exists():
                return success({ "source": model_to_dict(query.get()) })
            else:
                return error({"Message": f"Wrong id = {id}"})
        