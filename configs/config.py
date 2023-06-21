import os

from configs import secret_key

SECRET_KEY = secret_key

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True
