from functools import wraps
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity, verify_jwt_in_request_optional
from common.api_extensions import make_api_response
from flask import current_app as app

def jwt_required_user():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            print(app.config["ENV"])
            if app.config["ENV"] != "development":
                verify_jwt_in_request()
            return fn(*args, **kwargs)
        return decorator
    return wrapper

def jwt_required_admin():
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt_identity()
            if claims["is_administrator"]:
                return fn(*args, **kwargs)
            else:
                return make_api_response(False, {"message": "Not authorized!"}, 401)
        return decorator
    return wrapper