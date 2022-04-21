from services.database import db

class Author(db.Document):
    firstname = db.StringField(max_length=255)
    lastname = db.StringField(max_length=255)