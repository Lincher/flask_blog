"""
Routes and views for the flask application.
"""
import json
import datetime
from FlaskWebProject1 import *
from .models import *


@app.route('/')
@app.route("/linchuanjie")
def home():
    """Renders the home page."""
    # import ipdb;ipdb.set_trace()
    # import IPython;IPython.embed()
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.datetime.now().year,
        posts=Post.query.all()
    )


@app.route('/linchuanjie/about')
def about():
    """Renders the about page."""
    # if request.method == 'get':
    return render_template(
        'about.html',
        title='About',
        year=datetime.datetime.now().year,
        message='Your application description page.',
        user = User.query.first()
    )   
    

@app.route('/linchuanjie/about/change',methods=['POST'])
@login_required
def about_change():
    current_user.introduction = request.form.get(
        "introduction")
    db.session.add(current_user)
    db.session.commit()
    return redirect(url_for('about'))



@app.route('/linchuanjie/post/<int:post_id>')
def show_post(post_id):
    # import ipdb;ipdb.set_trace()
    post = Post.query.filter_by(id=post_id).first()
    return render_template(
        'post.html',
        title="Post",
        year=datetime.datetime.now().year,
        post=post
        )


# @app.route('/linchuanjie/auth/login',methods=['GET','POST'])
# def login_redirect():
#     return redirect(url_for("auth.login"))

