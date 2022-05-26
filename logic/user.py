from models.user import User
from services.encryption import bcrypt
from .base_logic import BaseLogic

class UserLogic(BaseLogic):
    def save(self, model):
        if User.objects(email=model.email).first() == None:
            model.password = bcrypt.generate_password_hash(model.user.password).decode("utf-8")
            model.save()

    def get(self, email, password):
        password_hash = bcrypt.generate_password_hash(password).decode("utf-8")
        user = User.objects(email=email, password=password_hash).first()
        return user

    def get_by_id(self, id):
        return User.objects.get_or_404(id=id)

    def update(self, id, model):
        user = User.objects.get(id=id)
        user.update(
            firstname = model.firstname,
            latname = model.lastname,
            email = model.email,
            street = model.street,
            housenumber = model.housenumber,
            city = model.city,
            zipcode = model.zipcode
        )

    def delete(self, id):
        user = User.objects.get_or_404(id=id)
        user.delete()
