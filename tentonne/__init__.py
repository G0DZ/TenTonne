import os

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import config

db = SQLAlchemy()
lm = LoginManager()


def create_app(config_name):
    app = Flask(__name__, static_url_path='')
    app.config.from_object(config[config_name])
    #
    db.init_app(app)
    lm.init_app(app)

    from .logic.user import user as user_blueprint
    from .logic.auth import auth as auth_blueprint
    from .logic.admin import admin as admin_blueprint

    app.register_blueprint(user_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(admin_blueprint, url_prefix='/admin')
    #app.register_blueprint(message_blueprint, url_prefix='/message')
    #app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    #with app.app_context():
        # Extensions like Flask-SQLAlchemy now know what the "current" app
        # is while within this block. Therefore, you can now run........
        #db.drop_all()
        #db.create_all()
        #Role.insert_roles()
        #Role.query.all()
    return app


app = create_app(os.getenv('CONFIG') or 'default')
from tentonne.logic import errors
# from tentonne.logic.models import Role
# with app.app_context():
#     Role.insert_roles()
#     Role.query.all()