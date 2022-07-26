from flask import Flask
from flask_mail import Mail, Message 
from flask_executor import Executor

mail = Mail()
executor = Executor()

def init_mail(app: Flask) -> None:
    mail.init_app(app)
    executor.init_app(app)

def send_mail(message: str) -> None:
    mail.send(message)

def send_mail_queued(sender: str, recipients: list[str], subject: str, message: str) -> None:
    try:
        mail_message = Message(sender=sender, recipients=recipients, subject=subject, body=message)
        executor.submit(send_mail, mail_message)
    except Exception as exception:
        pass 