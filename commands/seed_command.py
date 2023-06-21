from flask.cli import AppGroup
from seeders import run_seed

seed_cli = AppGroup('seed')


@seed_cli.command('db')
def seed():
    run_seed()
