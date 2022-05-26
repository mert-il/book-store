from services.database import db
from flask_login import UserMixin

class User(db.Document, UserMixin):
    firstname = db.StringField(max_length=255)
    lastname = db.StringField(max_length=255)
    email = db.StringField(max_length=255) 
    password = db.StringField() 
    street = db.StringField(max_length=255)
    housenumber = db.StringField(max_length=10)
    city = db.StringField(max_length=255)
    zipcode = db.StringField(max_length=10)