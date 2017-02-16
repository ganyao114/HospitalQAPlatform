from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from config import config

# global objects

LOGIN_MANAGER = LoginManager()
BOOTSTRAP = Bootstrap()
DB = SQLAlchemy()

def creat_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    BOOTSTRAP.init_app(app)
    DB.init_app(app)
    LOGIN_MANAGER.init_app(app)

    from .main import main as mian_blueprint
    app.register_blueprint(mian_blueprint)

    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    return app