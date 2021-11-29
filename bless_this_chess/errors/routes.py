import sys
sys.path.append("...")

from flask import Blueprint
from jinja2 import Environment, PackageLoader, select_autoescape
from src.obj.Utils import Map

env = Environment(
                loader=PackageLoader('bless_this_chess.errors', 'templates'),
                autoescape=select_autoescape(['html', 'xml'])
            )

error_bp = Blueprint('error_bp', __name__)

@error_bp.app_errorhandler(404)
@error_bp.app_errorhandler(405)
@error_bp.app_errorhandler(500)
def pageNotFound(error):
    template = env.get_template('error.html')
    map = Map()
    map.put("error", error)
    return template.render(map=map)