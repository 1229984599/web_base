from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404


from app.admin import index
