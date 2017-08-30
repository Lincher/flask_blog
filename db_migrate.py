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
#  __dict__ 类的属性
exec(old_model, tmp_module.__dict__)
# import ipdb;ipdb.set_trace()
script = api.make_update_script_for_model(
    SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_MIGRATE_REPO,
    tmp_module.meta,  # 旧数据库的元数据
    db.metadata   # 新数据库的元数据
)
# 为了保证迁移成功，一定不要重命名字段

# python 3中只有unicode str，所以把decode方法去掉了。你的代码
# 中，f1已经是unicode str了，不用decode。

# 如果文件内容不是unicode编码的，要先以二进制方式打开，读入比特流，再解码。
# import ipdb;ipdb.set_trace()
s = script.encode('utf-8')
open(migration, 'wb').write(s)
# script = open(migration, 'rb').read()
# open(migration, 'w').write(script.decode('gbk').encode
# ('utf-8'))


# 迁移的时候已经升级了
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print("New migration saved as %s" % migration)
print('Current database version: %s' % str(api.db_version(
    SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)))
