from flask import Flask
from flask_mongoengine import MongoEngine

db = MongoEngine()

def init_database(app: Flask):
    db.init_app(app)
