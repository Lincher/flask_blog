from FlaskWebProject1 import db, models, config
from migrate.versioning import api
import os.path as path

SQLALCHEMY_DATABASE_URI = config.SQLALCHEMY_DATABASE_URI
SQLALCHEMY_MIGRATE_REPO = config.SQLALCHEMY_MIGRATE_REPO

db.create_all()
admin = models.User('林川杰','lcjive@gmail.com','v595v595','admin')
db.session.add(admin)
db.session.commit()

# 数据库版本控制
if not path.exists(SQLALCHEMY_MIGRATE_REPO):
    api.create(SQLALCHEMY_MIGRATE_REPO,'database repository')
    api.version_control(SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_MIGRATE_REPO)
else:
    api.version_control(SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_MIGRATE_REPO,
    api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO))


    
