from flask import Flask
from flask_minify import minify
from dotenv import load_dotenv
load_dotenv() 
import os 
import config 
from services.database import initDatabase
from views.website import website
from views.admin import admin 

def createApp():
    app = Flask(__name__, static_folder="static", static_url_path="")
    minify(app=app, html=True, js=True, cssless=True, static=True)

    if bool(os.environ.get("SERVER_PRODUCTION")) == True:
        app.config.from_object(config.ProductionConfig)
    else:
        app.config.from_object(config.DevelopmentConfig)

    app.register_blueprint(website)
    app.register_blueprint(admin)

    return app 

if __name__ == "__main__":
    app = createApp()
    app.run(host=app.config["HOST"], port=app.config["PORT"], debug=app.config["DEBUG"])