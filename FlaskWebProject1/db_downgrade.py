from migrate.versioning import api
from FlaskWebProject1.config import (SQLALCHEMY_DATABASE_URI,
SQLALCHEMY_MIGRATE_REPO)
v = api.db_version(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)
# import IPython;IPython.embed()
api.downgrade(SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO,v-1)
print('Current database version : %s'%str(api.db_version(
    SQLALCHEMY_DATABASE_URI,SQLALCHEMY_MIGRATE_REPO)))
    