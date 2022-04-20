from distutils.debug import DEBUG
import os 

class BaseConfig(object):
    DEBUG = False 
    TESTING = False 
    PRODUCTION = False 

class ProductionConfig(BaseConfig):
    PRODUCTION = True 
    HOST = "0.0.0.0"
    PORT = os.environ.get("PORT")

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    HOST = "0.0.0.0"
    PORT = "8080"