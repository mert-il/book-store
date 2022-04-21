from flask import Flask
from flask_minify import minify
from dotenv import load_dotenv
load_dotenv() 
import os
import distutils.util 
import config 
from services.database import init_database
from views.website import website
from views.admin import admin 
from models.admin import Admin
from models.user import User
from models.book import Book
from models.author import Author
from models.publisher import Publisher
from models.genre import Genre 

def create_app():
    app = Flask(__name__, static_folder="static", static_url_path="")
    minify(app=app, html=True, js=True, cssless=True, static=True)

    if bool(distutils.util.strtobool(os.environ.get("SERVER_PRODUCTION"))) == True:
        app.config.from_object(config.ProductionConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)
    
    init_database(app)

    app.register_blueprint(website)
    app.register_blueprint(admin)

    return app 

if __name__ == "__main__":
    app = create_app()
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])