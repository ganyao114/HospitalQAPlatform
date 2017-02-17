from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required


class LoginForm(Form):
    username = StringField('LoginName', validators=[Required()])
    password = PasswordField('Pass', validators = [Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log in')