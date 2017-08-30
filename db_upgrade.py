from migrate.versioning import api
from FlaskWebProject1.config import SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
print('Current database version:%s'%str(
    api.db_version(
        SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_MIGRATE_REPO)))
