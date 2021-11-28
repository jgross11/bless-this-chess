from flask import Blueprint

sample_bp = Blueprint('sample_bp', __name__)

@sample_bp.route('/blueprinttest')
def index():
    return "blueprint test"