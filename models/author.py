from .base_model import BaseModel, db

class Author(BaseModel):
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    books = db.relationship("Book", backref="book", lazy=True)

    def __init__(self, firstname, lastname):
        self.firstname = firstname 
        self.lastname = lastname