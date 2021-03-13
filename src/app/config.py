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
        return f"mysql://{db['login']}:{db['password']}@{db['host']}/{db['name']}"

class Config(object):
    SQLALCHEMY_DATABASE_URI = load_database_settings()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "Fuck them all!"
    LOG_FILE = os.path.join(basedir, "download.log")

class DevelompentConfig(Config):
    SQLALCHEMY_DATABASE_URI = load_database_settings(develop=True)
