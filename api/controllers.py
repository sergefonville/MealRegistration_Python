from flask import Blueprint, request
from flask import jsonify
from shared.database import db
from shared.models import Meal, FoodItem, Unit

blueprint = Blueprint('api', __name__, url_prefix='/api')


@blueprint.route("/meal/add", methods=['PUT'])
def addMeal():
    pass


@blueprint.route("/meal/update", methods=['POST'])
def updateMeal():
    pass


@blueprint.route("/meal/search")
def searchMeal():
    q = request.args.get('q', )
    meals = Meal.query.first()
    return jsonify(meals)


@blueprint.route("/fooditem/search")
def searchFoodItem():
    q = request.args.get('q', '')
    fooditem = FoodItem.query.filter_byfirst()
    return jsonify(fooditem)


@blueprint.route('/fooditem/add', methods=['PUT'])
def addFoodItem():
    fooditem = FoodItem()
    unit = Unit.query(Unit.name).filter_by(
        Unit.name.like(f"%{request.args.get('unit')}%")).scalar()
    if unit is None:
        unit = Unit()
        unit.name = request.args.get('unit')
        db.session.add(unit)
        db.session.commit()
    unit.name = request.args.get('unit')
    fooditem.name = request.args.get('name')
    fooditem.calories_per_unit = request.args.get('calories_per_unit')
    fooditem.carbohydrates_per_unit = request.args.get(
        'carbohydrates_per_unit')
    fooditem.unit = unit


@blueprint.route('/fooditem/update', methods=['POST'])
def updateFoodItem():
    pass
