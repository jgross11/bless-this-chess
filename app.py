"""
######################################
######################################
######################################
FOR REFERENCE ONLY - EVENTUALLY DELETE
######################################
######################################
######################################
"""

from flask import Flask, jsonify

app = Flask(__name__, static_folder='./bless_this_chess/view/static')

# just keeping this endpoint so jsonification reference exists
@app.route('/resttest')
def rest_test():
    # single value
    return jsonify("data obtained from rest call!")

    # object
    # return jsonify(field1 = "value1", field2 = "value2")