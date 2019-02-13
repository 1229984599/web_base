from flask import Flask
from flask_mail import Mail

mail = Mail()


def create_app():
    # 实例化app
    app = Flask(__name__)
    # 读取配置文件
    app.config.from_object('config.config')

    # 检测是否开启数据库
    if app.config['DATABASE_SWITCH']:
        app.config.from_object('config.databases')
        from app.common.model.base import db
        # 挂载db对象
        db.init_app(app)
        with app.app_context():
            db.create_all()

    # 是否开启邮件功能
    if app.config['EMAIL_SWITCH']:
        app.config.from_object('config.email')
        # 挂载邮箱对象
        mail.init_app(app)

    # 注册蓝图
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.home import home
    from app.admin import admin
    app.register_blueprint(home)
    app.register_blueprint(admin)
