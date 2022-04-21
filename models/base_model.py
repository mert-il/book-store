from services.database import db 

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)

    def insert(self):
        db.session.add(self)
        db.session.commit()