"""
Routes and views for the flask application.
"""
import json
from datetime import datetime
from flask import render_template, request, redirect, url_for, session, flash
from FlaskWebProject1 import app, models


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )


@app.route('/login', methods=['POST'])
def login():
    user = models.User.query.filter_by(
        email=request.form.get('email')).first()
    #  不加first()或者all()只是一个查询对象，并没有执行
    #  JSON 只能用双引号
    if user is None:
        data = {"loginSuccess": False,
                "loginFailedReason": "该邮箱不存在"}
        return json.dumps(data, ensure_ascii=False)
    else:
        if user.password == request.form.get("password"):
            return json.dumps({"loginSuccess":True},
            ensure_ascii=False)
        else:
            return json.dumps({"loginSuccess": False,
                               "loginFailedReason": "密码错误"}, ensure_ascii=False)
