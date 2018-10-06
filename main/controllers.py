from flask import Blueprint, render_template, send_from_directory, send_file
from shared.database import db

blueprint = Blueprint(
    'main',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static')


@blueprint.route("/")
def home():
    return send_from_directory(
        directory=f'{main.static_folder}/views', filename='index.html')


@blueprint.route('/css/<path:filename>')
def css(filename):
    return send_from_directory(
        directory=f'{main.static_folder}/css', filename=filename)


@blueprint.route('/scripts/<path:filename>')
def scripts(filename):
    return send_from_directory(
        directory=f'{main.static_folder}/scripts', filename=filename)


@blueprint.route('/views/<path:filename>')
def views(filename):
    return send_from_directory(
        directory=f'{main.static_folder}/views', filename=filename)
