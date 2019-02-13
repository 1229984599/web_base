from . import home
from flask import current_app, request


@home.route('/')
def index():
    from app.home.form.user import DemoForm
    form = DemoForm(request.args)

    return current_app.config['SECRET_KEY']


@home.route('/email')
def email():
    from app.common.mail import Email
    emails = Email('768091671@qq.com', '异步邮件')
    # emails.send_email_text('测试文本内容')
    emails.send_email_html()
    emails.send_email_html('email.html', content='我是html内容')
    # send_email('768091671@qq.com', '标题测试', 'email.html', content='我是内容')
    return '邮件发送成功'
