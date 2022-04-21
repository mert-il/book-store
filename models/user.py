from .base_model import BaseModel, db 

class User(BaseModel):
    __tablename__ = "user"
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password_hash = db.Column(db.Text)
    street = db.Column(db.String(255))
    house_number = db.Column(db.String(10))
    city = db.Column(db.String(255))
    zip_code = db.Column(db.String(10))

    def __init__(self, firstname, lastname, email, password_hash, street, house_number, city, zip_code):
        self.firstname = firstname 
        self.lastname = lastname 
        self.email = email
        self.password_hash = password_hash
        self.street = street 
        self.house_number = house_number
        self.city = city 
        self.zip_code = zip_code