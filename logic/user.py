from models.user import User
from services.encryption import generate_hash

class UserLogic(object):
    def save(self, user):
        if User.objects(email=user.email).first() == None:
            user.password = generate_hash(user.password)
            user.save()

    def get(self, email, password) -> User:
        password_hash = generate_hash(password)
        user = User.objects(email=email, password=password_hash).first()
        return user

    def get_by_id(self, id) -> User:
        return User.objects.get_or_404(id=id)

    def update(self, id, user):
        user = User.objects.get(id=id)
        user.update(
            firstname = user.firstname,
            latname = user.lastname,
            email = user.email,
            street = user.street,
            housenumber = user.housenumber,
            city = user.city,
            zipcode = user.zipcode
        )

    def delete(self, id):
        user = User.objects.get_or_404(id=id)
        user.delete()
