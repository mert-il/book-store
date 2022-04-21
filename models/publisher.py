from services.database import db

class Publisher(db.Document):
    name = db.StringField(max_length=255)