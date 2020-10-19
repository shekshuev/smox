from flask import Flask, jsonify, request
#from flask_cors import CORS
from flask_restful import Api
from api import *
from models import *
from database import dbhandle 
import vk


DEBUG = True
API_VERSION = 1.0
ACCESS_TOKEN_ORYOL = "b87c995cb87c995cb87c995c55b808ad75bb87cb87c995ce7f1e962b8193502ba25154f"
VK_API_VERSION = 5.95

app = Flask(__name__)
api = Api(app)
api.add_resource(AccessProfile, f"/api/v{API_VERSION}/access_profiles")
api.add_resource(Log, f"/api/v{API_VERSION}/logs")
api.add_resource(Source, f"/api/v{API_VERSION}/sources")
#CORS(app)


session = vk.Session(access_token=ACCESS_TOKEN_ORYOL)
vk_api = vk.API(session, v=VK_API_VERSION)


@app.route(f"/api/v{API_VERSION}/vk/search", methods=["GET"])
def vk_search():
    res = vk_api.utils.resolveScreenName(screen_name=request.args.get("request"))
    return jsonify(res)


@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong")


if __name__ == "__main__":
    dbhandle.connect()
    AccessProfileModel.create_table()
    LogModel.create_table()
    SourceModel.create_table()
    app.run()

