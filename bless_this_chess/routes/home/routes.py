from flask import request, redirect, url_for
from flask.templating import render_template
from bless_this_chess.DBConnector import DBConnector
from bless_this_chess.Utils import InformationValidator, Map, create_blueprint

home_bp = create_blueprint('home_bp', __name__)
# this will eventually be a subclass that only contains the relevant DB ops
dbConnector = DBConnector()

@home_bp.route('/')
def home():
    print("navigating to home page")
    map = Map()
    map.put('testvar', 'test value')
    return render_template('home.html', map=map)

@home_bp.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        print("submitting username for search")
        print(request.form)
        username = request.form.get("username")
        searchResults = dbConnector.findUserByUsername(username)
        if searchResults != None:
            map = Map()
            map.put("notif",'User(s) exist')
            map.put("results", searchResults)
            return render_template('search.html', map=map)
        else:
            map = Map()
            map.put("notif",'User does not exist.')
            return render_template('search.html', map=map)
    else:
        print("navigating to search page")
        return render_template('search.html', map=Map())