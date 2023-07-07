import os
from pathlib import Path

# /${PATH}/docker_test_main_3/flask
DB_DIR = f"{Path(__file__).resolve().parent.parent.parent}/db/sqlite"
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

