import sys
import os
from flask import Flask
from shared.database import db
from config import Config
from main.controllers import main

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(main)
db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
else:
    application = app
