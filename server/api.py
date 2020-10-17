from flask_restful import Resource

class AccessProfile(Resource):
    def get(self):
        return "fuck you"