from flask_mongoengine import MongoEngine

db = MongoEngine()

def init_database(app):
    db.init_app(app)
