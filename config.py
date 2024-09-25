import os

from dotenv import load_dotenv
env_vars_to_clear = ['DB_NAME', 'DB_USER', 'DB_PASS', 'DB_HOST', 'DB_PORT', 'SECRET_AUTH']

for var in env_vars_to_clear:
    os.environ.pop(var, None)

load_dotenv()

DB_HOST = os.environ.get("DB_HOST")
DB_PORT = os.environ.get("DB_PORT")
DB_NAME = os.environ.get("DB_NAME")
DB_USER = os.environ.get("DB_USER")
DB_PASS = os.environ.get("DB_PASS")
ELASTIC_PASSWORD = os.environ.get("ELASTIC_PASSWORD")
ELASTIC_HOST = os.environ.get("ELASTIC_HOST")
