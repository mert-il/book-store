from flask_sessions import Session

sess = Session()

def init_session(app):
    sess.init_app(app)