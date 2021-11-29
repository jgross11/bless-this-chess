import sys
sys.path.append("...")

from flask import Blueprint
from jinja2 import Environment, PackageLoader, select_autoescape
from src.obj.Utils import Map

env = Environment(
                loader=PackageLoader('chess.sample', 'templates'),
                autoescape=select_autoescape(['html', 'xml'])
            )

sample_bp = Blueprint('sample_bp', __name__)

@sample_bp.route('/blueprinttest')
def index():
    template = env.get_template('sample.html')
    map = Map()
    map.put("testvar", 'blueprint jinja testing')
    return template.render(map=map)