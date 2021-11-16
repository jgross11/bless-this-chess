from flask import Flask
import random

import CredentialLoader
import DBConnector

app = Flask(__name__)

credentials = {}

dbConnection = None

@app.route('/')
def hello_world():  # put application's code here
    return "Look at this! Its a random number: " + str(random.randrange(0, 99999999999))


@app.route('/test')
def test():  # put application's code here
    return "would you look at that, a new page!"

if __name__ == '__main__':
    credentials = CredentialLoader.load()
    DBConnector.openConnection(
        credentials[CredentialLoader.MYSQL_USERNAME],
        credentials[CredentialLoader.MYSQL_ROOT_PASSWORD],
        credentials[CredentialLoader.MYSQL_HOST],
        credentials[CredentialLoader.MYSQL_DB],
    )
    DBConnector.closeConnection()
    app.run()