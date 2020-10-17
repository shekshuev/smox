from flask import Flask, jsonify
#from flask_cors import CORS
from flask_restful import Api
from api import AccessProfile
from models import AccessProfileModel
from database import dbhandle

DEBUG = True

app = Flask(__name__)
api = Api(app)
api.add_resource(AccessProfile, "/api/access_profile")
#CORS(app)

@app.route("/ping", methods=["GET"])
def ping_pong():
    return jsonify("pong")

if __name__ == "__main__":
    dbhandle.connect()
    AccessProfileModel.create_table()
    app.run()

