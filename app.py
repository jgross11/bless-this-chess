from flask import Flask
import random
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return "Look at this! Its a random number: " + str(random.randrange(0, 99999999999, 3))


if __name__ == '__main__':
    app.run()
