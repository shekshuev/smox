from flask_restful import Resource, abort
from flask import jsonify, request, make_response
from playhouse.shortcuts import model_to_dict, dict_to_model
from models import *
import vk
import datetime

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
                model = query.get()
                profile = model_to_dict(model)
                #profile["tasks"] = [ model_to_dict(task) for task in model.tasks ]
                return success({ "access_profile": profile })
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

    __ACCESS_TOKEN_ORYOL = "b87c995cb87c995cb87c995c55b808ad75bb87cb87c995ce7f1e962b8193502ba25154f"
    __VK_API_VERSION = 5.95

    def __init__(self):
        session = vk.Session(access_token=self.__ACCESS_TOKEN_ORYOL)
        self.__vk_api = vk.API(session, v=self.__VK_API_VERSION)

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

    def post(self):
        if "request" in request.args:
            res = self.__vk_api.utils.resolveScreenName(screen_name=request.args.get("request"))
            if res.get("type") == "group":
                group = self.__vk_api.groups.getById(group_id=res.get("object_id"), fields=[ "description" ])[0]
                source = SourceModel.create(**{ 
                                    "source_id": -int(group.get("id")), 
                                    "name": group.get("name"),
                                    "domain": group.get("screen_name"),
                                    "description": group.get("description"),
                                    "photo": group.get("photo_200") 
                                    })
                return success({ "source": model_to_dict(source)})
        else:
            return error({ "Message": "Wrong request!" })

    def put(self): 
        pass

    def delete(self):
        id = request.args.get("id", 0, type=int)
        if id <= 0:
            return error({ "message": f"Wrong id = {request.args.get('id')}" })
        res = SourceModel.delete_by_id(id)
        if bool(res):
            return success({"id": id})
        else: 
            return error({ "message": f"Wrong id = {request.args.get('id')}" })

    


class Task(Resource):
    def get(self):
        if not "id" in request.args:
            return success({ "tasks": list(TaskModel.select().dicts() ) })
        id = request.args.get("id", 0, type=int)
        if id <= 0:
            return error({ "message": f"Wrong id = {request.args.get('id')}" })
        else:
            query = TaskModel.select().where(TaskModel.id == id)
            if query.exists():
                return success({ "task": model_to_dict(query.get()) })
            else:
                return error({"Message": f"Wrong id = {id}"})

    def post(self):
        access_profile_id = request.args.get("access_profile_id")
        if not access_profile_id:
            return error({"message": "Access profile id cannot be null or empty!"})
        profile = AccessProfileModel.select().where(AccessProfileModel.id == access_profile_id)
        if profile.exists():
            task = TaskModel.create(access_profile=profile.first(), begin_datetime=datetime.datetime.now(), end_datetime=None)
            return success({ "task": model_to_dict(task) })
        else:
            return error({"Message": f"Wrong access profile id = {access_profile_id}"})

    def put(self):
        pass

    def delete(self):
        id = request.args.get("id", 0, type=int)
        if id <= 0:
            return error({ "message": f"Wrong id = {request.args.get('id')}" })
        res = TaskModel.delete_by_id(id)
        if bool(res):
            return success({"id": id})
        else: 
            return error({ "message": f"Wrong id = {request.args.get('id')}" })