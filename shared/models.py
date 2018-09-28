from shared.database import db


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime)
    foodItems = db.relationship('FoodItem')


class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('unit.id'), nullable=False)
    carbohydratesPerUnit = db.Column(db.Integer, nullable=False)
    caloriesPerUnit = db.Column(db.Integer, nullable=False)


class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
