from flask import Flask
import random

import CredentialLoader
import DBConnector
from jinja2 import Environment, PackageLoader, select_autoescape

from obj.Map import Map

app = Flask(__name__)

credentials = {}

dbConnection = None
env = None

@app.route('/')
def hello_world():  # put application's code here
    return "Look at this! Its a random number: " + str(random.randrange(0, 99999999999))

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

if __name__ == '__main__':

    credentials = CredentialLoader.load()
    if credentials == None:
        print("No credentials = no soup for you!")
    else:
        DBConnector.openConnection(
            credentials[CredentialLoader.MYSQL_USERNAME],
            credentials[CredentialLoader.MYSQL_ROOT_PASSWORD],
            credentials[CredentialLoader.MYSQL_HOST],
            credentials[CredentialLoader.MYSQL_DB],
        )
        DBConnector.closeConnection()
        env = Environment(
            loader=PackageLoader('app', 'templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        app.run()