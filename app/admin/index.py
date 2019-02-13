from . import admin


@admin.route('/')
def admin_index():
    return 'admin/index'

@admin.route('/test')
def admin_test():
    return 'admin/test'