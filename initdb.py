from app import app, db

db.drop_all(app=app)
db.create_all(app=app)
