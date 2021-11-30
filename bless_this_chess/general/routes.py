import sys
sys.path.append("...")

from flask import Blueprint, request
from jinja2 import Environment, PackageLoader, select_autoescape
from src.init.DBConnector import DBConnector
from src.obj.Utils import Map

env = Environment(
                loader=PackageLoader('bless_this_chess.general', 'templates'),
                autoescape=select_autoescape(['html', 'xml'])
            )

home_bp = Blueprint('home_bp', __name__)
search_bp = Blueprint('search_bp', __name__)

dbConnector : DBConnector = None


@home_bp.route('/')
def index():
    template = env.get_template('homepage.html')
    map = Map()
    map.put("testvar", 'welcome to the homepage')
    return template.render(map=map)

@search_bp.route('/search', methods=['GET','POST'])
def search():
    if request.method == 'POST':
        print("submitting username for search")
        print(request.form)
        username = request.form.get("username")
        searchResults = dbConnector.findUserByUsername(username)
        if searchResults != None:
            template = env.get_template('search.html')
            map = Map()
            map.put("notif",'User(s) exist')
            map.put("results", searchResults)
            return template.render(map=map)
        else:
            template = env.get_template('search.html')
            map = Map()
            map.put("notif",'User does not exist.')
            return template.render(map=map)
    else:
        print("navigating to search page")
        template = env.get_template('search.html')
        map = Map()
        return template.render(map=map)