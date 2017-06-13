from FlaskWebProject1 import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(12))
    permission = db.Column(db.Integer)

    def __init__(self, username, email, password, permission=0):
        self.username = username
        self.email = email
        self.password = password
        self.permission = permission

    def __repr__(self):
        return '<User %r>' % self.username
