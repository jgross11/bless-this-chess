import sys
sys.path.append("...")

from flask import Blueprint
from jinja2 import Environment, PackageLoader, select_autoescape
from src.obj.Utils import Map

env = Environment(
                loader=PackageLoader('bless_this_chess.general', 'templates'),
                autoescape=select_autoescape(['html', 'xml'])
            )

home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/')
def index():
    template = env.get_template('homepage.html')
    map = Map()
    map.put("testvar", 'welcome to the homepage')
    return template.render(map=map)