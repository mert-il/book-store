import os 
import distutils.util

class BaseConfig(object):
    DEBUG = False 
    TESTING = False 
    PRODUCTION = False 
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(BaseConfig):
    PRODUCTION = True 
    HOST = "0.0.0.0"
    PORT = os.environ.get("PORT")
    SQLALCHEMY_DATABASE_URI = "postgresql://{}:{}@{}:{}/{}".format(
    os.environ.get("POSTGRES_USER"), 
    os.environ.get("POSTGRES_PASSWORD"), 
    os.environ.get("POSTGRES_SERVER"), 
    os.environ.get("POSTGRES_PORT"), 
    os.environ.get("POSTGRES_DATABASE")
    )
    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = os.environ.get("MAIL_PORT")
    MAIL_USE_SSL = bool(distutils.util.strtobool(os.environ.get("MAIL_USE_SSL", "True")))
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class DevelopmentConfig(BaseConfig):
    DEVELOPTMENT=True
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = "8080"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"