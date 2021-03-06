"""
The flask application package.
"""
from flask import (Flask, render_template, request, redirect, url_for, session,
 flash,g, Blueprint,send_from_directory,current_app)
from flask_sqlalchemy import SQLAlchemy
from flask_login import (LoginManager, login_fresh,
login_required, login_url, login_user, logout_user, 
UserMixin,current_user)
from .config import *
from .jinja_filters import *

app = Flask(__name__)

app.config.from_pyfile('config.py')
env = app.jinja_env
env.filters['counting']= jinja_filters.counting
db = SQLAlchemy(app)
login_manager = LoginManager(app=app)
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

from FlaskWebProject1 import views, models, views_auth
