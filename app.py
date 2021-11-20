from flask import Flask, request
import random

import CredentialLoader
import DBConnector
from jinja2 import Environment, PackageLoader, select_autoescape

from obj.Map import Map

app = Flask(__name__)

credentials = {}

dbConnection = None
env = None

users = {"username" : "testusername", "password" : "testpassword"}

@app.route('/')
def hello_world():  # put application's code here
    print("navigating to home page")
    return "Look at this! Its a random number: " + str(random.randrange(0, 99999999999))

@app.route('/submit-login', methods = ['POST'])
def verify_login():
    print("submitted login information")
    print(request.form)
    submittedUsername = request.form.get("username")
    submittedPassword = request.form.get("password")
    return "Login Successful" if users["username"] == submittedUsername and users["password"] == submittedPassword  else "Login failed"

@app.route('/template')
def render():
    template = env.get_template('test.html')
    map = Map()
    map.put("var1", 'hello')
    map.put('var2', 'world!')
    return template.render(map=map)

@app.route('/login')
def login():
    print("navigating to login page")
    template = env.get_template('login.html')
    return template.render()

@app.route('/test')
def test():  # put application's code here
    return "would you look at that, a new page!"

if __name__ == '__main__':
    print("loading credentials...")
    credentials = CredentialLoader.load()
    if credentials == None:
        print("No credentials = no soup for you!")
    else:
        print("successfully loaded credentials")
        DBConnector.openConnection(
            credentials[CredentialLoader.MYSQL_USERNAME],
            credentials[CredentialLoader.MYSQL_ROOT_PASSWORD],
            credentials[CredentialLoader.MYSQL_HOST],
            credentials[CredentialLoader.MYSQL_DB],
        )
        DBConnector.closeConnection()
        print("creating Jinja2 environment")
        env = Environment(
            loader=PackageLoader('app', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        print("created Jinja2 environment")
        print("starting Flask")
        app.run()