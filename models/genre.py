from services.database import db

class Genre(db.Document):
    name = db.StringField(max_length=255)