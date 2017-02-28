from flask.ext.login import login_user

from app.filebrowser.explorer import showdir
from app.main import main
from app.main.form import LoginForm
from app.model import User
from config import Domain


@main.route('/')
def hello_world():
    return 'Hello World!'

@main.route(Domain.USER +  '/login', methods = ['GET', 'POST'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(name = form.username).first();
        if user is not None and user.verify_password():
            login_user(user, form.remember_me.data)
            pass

@main.route(Domain.USER +  '/show', methods = ['GET', 'POST'])
def show():
    return showdir('Android')

