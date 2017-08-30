from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
migration_tmp = Table('migration_tmp', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('username', VARCHAR(length=80)),
    Column('email', VARCHAR(length=120)),
    Column('password', VARCHAR(length=12)),
    Column('permission', VARCHAR(length=12)),
    Column('gander', BOOLEAN),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('username', String(length=80)),
    Column('email', String(length=120)),
    Column('password', String(length=12)),
    Column('permission', String(length=12), default=ColumnDefault('guest')),
    Column('gander', Boolean),
    Column('birthdate', DateTime),
    Column('introduction', Text, default=ColumnDefault('这个人很懒，没有任何说明')),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].drop()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['migration_tmp'].create()
    post_meta.tables['user'].drop()
