# import ptvsd
# ptvsd.settrace("secret",address = ('0.0.0.0', 3000))
# import os
# os.system("pause")
import imp
from migrate.versioning import api
from FlaskWebProject1 import db
from FlaskWebProject1.config import (SQLALCHEMY_DATABASE_URI,
                                     SQLALCHEMY_MIGRATE_REPO)
import os.path as path

# 迁移脚本
migration = path.join(SQLALCHEMY_MIGRATE_REPO,
                      path.join(
                          'versions',
                          '%03d_migration.py' % (api.db_version(
                              SQLALCHEMY_DATABASE_URI,
                              SQLALCHEMY_MIGRATE_REPO)
                              + 1)
                      ))


tmp_module = imp.new_module('old_model')
# 通过数据库文件 反推出对象模型
old_model = api.create_model(SQLALCHEMY_DATABASE_URI,
                             SQLALCHEMY_MIGRATE_REPO)
# 执行old_model中的语句在 tmp_module的作用域中，这样就不会污染全局环境
exec(old_model, tmp_module.__dict__)
script = api.make_update_script_for_model(
    SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_MIGRATE_REPO,
    tmp_module.meta,  # 旧数据库的元数据
    db.metadata   # 新数据库的元数据
)



# 为了保证迁移成功，一定不要重命名字段

open(migration, 'w').write(script)
# 迁移的时候已经升级了
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print("New migration saved as %s" % migration)
print('Current database version: %s' % str(api.db_version(
    SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)))
