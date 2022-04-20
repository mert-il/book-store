from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

db = SQLAlchemy()

def initDatabase(app):
    engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
    if not database_exists(engine.url):
        create_database(engine.url)
    db.init_app(app)
    Migrate(app, db)
    db.create_all(app=app)
