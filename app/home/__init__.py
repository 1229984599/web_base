from flask import Blueprint, render_template

home = Blueprint('homes', __name__)


@home.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


from app.home import index
