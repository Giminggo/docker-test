from settings.base import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(DB_DIR, 'flask_dev.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "dev"
