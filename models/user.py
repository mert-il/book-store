from services.database import db

class User(db.Document):
    firstname = db.StringField(max_length=255)
    lastname = db.StringField(max_length=255)
    email = db.StringField(max_length=255) 
    password_hash = db.StringField() 
    street = db.StringField(max_length=255)
    house_number = db.StringField(max_length=10)
    city = db.StringField(max_length=255)
    zip_code = db.StringField(max_length=10)