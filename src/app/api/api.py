from flask import request, Blueprint
from database import db
from database.social.access_profile import AccessProfileModel
from database.social.log import LogModel
from database.social.source import SourceModel
import vk
import datetime
from common.api_extensions import success, error

API_VERSION = 1.0
VK_API_VERSION = 5.95

api = Blueprint("app_api", __name__)



task_route = f"/api/v{API_VERSION}/task"
task_source_route = f"/api/v{API_VERSION}/task_source"





"""



@api.route(task_route, methods=["GET"])
def read_task():
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

@api.route(task_route, methods=["POST"])
def create_task():
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
            TaskSourceModel.create(source=source, task=task)        
        return success({ "task": model_to_dict(task) })

@api.route(task_route, methods=["DELETE"])
def delete_task():
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



@api.route(task_source_route, methods=["GET"])
def read_task_source():
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



@api.route(post_route, methods=["GET"])
def read_post():
    if not "id" in request.args:
        page = request.args.get("page", 1, type=int)
        count = request.args.get("count", 10, type=int)
        start_date = datetime.datetime.fromtimestamp(request.args.get("start_date", 0, type=float))
        end_date = datetime.datetime.fromtimestamp(request.args.get("end_date", 2147483647, type=float))
        query = PostModel.select().where((PostModel.posted_date >= start_date) & (PostModel.posted_date <= end_date))
        return success({ 
            "posts": [model_to_dict(post, backrefs=True) for post in query.paginate(page, count)],
            "count": query.count()
        })
    id = request.args.get("id", 0, type=int)
    if id <= 0:
        return error({ "message": f"Wrong id = {request.args.get('id')}" })

"""