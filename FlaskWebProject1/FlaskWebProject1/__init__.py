"""
The flask application package.
"""
from flask import Flask, blueprints
from flask_sqlalchemy import SQLAlchemy
from flask_login import (LoginManager, login_fresh,
login_required, login_url, login_user, logout_user, 
UserMixin)

app = Flask(__name__)

app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
login_manager = LoginManager(app=app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'login'


from FlaskWebProject1 import views, models
