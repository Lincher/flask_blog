"""
The flask application package.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)

from FlaskWebProject1 import *
