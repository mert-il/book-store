from .base_model import BaseModel, db 

class Genre(BaseModel):
    __tablename__ = "genre"
    name = db.Column(db.String(255))
    books = db.relationship("Book", backref="book", lazy=True)

    def __init__(self, name):
        self.name = name