from flask.ext.wtf import Form
from wtforms import StringField


class LoginForm(Form):
    username = StringField('Email')
