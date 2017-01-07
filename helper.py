# -*- coding:utf-8 -*-

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from message_box import app, db, models

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


def init_db():
    db.create_all()


if __name__ == '__main__':
    manager.run()
