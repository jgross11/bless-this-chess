from flask.blueprints import Blueprint
import re

class Map:
    def __init__(self):
        self.internalMap = {}

    def put(self, key, value):
        self.internalMap[key] = value
    
    def get(self, key):
        return self.internalMap[key]

    def containsKey(self, key):
        return key in self.internalMap
    
class InformationValidator:
    USERNAME_ERROR_KEY = "usernameError"
    INVALID_USERNAME_VALUE = "Please provide a valid username."
    USERNAME_TAKEN_VALUE = "An account with this username already exists."
    PASSWORD_ERROR_KEY = "passwordError"
    INVALID_PASSWORD_VALUE = "Please provide a valid password. Valid passwords are [criteria]."
    EMAIL_ERROR_KEY = "emailError"
    INVALID_EMAIL_VALUE = "Please provide a valid email."
    EMAIL_TAKEN_VALUE = "An account with this email already exists."
    def __init__(self):
        pass
    
    def usernameIsValid(self, username : str):
        return username and username.strip() and len(username) > 0 and len(username) < 65
    
    def passwordIsValid(self, pwd : str):
        # TODO password should be encrypted to standard format
        return pwd and pwd.strip()

    def emailIsValid(self, email : str):
        # (.+) -> at least one character
        # regex 'reads': at least one character, an @, at least one character, a ., at least one character
        # not perfect, but good enough for our purposes
        return email and email.strip() and len(email) > 5 and len(email) < 65 and re.match("(.+)@(.+)[.](.+)", email)

def create_blueprint(blueprintName : str, relativeRoot : str):
    blueprint = Blueprint(
        blueprintName, relativeRoot,
        template_folder='templates',
        static_folder='static'
    )
    return blueprint