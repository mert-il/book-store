from services.database import db

class Author(db.Document):
    name = db.StringField(max_length=255)