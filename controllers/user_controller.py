import os
from models.user import User
from services.encryption import bcrypt
from services.mail import send_mail_queued
from services.exception import BasicException

def create_user(user: User):
    try:
        if User.objects(email=user.email).first() == None:
            user.password = bcrypt.generate_password_hash(user.password).decode("utf-8")
            user.save()
            mail_msg = f"Hello {user.firstname} {user.lastname}, welcome to the bookstore\nYour new account was successfully created!"
            send_mail_queued(os.environ.get("MAIL_SENDER"), [user.email], "Your new bookstore account", mail_msg)
    except Exception as e:
        raise BasicException(message = str(e), HTTPCode = 400)

def delete_user(user_id):
    try:
        user = User.objects.get(id=user_id).first()
        user.delete()
        mail_msg = f"Hello {user.firstname} {user.lastname},\nYour account was successfully deleted!"
        send_mail_queued(os.environ.get("MAIL_SENDER"), [user.email], "Bookstore account deleted", mail_msg) 
    except Exception as e:
        raise BasicException(message = str(e), HTTPCode = 400)

def update_user(user_id, firstname, lastname, email, street, housenumber, city, zipcode):
    try:
        user = User.objects.get(id=user_id).first()
        user.update(
            firstname = firstname,
            lastname = lastname,
            email = email,
            street = street,
            housenumber = housenumber,
            city = city,
            zipcode = zipcode
        )
    except Exception as e:
        raise BasicException(message = str(e), HTTPCode = 400)

def get_user(email, password) -> User:
    try:
        user = User.objects(email=email, password=bcrypt.generate_password_hash(password).decode("utf-8")).first()
        return user 
    except Exception as e:
        raise BasicException(message = str(e), HTTPCode = 400)

def change_user_password(user_id, old_password, new_password) -> bool:
    try:
        user = User.objects.get(id=user_id).first()
        old_password_hash = bcrypt.generate_password_hash(old_password).decode("utf-8")
        new_password_hash = bcrypt.generate_password_hash(new_password).decode("utf-8")
        if bcrypt.check_password_hash(user.password, old_password_hash):
            if not bcrypt.check_password_hash(user.password, new_password_hash):
                user.update(password = new_password_hash)
                return True 
        else:
            return False 
    except Exception as e:
        raise BasicException(message = str(e), HTTPCode = 400)