import json
from datetime import datetime
from flask import (render_template, request, redirect, url_for, session, flash,
                   g, Blueprint)
from FlaskWebProject1 import *
from .models import *

# url redirect
# 蓝图，路由模块化
auth = Blueprint('auth', __name__)


# flask-login版login
@auth.route('/login', methods=['POST'])
def login():
    # if g.user is not None and g.user.is_authenticated():

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
            import ipdb
            ipdb.set_trace()
            login_user(user,
                       remember=request.form.get("remember_me")
                       )
            return json.dumps({"loginSuccess": True},
                              ensure_ascii=False)
        else:
            return json.dumps({"loginSuccess": False,
                               "loginFailedReason": "密码错误"},
                              ensure_ascii=False)


@auth.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
    # 网络传的id是字符串，要转成整型，大坑啊


@app.before_request
def before_request():
    pass

# 一定要在写完所有路由函数后 加这句话，否则会丢失路由
app.register_blueprint(auth, url_prefix='/auth')
