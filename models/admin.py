from services.database import db
from flask_login import UserMixin

class Admin(db.Document, UserMixin):
    email = db.StringField(max_length=255)
    password = db.StringField()