from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()


def create_app():
  app = Flask(__name__)
  CORS(app)
  app.config.from_envvar('APP_CONFIG_FILE')
  
  db.init_app(app)
  migrate.init_app(app, db)
  from models import user
  from views import main_views
  app.register_blueprint(main_views.bp)
  
  return app

  # if __name__ == '__main__':
  #   app.run(host='0.0.0.0', debug=True)