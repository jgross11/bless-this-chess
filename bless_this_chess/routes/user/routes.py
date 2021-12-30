from flask import request, session, redirect, url_for, render_template
from bless_this_chess.DBConnector import DBConnector
from bless_this_chess.Utils import InformationValidator
from bless_this_chess.Utils import Map, create_blueprint


user_bp = create_blueprint('user_bp', __name__)
# this will eventually be a subclass that only contains the relevant DB ops
dbConnector = DBConnector()

informationValidator = InformationValidator()

@user_bp.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        print("submitted login information")
        print(request.form)
        username = request.form.get("username")
        password = request.form.get("password")
        loginData = dbConnector.findUserByUsernamePassword(username, password)
        if loginData != None:
            session['userlogged'] = username
            return redirect(url_for('home_bp.home')) 
        else:
            map = Map()
            map.put("invalidauth",'Incorrect username or password. Please try again.')
            return render_template('login.jinja2', map=map)
    else:
        print("navigating to login page")
        return render_template('login.jinja2', map=Map())

@user_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect(url_for('user_bp.login'))

@user_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    map = Map()
    if request.method == 'GET':
        return render_template('signup.jinja2', map=map)
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
            return render_template('signup.jinja2', map=map)

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
            return render_template('signup.jinja2', map=map)

        # information good - enter into db
        # TODO salt?
        if dbConnector.insertNewUser(username, password, email):
            print("successfully inserted new user in db")
            session['userlogged'] = username
            return redirect(url_for('home_bp.home'))
        else:
            print("error when attempting to insert new user in db")
            map.put("signupError", "Unable to create new user. Please try again.")
            return render_template('signup.jinja2', map=map)

@user_bp.route('/profile')
def profile():
    map = Map()
    #map.put('notif', 'This is a notification')
    return render_template('profile.jinja2', map=map)