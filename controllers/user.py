from models.user import User
from services.hash import generate_hash

def create_user(user):
    if User.objects(email=user.email).first() == None:
        user.password = str(generate_hash(user.password))
        user.save()