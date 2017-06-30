import os

# sqlalchemy 配置
basedir = os.path.abspath(os.path.dirname(__file__))
# 数据库地址
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.join(basedir,'tmp'), 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 数据库管理仓库地址
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')

# flask-wtf(form) 配置
# 跨域保护
CSRF_ENABLED = True
SECRET_KEY = 'fuck-u-'
# 上传文件的地址
# /开头的为 绝对地址
UPLOAD_FOLDER = 'static/favicon'
# 允许上传文件的类型
ALLOWED_EXTENSIONS = set(['png','jpg','jpeg','gif'])
# 上传文件大小限制
MAX_CONTENT_LENGTH = 2*1024*1024