from flask import Blueprint
from shared.database import db

api = Blueprint('api', __name__, url_prefix='/api')