from services.database import db
from models.author import Author
from models.publisher import Publisher
from models.genre import Genre

class Book(db.Document):
    title = db.StringField(max_length=255)
    author = db.ReferenceField(Author)
    isban = db.StringField(max_length=100)
    publisher = db.ReferenceField(Publisher)
    genre = db.ReferenceField(Genre)
    blurb = db.StringField()
    price = db.FloatField()