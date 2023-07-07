from settings.base import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(DB_DIR, '/sqlite/flask_dev.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xfaNt\xf5k-\xc0\x0e\xcb\xf4srb\xd2\xca3'