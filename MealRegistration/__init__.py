import os
from flask import Flask, send_from_directory
applicationDirectory = os.path.dirname(__file__)
app = Flask(__name__)

@app.route("/")
def home():
    return send_from_directory(applicationDirectory, 'index.html')

@app.route('/css/<path:filename>')
def css(filename):
  return send_from_directory(applicationDirectory + '/static/css', filename)

@app.route('/scripts/<path:filename>')
def scripts(filename):
  return send_from_directory(applicationDirectory + '/static/scripts', filename)

@app.route('/templates/<path:filename>')
def templates(filename):
  return send_from_directory(applicationDirectory + '/static/templates', filename)

if __name__ == "__main__":
    app.run()