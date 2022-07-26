from flask import Flask
from flask_login import LoginManager

login_manager = LoginManager()

def init_auth(app: Flask) -> None:
    login_manager.init_app(app)