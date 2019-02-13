from app import mail
from flask_mail import Message
from flask import current_app, render_template
from threading import Thread


class Email(Thread):
    """
    发送邮件类
    异步发送邮件
    """
    def __init__(self, to, subject):
        """
        :param to: 邮件接收者，字符串或列表
        :param subject: 邮件主题
        """
        Thread.__init__(self)
        self.to = self.check_recipients(to)
        self.subject = subject

    def __send_async_email(self, msg):
        app = current_app._get_current_object()
        with app.app_context():
            try:
                mail.send(msg)
            except Exception as e:
                pass
        self.start()

    @staticmethod
    def check_recipients(recipient):
        temp = []
        if isinstance(recipient, str):
            temp.append(recipient)
            return temp
        if isinstance(recipient, list):
            return recipient
        raise TypeError('接受者邮箱只能是字符串或列表')

    def send_email_text(self, body):
        """
        发送文本邮件
        :param body: 邮件内容
        :return:
        """
        msg = Message(subject=self.subject, body=body, recipients=self.to)
        self.__send_async_email(msg)

    def send_email_html(self, template, **kwargs):
        """
        发送html邮件
        :param template: html模板所在路径
        :param kwargs: 传入模板的变量
        :return:
        """
        msg = Message(subject=self.subject, recipients=self.to)
        msg.html = render_template(template, **kwargs)
        self.__send_async_email(msg)
