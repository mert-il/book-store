from flask_mail import Mail, Message 
from flask_executor import Executor

mail = Mail()
executor = Executor()

def init_mail(app):
    mail.init_app(app)
    executor.init_app(app)

def send_mail(msg):
    mail.send(msg)

def send_mail_queued(sender, recipients, subject, message):
    msg = Message(sender=sender, recipients=recipients, subject=subject, body=message)
    executor.submit(send_mail, msg)