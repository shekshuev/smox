from datetime import date
import re
from flask_restful import Resource, abort
from flask import jsonify, request, make_response
from playhouse.shortcuts import model_to_dict, dict_to_model
from models import *
import vk
import datetime
import sys

def make_api_response(success, response, status):
    return make_response(jsonify({ "success": success, "response": response }), status)

def success(response="", status=200):
    return make_api_response(True, response, status)

def error(response="", status=400):
    return make_api_response(False, response, status)

class AccessProfile(Resource):
    def get(self):
        if not "id" in request.args:
            profiles = [model_to_dict(profile, backrefs=True) for profile in AccessProfileModel.select().iterator()]
            return success({ "access_profiles": profiles })
        id = request.args.get("id", 0, type=int)
        if id <= 0:
            return error({ "message": f"Wrong id = {request.args.get('id')}" })
        else:
            query = (AccessProfileModel.select().where(AccessProfileModel.id == id))
            if query.exists():
                model = query.get()
                profile = model_to_dict(model, backrefs=True, max_depth=1)
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
        page = request.args.get("page", 1, type=int)
        count = request.args.get("count", 10, type=int)
        return success({ 
            "logs": [model_to_dict(log) for log in LogModel.select().paginate(page, count)],
            "count": LogModel.select().count()
        })
        


class Source(Resource):

    __ACCESS_TOKEN_ORYOL = "b87c995cb87c995cb87c995c55b808ad75bb87cb87c995ce7f1e962b8193502ba25154f"
    __VK_API_VERSION = 5.95

    def __init__(self):
        session = vk.Session(access_token=self.__ACCESS_TOKEN_ORYOL)
        self.__vk_api = vk.API(session, v=self.__VK_API_VERSION)

    def get(self):
        if not "id" in request.args:
            sources = [model_to_dict(source, backrefs=True) for source in SourceModel.select().iterator()]
            return success({ "sources": sources })
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
            tasks = [model_to_dict(task_model, backrefs=True) for task_model in TaskModel.select().iterator()]
            return success({ "tasks": tasks })
        id = request.args.get("id", 0, type=int)
        if id <= 0:
            return error({ "message": f"Wrong id = {request.args.get('id')}" })
        else:
            print(id)
            query = TaskModel.select().where(TaskModel.id == id)
            print(query.exists())
            if query.exists():
                model = query.get()
                task = model_to_dict(model, backrefs=True)
                return success({ "task": task })
            else:
                return error({"Message": f"Wrong id = {id}"})

    def post(self):
        access_profile_id = request.args.get("access_profile_id")
        if not access_profile_id:
            return error({"message": "Access profile id cannot be null or empty!"})
        source_ids = set(request.args.get("source_ids").split(","))
        if len(source_ids) == 0:
            return error({"message": "At least one source id required!"})
        profile = AccessProfileModel.select().where(AccessProfileModel.id == access_profile_id)
        if not profile.exists():
            return error({"Message": f"Wrong access profile id = {access_profile_id}"})
        sources = SourceModel.select().where(SourceModel.id << source_ids)
        if not sources:
            return error({"Message": f"Wrong sources ids = {source_ids}"})
        elif len(sources) < len(source_ids):
            find_ids = set([source.id for source in sources])
            return error({"Message": f"Wrong sources ids = {source_ids-find_ids}"})
        else:
            task = TaskModel.create(access_profile=profile.first(), begin_datetime=datetime.datetime.now(), end_datetime=None)
            for source in sources:
                task_source = TaskSourceModel.create(source=source, task=task)
            
            return success({ "task": model_to_dict(task) })

    def put(self):
        pass

    def delete(self):
        id = request.args.get("id", 0, type=int)
        if id <= 0:
            return error({ "message": f"Wrong id = {request.args.get('id')}" })
        res = TaskModel.delete_by_id(id)
        # Cascade doesn't work
        res = TaskSourceModel.delete().where(TaskSourceModel.task == id).execute()
        if bool(res):
            return success({"id": id})
        else: 
            return error({ "message": f"Wrong id = {request.args.get('id')}" })



class TaskSource(Resource):
    def get(self):
        if not "id" in request.args:
            task_sources = [model_to_dict(task_source, backrefs=True) for task_source in TaskSourceModel.select().iterator()]
            return success({ "task_sources": task_sources })
        id = request.args.get("id", 0, type=int)
        if id <= 0:
            return error({ "message": f"Wrong id = {request.args.get('id')}" })
        else:
            query = TaskSourceModel.select().where(TaskSourceModel.id == id)
            if query.exists():
                return success({ "task_source": model_to_dict(query.get()) })
            else:
                return error({"Message": f"Wrong id = {id}"})

    def post(self):
        pass  
            

    def put(self):
        pass

    def delete(self):
        pass



class Post(Resource):
    def get(self):
        if not "id" in request.args:
            page = request.args.get("page", 1, type=int)
            count = request.args.get("count", 10, type=int)
            start_date = datetime.datetime.fromtimestamp(request.args.get("start_date", 0, type=float))
            end_date = datetime.datetime.fromtimestamp(request.args.get("end_date", 2147483647, type=float))
            return success({ 
                "posts": [model_to_dict(post, backrefs=True) for post in PostModel.select().where(PostModel.posted_date >= start_date and PostModel.posted_date <= end_date).paginate(page, count)],
                "count": PostModel.select().count()
            })
        id = request.args.get("id", 0, type=int)
        if id <= 0:
            return error({ "message": f"Wrong id = {request.args.get('id')}" })


    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass