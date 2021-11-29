import sys
sys.path.append("...")

from flask import Blueprint, request, redirect
from jinja2 import Environment, PackageLoader, select_autoescape
from src.init.DBConnector import DBConnector
from src.obj.Utils import InformationValidator, Map

env = Environment(
                loader=PackageLoader('bless_this_chess.auth', 'templates'),
                autoescape=select_autoescape(['html', 'xml'])
            )

login_bp = Blueprint('login_bp', __name__)
signup_bp = Blueprint('signup_bp', __name__)

dbConnector : DBConnector = None
credentials = {}
informationValidator = InformationValidator()


@login_bp.route('/login', methods=['GET','POST'])
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

@signup_bp.route('/signup', methods=['GET', 'POST'])
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