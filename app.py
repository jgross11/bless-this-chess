from flask import Flask, request, redirect
import random

from src.init.CredentialLoader import CredentialLoader
from src.init.DBConnector import DBConnector
from src.obj.Utils import Map
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__, static_folder='./src/view/static')
dbConnector = None

credentials = {}

dbConnection = None
env = None

users = {"username" : "testusername", "password" : "testpassword"}

@app.route('/')
def hello_world():  # put application's code here
    print("navigating to home page")
    return "Look at this! Its a random number: " + str(random.randrange(0, 99999999999))

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        print("submitted login information")
        print(request.form)
        username = request.form.get("username")
        password = request.form.get("password")
        loginData = dbConnector.findUserByUsernamePassword(username, password)
        if loginData != None:
            return redirect('/') 
        else:
            template = env.get_template('login.html')
            map = Map()
            map.put("notif",'Incorrect username or password. Please try again.')
            return template.render(map=map)
    else:
        print("navigating to login page")
        template = env.get_template('login.html')
        map = Map()
        return template.render(map=map)

@app.route('/template')
def render():
    template = env.get_template('test.html')
    map = Map()
    map.put("var1", 'hello')
    map.put('var2', 'world!')
    return template.render(map=map)

@app.route('/test')
def test():  # put application's code here
    return "would you look at that, a new page!"

@app.errorhandler(404)
@app.errorhandler(405)
@app.errorhandler(500)
def pageNotFound(error):
    template = env.get_template('error.html')
    map = Map()
    map.put("error", error)
    return template.render(map=map)

if __name__ == '__main__':
    print("loading credentials...")
    credentialLoader = CredentialLoader()
    credentials = credentialLoader.loadCredentials()
    if credentials == None:
        print("No credentials = no soup for you!")
    else:
        print("successfully loaded credentials")
        print("initializing db properties")
        dbConnector = DBConnector()
        if dbConnector.init(
            credentials[credentialLoader.MYSQL_USERNAME],
            credentials[credentialLoader.MYSQL_ROOT_PASSWORD],
            credentials[credentialLoader.MYSQL_HOST],
            credentials[credentialLoader.MYSQL_DB],
        ):
            print("db test connection successful")
            print("creating Jinja2 environment")
            env = Environment(
                loader=PackageLoader('src.view', 'templates'),
                autoescape=select_autoescape(['html', 'xml'])
            )
            print("created Jinja2 environment")
            print("starting Flask")
            app.run()
        else: 
            print("db test connection failed")