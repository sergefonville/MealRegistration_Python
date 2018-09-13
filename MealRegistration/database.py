import flask_sqlalchemy

db = None

def db_session(app):
  db =  flask_sqlalchemy.SQLAlchemy(app)
  return db

class Meal(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  timestamp = db.Column(db.DateTime)