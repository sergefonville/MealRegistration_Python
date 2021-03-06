from shared.database import db


class Meal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    mealparts = db.relationship('MealPart')


class FoodItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False, unique=True)
    unit_id = db.Column(db.Integer, db.ForeignKey('unit.id'), nullable=False)
    carbohydrates_per_unit = db.Column(db.Integer, nullable=False)
    calories_per_unit = db.Column(db.Integer, nullable=False)
    mealparts = db.relationship('MealPart')

    @property
    def unit(self):
        return self._unit.name

    @unit.setter
    def unit(self, value):
        unit = Unit.query.filter_by(name=value).first()
        if unit is None:
            unit = Unit(name=value)
        self._unit = unit


class MealPart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meal_id = db.Column(db.Integer, db.ForeignKey('meal.id'), nullable=False)
    fooditem_id = db.Column(
        db.Integer, db.ForeignKey('food_item.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)


class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), nullable=False)
    fooditems = db.relationship('FoodItem', backref='_unit', lazy=True)
