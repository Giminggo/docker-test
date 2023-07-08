import os, json
from pathlib import Path

# /${PATH}/docker_test_main_3/flask
SQLITE_DB_DIR = f'{Path(__file__).resolve().parent.parent}/sqlite'
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_FILE = os.path.join(BASE_DIR, 'secrets.json')

with open(SECRET_FILE) as f:
  secrets = json.loads(f.read())

def get_secret(setting, secrets=secrets):
    """Get SECRET_KEY Value or Error"""
    try:
        return secrets[setting]
    except KeyError:
        error_msg = f"Set the {setting} environment variable."
        raise error_msg