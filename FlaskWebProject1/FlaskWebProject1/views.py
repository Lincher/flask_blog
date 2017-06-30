"""
Routes and views for the flask application.
"""
import json
import datetime
from FlaskWebProject1 import *
from .models import *
from PIL import Image


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
        user=User.query.first()
    )


# @app.route('/linchuanjie/about/change', methods=['POST'])
# @login_required
# def about_change():

#     return redirect(url_for('about'))


@app.route('/linchuanjie/about/upload', methods=['POST'])
@login_required
def about_upload():
    # 更新介绍
    # import ipdb
    # ipdb.set_trace()
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
            filename = secure_filename(file.filename)
            filename = "%d.%s" % (current_user.id,
                                filename.rsplit('.', 1)[1])
            pathname = os.path.join(UPLOAD_FOLDER, filename)

            if not os.path.isabs(filename):
                pathname = os.path.join(current_app.root_path, pathname)
            # image handle
            im = Image.open(file)
            size = (200,200)
            im.thumbnail(size)
            im.save(pathname)
            current_user.avatar = filename
            db.session.add(current_user)
            db.session.commit()
            return redirect(url_for('about'))


@app.route('/linchuanjie/about/download/<filename>')
def about_download(filename):
    #  找文件
    return send_from_directory(
        UPLOAD_FOLDER, filename
    )
# os.path.isabs


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


def allowed_file(filename):
    '''文件名有. 并且.后面的文件类型被允许'''
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'),404


@app.errorhandler(500)
def internal_error(error):
    # db.session.rollback()
    return render_template('500.html'),500