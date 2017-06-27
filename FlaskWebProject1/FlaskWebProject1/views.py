"""
Routes and views for the flask application.
"""
import json
import datetime
from flask import (render_template, request, redirect, url_for, session, flash,
g, Blueprint)
from FlaskWebProject1 import (app, models, login_manager,login_required)
from .models import *



@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.datetime.now().year
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.datetime.now().year,
        message='Your contact page.'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.datetime.now().year,
        message='Your application description page.'
    )


