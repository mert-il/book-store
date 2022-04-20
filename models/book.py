from services.database import db 

class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    author = db.Column(db.String(255))
    price = db.Column(db.Float)
    blurb = db.Column(db.Text)

    def __init__(self, title, author, price, blurb):
        self.title = title 
        self.author = author 
        self.price = price 
        self.blurb = blurb