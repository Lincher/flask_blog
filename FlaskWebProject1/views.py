"""
Routes and views for the flask application.
"""
import json
import datetime
from PIL import Image
from .models import User,Post
from FlaskWebProject1 import *
import werkzeug
import ipdb

year = datetime.datetime.now().year


@app.route('/')
def home():
    """Renders the home page."""
    # import ipdb;ipdb.set_trace()
    users = User.query.all()
    return render_template(
            'home.html',
            users=users,
            year=year
        )


@app.route('/<domain>')
def index(domain):
    # ipdb.sset_trace()
    if domain is None or domain == 'favicon.ico':
        users = User.query.all()
        return render_template(
                'home.html',
                users=users,
                year=year
            )
    else:
        user = User.query.filter_by(domain_name=domain).first()
        try:
            posts=user.post.all()
        except AttributeError:
            posts=None
        # for i,post in enumerate(posts):
        #     posts
        return render_template(
            'index.html',
            title='Home Page',
            year=year,
            user=user,
            posts=posts
        )


@app.route('/<domain>/about')
def about(domain):
    """Renders the about page."""
    # if request.method == 'get':
    return render_template(
        'about.html',
        title='About',
        year=year,
        message='Your application description page.',
        user=User.query.filter_by(domain_name=domain).first()
    )


# @app.route('/linchuanjie/about/change', methods=['POST'])
# @login_required
# def about_change():

#     return redirect(url_for('about'))


@app.route('/<domain>/about/upload', methods=['POST'])
@login_required
def about_upload(domain):
    # 更新介绍
    current_user.introduction = request.form.get("introduction")
    db.session.add(current_user)
    # 更新头像
    file = request.files['file']
    # 后缀名正确
    if not file:
        db.session.commit()
        return redirect(url_for('about'))
    else:
        if not allowed_file(file.filename.lower()):
            flash('错误的文件类型')
            db.session.commit()
            return redirect(url_for('about'))
        else:
            filename = werkzeug.secure_filename(file.filename)
            filename = "%d.%s" % (current_user.id,
                                  filename.rsplit('.', 1)[1])
            pathname = os.path.join(UPLOAD_FOLDER, filename)

            if not os.path.isabs(filename):
                pathname = os.path.join(current_app.root_path, pathname)
            # image handle
            im = Image.open(file)
            size = (200, 200)
            im.thumbnail(size)
            im.save(pathname)
            current_user.avatar = filename
            db.session.add(current_user)
            db.session.commit()
            return redirect(url_for('about'))


@app.route('/<domain>/about/download/<filename>')
def about_download(domain, filename):
    #  找文件
    return send_from_directory(
        UPLOAD_FOLDER, filename
    )
# os.path.isabs


@app.route('/<domain>/post/<int:post_id>')
def show_post(domain, post_id):
    # post = Post.query.filter_by(id=post_id).first()
    user = User.query.filter_by(domain_name=domain).first()
    return render_template(
        'post.html',
        title="Post",
        year=year,
        user=user,
        post=user.post.filter_by(id=post_id).first()
    )


def allowed_file(filename):
    '''文件名有. 并且.后面的文件类型被允许'''
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
    # db.session.rollback()
    return render_template('500.html'), 500
