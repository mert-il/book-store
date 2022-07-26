from models.user import User
from services.encryption import generate_hash

class UserLogic(object):
    def save(self, user: User):
        try:
            if User.objects(email=user.email).first() == None:
                user.password = generate_hash(user.password)
                user.save()
        except Exception as exception:
            raise exception

    def get(self, email: str, password: str) -> User:
        try:
            password_hash = generate_hash(password)
            user = User.objects(email=email, password=password_hash).first()
            return user
        except Exception as exception:
            raise exception

    def get_by_id(self, id: str) -> User:
        return User.objects.get_or_404(id=id)

    def update(self, id: str, new_user_data: User) -> None:
        try:
            user = User.objects.get(id=id)
            user.update(
                firstnam = new_user_data.firstname,
                lastname = new_user_data.lastname,
                email = new_user_data.email,
                street = new_user_data.street,
                housenumber = new_user_data.housenumber,
                city = new_user_data.city,
                zipcode = new_user_data.zipcode
            )
        except Exception as exception:
            raise exception

    def delete(self, id: str) -> None:
        user = User.objects.get_or_404(id=id)
        user.delete()

    def change_password(self, id: str, old_password: str, new_password: str) -> None:
        try:
            old_password_hash = generate_hash(old_password)
            new_password_hash = generate_hash(new_password)
            user = User.objects.get_or_404(id=id)
            if user.password == old_password_hash and old_password_hash != new_password_hash:
                user.update(password=new_password_hash)
        except Exception as exception:
            raise exception
