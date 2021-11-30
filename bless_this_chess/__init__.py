from flask import Flask
from bless_this_chess.DBConnector import DBConnector
from bless_this_chess.CredentialLoader import CredentialLoader
from bless_this_chess.Utils import *

dbConnector = DBConnector()
credentials = {}
credentialLoader = CredentialLoader()
informationValidator = InformationValidator()

def init_app():
    print("loading credentials")
    # , static_folder='./bless_this_chess/view/static'
    app = Flask(__name__, static_folder='./view/static')
    credentials = credentialLoader.loadCredentials("config/")
    if credentials == None:
        print("No credentials = no soup for you!")
    else:
        print("successfully loaded credentials")
        print("initializing db properties")
        if dbConnector.init(
            credentials[credentialLoader.MYSQL_USERNAME],
            credentials[credentialLoader.MYSQL_ROOT_PASSWORD],
            credentials[credentialLoader.MYSQL_HOST],
            credentials[credentialLoader.MYSQL_DB],
        ):
            print("db test connection successful")
            print("creating app context")
            # TODO there should be a nicer way to do this part...
            with app.app_context():
                from .routes.home import routes as home
                from .routes.errors import routes as error
                from .routes.user import routes as user

                app.register_blueprint(home.home_bp)
                app.register_blueprint(error.error_bp)
                app.register_blueprint(user.user_bp)

                print("app context successfully created")
                return app
        else: 
            print("db test connection failed")
    