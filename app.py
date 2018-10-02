import sys
import os
from flask import Flask
from importlib import import_module


workingDirectory = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, workingDirectory)
sharedPackage = f'{workingDirectory}/shared'
configPackage = f'{workingDirectory}/config'
mainPackage = f'{workingDirectory}/main'
apiPackage = f'{workingDirectory}/api'

db = import_module('shared', package=sharedPackage).db
Config = import_module('config', package=configPackage).Config
main = import_module('main', package=mainPackage).main
api = import_module('api', package=apiPackage).api


app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(main)
app.register_blueprint(api)
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
else:
    application = app
