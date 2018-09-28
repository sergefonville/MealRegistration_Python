from flask import Blueprint, render_template
from shared.database import db

main = Blueprint('main', __name__, url_prefix='', template_folder='templates')


@main.route("/")
def home():
    return render_template('index.html')


@main.route('/css/<path:filename>')
def css(filename):
    return send_from_directory(directory='', filename=filename)


@main.route('/scripts/<path:filename>')
def scripts(filename):
    return send_from_directory(directory='', filename=filename)


@main.route('/templates/<path:filename>')
def templates(filename):
    return send_from_directory(directory='', filename=filename)
