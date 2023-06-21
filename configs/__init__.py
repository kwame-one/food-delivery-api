import os

from dotenv import load_dotenv

load_dotenv('../.env')

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_host = os.getenv('DB_HOST')
db_name = os.getenv('DB_NAME')
secret_key = os.getenv('SECRET_KEY')
debug = os.getenv('APP_DEBUG')