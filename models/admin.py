from .base_model import BaseModel, db

class Admin(BaseModel):
    __tablename__ = "admin"
    email = db.Column(db.String(255))
    password_hash = db.Column(db.Text)

    def __init__(self, email, password_hash):
        self.email = email
        self.password_hash = password_hash