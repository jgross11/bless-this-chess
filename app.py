from flask import Flask
import random
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "Look at this! Its a random number: " + str(random.randrange(0, 99999999999))


@app.route('/test')
def test():  # put application's code here
    return "would you look at that, a new page!"


if __name__ == '__main__':
    app.run()
