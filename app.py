from flask import Flask
from flask_http_middleware import MiddlewareManager
from flask_jwt_extended import JWTManager

from commands.seed_command import seed_cli
from configs.database import db_session, init_db
from controllers import register_routes
from di import init_container
from exceptions import register_handlers
from middlewares import register_middlewares

app = Flask(__name__)
app.config.from_object('configs.config')
JWTManager(app)

init_db()


app.wsgi_app = MiddlewareManager(app)
app.cli.add_command(seed_cli)

register_middlewares(app)
register_handlers(app)

register_routes(app, 'v1')

init_container(app)


@app.route('/')
def index():
    return 'welcome'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
