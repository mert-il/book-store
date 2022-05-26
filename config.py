import os 
import distutils.util

class BaseConfig(object):
    DEBUG = False 
    TESTING = False 
    PRODUCTION = False 
    MONGODB_SETTINGS = {
        "host": "mongodb://{}:{}/{}".format(
            os.environ.get("MONGODB_HOST"), 
            os.environ.get("MONGODB_PORT"), 
            os.environ.get("MONGODB_DB")
        ),
        "username": os.environ.get("MONGODB_USERNAME"),
        "password": os.environ.get("MONGODB_PASSWORD"),
        "authentication_source": "admin",
        "connect": False
    }
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_SSL = bool(distutils.util.strtobool(os.environ.get("MAIL_USE_SSL", "True")))
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProductionConfig(BaseConfig):
    PRODUCTION = True 
    HOST = "0.0.0.0"
    PORT = os.environ.get("PORT")
    SECRET_KEY = os.environ.get("SECRET_KEY")
    JWT_SECRET_KEY = os.environ.get("JWT_SECRET_KEY")

class DevelopmentConfig(BaseConfig):
    DEVELOPTMENT = True
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = "8080"
    SECRET_KEY = "secretkey"
    JWT_SECRET_KEY = "jwtsecretkey"