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
        return username and username.strip()
    
    def passwordIsValid(self, pwd : str):
        # TODO password should be encrypted to standard format
        return pwd and pwd.strip()

    def emailIsValid(self, email : str):
        # TODO email should be in some standard format
        return email and email.strip()