from flask import Flask
from flask_http_middleware import MiddlewareManager

from commands.seed_command import seed_cli
from configs.database import db_session, init_db
from di import init_container


app = Flask(__name__)
app.config.from_object('configs.config')

init_db()


app.wsgi_app = MiddlewareManager(app)
app.cli.add_command(seed_cli)

init_container(app)


@app.route('/')
def index():
    return 'welcome'


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


if __name__ == '__main__':
    app.run()
