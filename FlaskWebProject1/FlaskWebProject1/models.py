import datetime
from FlaskWebProject1 import db, UserMixin
from sqlalchemy import types

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(12))
    permission = db.Column(db.String(12))
    gander = db.Column(db.Boolean)
    birthdate = db.Column(db.DateTime)
    test = db.Column(types.BOOLEAN,nullable=True,default=True)
    post = db.relationship('Post',backref='author',lazy='dynamic')

    def __init__(self, username, email, password,permission='guest'):
        self.username = username
        self.email = email
        self.password = password
        self.permission = permission

    def __repr__(self):
        return '<User %r>,email:%r,password:%r,permission:%r,\
        gander:%r,birthdata:%r' % (self.username,self.email,
        self.password,self.permission,self.gander,self.birthdate)

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
