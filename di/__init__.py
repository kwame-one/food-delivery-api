from flask_injector import FlaskInjector

from .modules.role_module import RoleModule
from .modules.user_module import UserModule


def init_container(app):
    FlaskInjector(app=app, modules=[UserModule, RoleModule])
