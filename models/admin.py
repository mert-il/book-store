from services.database import db

class Admin(db.Document):
    email = db.StringField(max_length=255)
    password_hash = db.StringField()