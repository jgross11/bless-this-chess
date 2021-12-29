from flask import session
from flask.templating import render_template
from bless_this_chess.Utils import Map, create_blueprint

error_bp = create_blueprint('error_bp', __name__)

@error_bp.app_errorhandler(404)
@error_bp.app_errorhandler(405)
@error_bp.app_errorhandler(500)
def pageNotFound(error):
    map = Map()
    map.put("error", error)
    # if user is logged in
    userlogged = session.get('userlogged')
    if userlogged:
        map.put('userlogged', str(userlogged))
    return render_template('error.jinja2', map=map)