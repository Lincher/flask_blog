"""
Routes and views for the flask application.
"""
import json
import datetime
from FlaskWebProject1 import *
from .models import *



@app.route('/')
@app.route("/LinChuanJie")
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


@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.datetime.now().year,
        message='Your application description page.'
    )


@app.route('/Linchuanjie/<int:post_id>')
def show_post(post_id):
    # import ipdb;ipdb.set_trace()
    post = Post.query.filter_by(id=post_id).first()
    return render_template(
        'post.html',
        title="Post",
        year=datetime.datetime.now().year,
        post=post
        )

# @app.route('/test')
# def test():
    # return redirect(url_for("show_post",post_id=1))

