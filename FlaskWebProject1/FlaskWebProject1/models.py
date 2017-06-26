import datetime
from FlaskWebProject1 import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(12))
    permission = db.Column(db.String(12))
    post = db.relationship('Post',backref='author',lazy='dynamic')

    def __init__(self, username, email, password, permission='guest'):
        self.username = username
        self.email = email
        self.password = password
        self.permission = permission

    def __repr__(self):
        return '<User %r>' % self.username

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(20))
    # 标题不能为空
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer,db.ForeignKey('user.id'))

    def __init__(self,**kw):
        super().__init__(**kw)
        self.timestamp = datetime.datetime.utcnow()

    def __repr__(self):
        return "Title: %s"%self.title