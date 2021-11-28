from flask import Flask, request, redirect
import random

from src.init.CredentialLoader import CredentialLoader
from src.init.DBConnector import DBConnector
from src.obj.Utils import InformationValidator, Map
from jinja2 import Environment, PackageLoader, select_autoescape

app = Flask(__name__, static_folder='./src/view/static')
dbConnector : DBConnector = None

credentials = {}

informationValidator = InformationValidator()
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

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    map = Map()
    if request.method == 'GET':
        return env.get_template('signup.html').render(map=map)
    if request.method == 'POST':
        errorOccurred = False
        print("submitted signup information")
        print(request.form)

        ## validate form information
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        if not informationValidator.usernameIsValid(username):
            print("invalid username provided")
            map.put(informationValidator.USERNAME_ERROR_KEY, informationValidator.INVALID_USERNAME_VALUE)
            errorOccurred = True
        if not informationValidator.passwordIsValid(password):
            print("invalid password provided")
            map.put(informationValidator.PASSWORD_ERROR_KEY, informationValidator.INVALID_PASSWORD_VALUE)
            errorOccurred = True
        if not informationValidator.emailIsValid(email):
            print("invalid email provided")
            map.put(informationValidator.EMAIL_ERROR_KEY, informationValidator.INVALID_EMAIL_VALUE)
            errorOccurred = True
        if errorOccurred:
            print("invalid form data detected - not processing")
            template = env.get_template('signup.html')
            return template.render(map=map)

        ## go to db and check if information exists already
        if dbConnector.usernameTaken(username):
            print("username already in db")
            map.put(informationValidator.USERNAME_ERROR_KEY, informationValidator.USERNAME_TAKEN_VALUE)
            errorOccurred = True
        if dbConnector.emailTaken(email):
            print("email already in db")
            map.put(informationValidator.EMAIL_ERROR_KEY, informationValidator.EMAIL_TAKEN_VALUE)
            errorOccurred = True
        if errorOccurred:
            print("data already exists in db - not processing")
            template = env.get_template('signup.html')
            return template.render(map=map)

        # information good - enter into db
        # TODO salt?
        if dbConnector.insertNewUser(username, password, email):
            # TODO session?
            print("successfully inserted new user in db")
            return redirect("/")
        else:
            print("error when attempting to insert new user in db")
            map.put("signupError", "Unable to create new user. Please try again.")
            template = env.get_template('signup.html')
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
    credentials = credentialLoader.loadCredentials("config/")
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