from services.database import db 

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(255))
    lastname = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.Text)

    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname 
        self.lastname = lastname 
        self.email = email
        self.password = password