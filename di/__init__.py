from flask_injector import FlaskInjector


def init_container(app):
    FlaskInjector(app=app, modules=[])
