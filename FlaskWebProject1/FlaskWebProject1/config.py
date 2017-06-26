import os

# sqlalchemy 配置
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.join(basedir,'tmp'), 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir,'db_repository')

# flask-wtf(form) 配置
CSRF_ENABLED = True
SECRET_KEY = 'fuck-u-'