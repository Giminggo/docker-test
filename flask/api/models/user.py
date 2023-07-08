from api.main import db

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(200), nullable=False)
  age = db.Column(db.String(200), nullable=False)
  information = db.Column(db.Text(), nullable=False)
  