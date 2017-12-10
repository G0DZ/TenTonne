#!/usr/bin/env python
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from tentonne import app, db
from tentonne.logic.models import User, Permission

manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Permission=Permission)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


# # 部署命令
# @manager.command
# def deploy():
#     from flask_migrate import upgrade
#     from tentonne.models import Role
#     # 迁移数据库到最新修订版本
#     upgrade()
#     # 创建用户角色
#     Role.insert_roles()


if __name__ == '__main__':
    manager.run()