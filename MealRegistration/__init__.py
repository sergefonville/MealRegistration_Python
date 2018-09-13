import os
from flask import Flask, send_from_directory
from database import db_session
applicationDirectory = os.path.dirname(__file__)
application = Flask(__name__)
db = db_session(application)

@application.route("/")
def home():
  return send_from_directory('{0}/{1}'.format(applicationDirectory,'static'), 'index.html')

@application.route('/css/<path:filename>')
def css(filename):
  return send_from_directory('{0}/{1}/{2}'.format(applicationDirectory,'static', 'css'), filename)

@application.route('/scripts/<path:filename>')
def scripts(filename):
  return send_from_directory('{0}/{1}/{2}'.format(applicationDirectory,'static', 'scripts') + '', filename)

@application.route('/templates/<path:filename>')
def templates(filename):
  return send_from_directory('{0}/{1}/{2}'.format(applicationDirectory,'static', 'templates'), filename)

if __name__ == "__main__":
  application.run()