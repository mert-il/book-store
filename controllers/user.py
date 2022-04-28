import os
from models.user import User
from services.encryption import bcrypt
from services.mail import send_mail_queued
from services.exception import BasicException

def create_user(user):
    try:
        if User.objects(email=user.email).first() == None:
            user.password = bcrypt.generate_password_hash(user.password)
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

def signin_user(email, password):
    try:
        user = User.objects(email=email, password=bcrypt.generate_password_hash(password)).first()
        if user:
            pass 
    except Exception as e:
        raise BasicException(message = str(e), HTTPCode = 400)