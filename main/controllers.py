from flask import Blueprint, render_template, send_from_directory, send_file
from shared.database import db

main = Blueprint(
    'main',
    __name__,
    url_prefix='',
    template_folder='templates',
    static_folder='static'
)


@main.route("/")
def home():
    return send_from_directory(
        directory=f'{main.static_folder}/views',
        filename='index.html'
    )


@main.route('/css/<path:filename>')
def css(filename):
    return send_from_directory(
        directory=f'{main.static_folder}/css',
        filename=filename
    )


@main.route('/scripts/<path:filename>')
def scripts(filename):
    return send_from_directory(
        directory=f'{main.static_folder}/scripts',
        filename=filename
    )


@main.route('/views/<path:filename>')
def views(filename):
    return send_from_directory(
        directory=f'{main.static_folder}/views',
        filename=filename
    )
