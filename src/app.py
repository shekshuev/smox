from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api
from api import *
from models import *
from database import dbhandle 


DEBUG = True
API_VERSION = 1.0

app = Flask(__name__)
api = Api(app)
api.add_resource(AccessProfile, f"/api/v{API_VERSION}/access_profiles")
api.add_resource(Log, f"/api/v{API_VERSION}/logs")
api.add_resource(Source, f"/api/v{API_VERSION}/sources")
api.add_resource(Task, f"/api/v{API_VERSION}/tasks")
api.add_resource(TaskSource, f"/api/v{API_VERSION}/task_sources")
CORS(app)


@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong")


if __name__ == "__main__":
    dbhandle.connect()
    AccessProfileModel.create_table()
    LogModel.create_table()
    SourceModel.create_table()
    TaskModel.create_table()
    TaskSourceModel.create_table()
    app.run()

