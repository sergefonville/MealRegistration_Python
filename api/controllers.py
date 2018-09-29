from flask import Blueprint, request
from flask import jsonify
from shared.database import db
from shared.models import Meal, FoodItem, Unit

api = Blueprint('api', __name__, url_prefix='/api')


@api.route("/meal/add", methods=['POST'])
def addMeal():
    pass


@api.route("/meal/find")
def findMeal():
    q = request.args.get('q',)
    meals = Meal.query.first()
    return jsonify(meals)


@api.route("/fooditem/find")
def findFoodItem():
    q = request.args.get('q',)
    fooditem = FoodItem.query.first()
    return jsonify(fooditem)


@api.route('/fooditem/add', methods=['POST'])
def addFoodItem():
    fooditem = FoodItem()
    unit = Unit()
    unit.name = request.args.get('unit')
    fooditem.name = request.args.get('name')
    fooditem.calories_per_unit = request.args.get('calories_per_unit')
    fooditem.carbohydrates_per_unit = request.args.get(
        'carbohydrates_per_unit'
    )
    fooditem.unit = request.args.get('calories_per_unit')
