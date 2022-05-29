from models.user import User
from services.encryption import generate_hash

class UserLogic(object):
    def save(self, user):
        try:
            if User.objects(email=user.email).first() == None:
                user.password = generate_hash(user.password)
                user.save()
        except Exception as exception:
            raise exception

    def get(self, email, password):
        try:
            password_hash = generate_hash(password)
            user = User.objects(email=email, password=password_hash).first()
            return user
        except Exception as exception:
            raise exception

    def get_by_id(self, id):
        return User.objects.get_or_404(id=id)

    def update(self, id, new_user_data):
        try:
            user = User.objects.get(id=id)
            user.update(
                firstname=new_user_data.firstname,
                latname=new_user_data.lastname,
                email=new_user_data.email,
                street=new_user_data.street,
                housenumber=new_user_data.housenumber,
                city=new_user_data.city,
                zipcode=new_user_data.zipcode
            )
        except Exception as exception:
            raise exception

    def delete(self, id):
        user = User.objects.get_or_404(id=id)
        user.delete()

    def change_password(self, id, old_password, new_password):
        try:
            old_password_hash = generate_hash(old_password)
            new_password_hash = generate_hash(new_password)
            user = User.objects.get_or_404(id=id)
            if user.password == old_password_hash and old_password_hash != new_password_hash:
                user.update(password=new_password_hash)
        except Exception as exception:
            raise exception
