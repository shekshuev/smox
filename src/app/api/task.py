from flask import request, Blueprint
from database import db
from database.social.task import TaskModel
from database.social.access_profile import AccessProfileModel
from database.social.source import SourceModel
from database.social.task_source import TaskSourceModel
from common.api_extensions import success, error
from app.api.version import API_VERSION
import datetime

api = Blueprint("task_api", __name__)

task_route = f"/api/v{API_VERSION}/task"

@api.route(task_route, methods=["GET"])
def read_task():
    if not "id" in request.args:
        tasks = [task.to_dict(True) for task in TaskModel.query.all()]
        return success({ "tasks": tasks })
    id = request.args.get("id", 0, type=int)
    if id <= 0:
        return error({ "message": f"Wrong id = {request.args.get('id')}" })
    else:
        task = TaskModel.query.get(id)
        if task:
            return success({ "task": task.to_dict() })
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
    profile = AccessProfileModel.query.get(access_profile_id)
    if not profile:
        return error({"Message": f"Wrong access profile id = {access_profile_id}"})
    sources = SourceModel.query.filter(SourceModel.id.in_(source_ids)).all()
    if not sources:
        return error({"Message": f"Wrong sources ids = {source_ids}"})
    elif len(sources) < len(source_ids):
        find_ids = set([source.id for source in sources])
        return error({"Message": f"Wrong sources ids = {source_ids-find_ids}"})
    else:
        task = TaskModel(access_profile_id=profile.id, begin_datetime=datetime.datetime.now(), end_datetime=None)
        db.session.add(task)
        db.session.commit()
        for source in sources:
            task_source = TaskSourceModel(source_id=source.id, task_id=task.id)   
            db.session.add(task_source)
        db.session.commit()     
        return success({ "task": task.to_dict(True) })

@api.route(task_route, methods=["PUT"])
def stop_task():
    print(request.args)
    id = request.args.get("id", 0, type=int)
    if id <= 0:
        return error({ "message": f"Wrong id = { request.args.get('id')}" })
    task = TaskModel.query.get(id)
    if task:
        task.is_finished = True
        task.end_datetime = datetime.datetime.now()
        db.session.commit()
        return success({"task": task.to_dict(True)})
    else: 
        return error({ "message": f"Wrong id = { request.args.get('id')}" })

    
@api.route(task_route, methods=["DELETE"])
def delete_task():
    id = request.args.get("id", 0, type=int)
    if id <= 0:
        return error({ "message": f"Wrong id = { request.args.get('id')}" })
    task = TaskModel.query.get(id)
    if task:
        for ts in task.task_sources:
            db.session.delete(ts)
        db.session.delete(task)
        db.session.commit()
        return success({"id": id})
    else: 
        return error({ "message": f"Wrong id = { request.args.get('id')}" })
