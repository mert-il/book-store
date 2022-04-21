from distutils.debug import DEBUG
import os 

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

class DevelopmentConfig(BaseConfig):
    DEVELOPTMENT=True
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = "8080"
    SQLALCHEMY_DATABASE_URI = "sqlite:///db.sqlite3"