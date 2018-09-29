import sys
import os
from flask import Flask
from importlib import import_module


workingDirectory = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, workingDirectory)

db = import_module('shared.database', f'{workingDirectory}/shared').db
Config = import_module('config', f'{workingDirectory}/config').Config
main = import_module('main.controllers', f'{workingDirectory}/main').main
api = import_module('api.controllers', f'{workingDirectory}/api').api


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(main)
app.register_blueprint(api)
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
else:
    application = app
