from services.database import db
from models.user import User 
from models.book import Book

class Order(db.Document):
    user = db.ReferenceField(User)
    book = db.ReferenceField(Book)
    date = db.DateTimeField()