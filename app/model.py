from flask.ext.login import UserMixin
from werkzeug.security import check_password_hash

from app import DB
from app.lib.utils import Privacy


class Permission:
    QUERY = 0x01
    SUBMIT = 0x02
    EDITANALYZER = 0x12
    ADMINISTER = 0xff

class User(UserMixin, DB.Model, Privacy):
    privates = []
    __tablename__ = 'users'
    id = DB.Column(DB.Integer, primary_key = True)
    login_name = DB.Column(DB.String(128), unique = True, index = True)
    password_hash = DB.Column(DB.String(128))
    email = DB.Column(DB.String(64),unique = True,index = True)
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
