from .base_model import BaseModel, db 

class Book(BaseModel):
    __tablename__ = "book"
    title = db.Column(db.String(255))
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    isban = db.Column(db.String(100))
    publisher_id = db.Column(db.Integer, db.ForeignKey("publisher.id"))
    genre_id = db.Column(db.Integer, db.ForeignKey("genre.id"))
    blurb = db.Column(db.Text)
    price = db.Column(db.Float)

    def __init__(self, title, author, isban, publisher_id, genre_id, blurb, price):
        self.title = title 
        self.author = author 
        self.isban = isban 
        self.publisher_id = publisher_id 
        self.genre_id = genre_id 
        self.blurb = blurb 
        self.price = price 