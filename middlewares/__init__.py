from flask_http_middleware import MiddlewareManager


def register_middlewares(app):
    app.wsgi_app = MiddlewareManager(app)