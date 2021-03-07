import os
import pickledb
basedir = os.path.abspath(os.path.dirname(__file__))

def load_database_settings():
    settings = pickledb.load("settings.json", True, sig=False)
    db = settings.get("db")
    if not db:
        return ""
    else:
        return f"mysql://{db['login']}:{db['password']}@{db['host']}/{db['name']}"

class Config(object):
    #SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_DATABASE_URI = load_database_settings()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = "Fuck them all!"