from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class LoginForm(Form):

    openid = StringField('openid', validators=[DataRequired()])  # Check not empty
    remember_me = BooleanField('remember_me', default=False)