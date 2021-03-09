from flask import request, Blueprint
from database import db
from database.social.log import LogModel
from common.api_extensions import success, error
from app.api.version import API_VERSION

api = Blueprint("log_api", __name__)

log_route = f"/api/v{API_VERSION}/log"

@api.route(log_route, methods=["GET"])
def read_log():
    page = request.args.get("page", 1, type=int)
    count = request.args.get("count", 10, type=int)
    return success({ 
        "logs": [log.to_dict() for log in LogModel.query.order_by(LogModel.datetime.desc()).offset((page - 1) * count).limit(count)],
        "count": LogModel.query.count()
    })