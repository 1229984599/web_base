from wtforms import Form, StringField
from wtforms.validators import DataRequired, Required, Length


class DemoForm(Form):
    field1 = StringField(validators=[
        DataRequired(message='field1不能为空'), Length(2, 6, message='长度必须在2到6位')
    ])

    def validate_field1(self):
        print('field1验证函数-validate_字段名')
