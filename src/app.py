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
api.add_resource(AccessProfile, f"/api/v{API_VERSION}/access_profile")
api.add_resource(Log, f"/api/v{API_VERSION}/log")
api.add_resource(Source, f"/api/v{API_VERSION}/source")
api.add_resource(Task, f"/api/v{API_VERSION}/task")
api.add_resource(TaskSource, f"/api/v{API_VERSION}/task_source")
api.add_resource(Post, f"/api/v{API_VERSION}/post")
CORS(app)

if __name__ == "__main__":
    dbhandle.connect()
    AccessProfileModel.create_table()
    LogModel.create_table()
    SourceModel.create_table()
    TaskModel.create_table()
    TaskSourceModel.create_table()
    PostAttachmentModel.create_table()
    PostTimestampModel.create_table()
    PostModel.create_table()
    app.run()

