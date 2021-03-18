import os
import pickledb
basedir = os.path.abspath(os.path.dirname(__file__))

def load_database_settings(develop=False):
    if develop:
        settings = pickledb.load(os.path.join(basedir, "settings.dev.json"), True, sig=False)
    else:
        settings = pickledb.load(os.path.join(basedir, "settings.json"), True, sig=False)
    db = settings.get("db")
    if not db:
        return ""
    else:
        return f"mysql://{db['login']}:{db['password']}@{db['host']}/{db['name']}?ssl_ca=~/.mysql/root.crt&charset=utf8mb4"

class Config(object):
    SQLALCHEMY_DATABASE_URI = load_database_settings()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "Fuck them all!"
    LOG_FILE = os.path.join(basedir, "download.log")
    JWT_TOKEN_LOCATION = ['cookies']
    #JWT_ACCESS_TOKEN_EXPIRES = datetime.timedelta(seconds=1800)
    JWT_COOKIE_SECURE = False
    #JWT_REFRESH_TOKEN_EXPIRES = datetime.timedelta(days=15)
    JWT_COOKIE_CSRF_PROTECT = False 
    JWT_ACCESS_COOKIE_NAME = "access_token"

class DevelompentConfig(Config):
    SQLALCHEMY_DATABASE_URI = load_database_settings(develop=True)
