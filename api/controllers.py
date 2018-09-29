from flask import Blueprint
from shared.database import db

api = Blueprint('api', __name__, url_prefix='/api')


@api.route("/meal/add", methods=['POST'])
def addMeal():
    pass


@api.route("/meal/find")
def findMeal():
    pass


@api.route("/fooditem/find")
def findFoodItem():
    pass

