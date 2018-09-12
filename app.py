import os
# Change working directory so relative paths (and template lookup) work again
os.chdir(os.path.dirname(__file__))

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

@route('/')
def home():
  return static_file('index.html', root='.')
	
@route('/css/<filepath:path>')
def css(filepath):
  return static_file(filepath, root='./css')

@route('/templates/<filepath:path>')
def template(filepath):
  return static_file(filepath, root='./templates')
  
@route('/scripts/<filepath:path>')
def template(filepath):
  return static_file(filepath, root='./scripts')
  
application = default_app()