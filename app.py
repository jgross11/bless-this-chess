"""
######################################
######################################
######################################
FOR REFERENCE ONLY - EVENTUALLY DELETE
######################################
######################################
######################################
"""

from flask import Flask, request, redirect, jsonify
import random

from src.init.CredentialLoader import CredentialLoader
from src.init.DBConnector import DBConnector
from src.obj.Utils import InformationValidator, Map
from jinja2 import Environment, PackageLoader, select_autoescape

from bless_this_chess.general.routes import home_bp, search_bp
from bless_this_chess.sample.routes import sample_bp
from bless_this_chess.auth.routes import login_bp, signup_bp
from bless_this_chess.errors.routes import error_bp

app = Flask(__name__, static_folder='./bless_this_chess/view/static')
app.register_blueprint(home_bp)
app.register_blueprint(search_bp)
app.register_blueprint(sample_bp)
app.register_blueprint(login_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(error_bp)

dbConnector : DBConnector = None

credentials = {}

informationValidator = InformationValidator()
env = None

users = {"username" : "testusername", "password" : "testpassword"}

@app.route('/resttest')
def rest_test():
    return jsonify("data obtained from rest call!")

@app.route('/loggedin')
def logged_in():
    map = Map()
    template = env.get_template("loggedin.html")
    return template.render(map=map)