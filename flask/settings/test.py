from settings.base import *

SQLALCHEMY_DATABASE_URI = f'postgresql://{get_secret("POSTGRES_USER")}:{get_secret("POSTGRES_PASSWORD")}@localhost:5432/antoliny'
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xfaNt\xf5k-\xc0\x0e\xcb\xf4srb\xd2\xca3'