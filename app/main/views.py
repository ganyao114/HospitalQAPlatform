from app.main import main
from app.main.form import LoginForm
from config import Domain


@main.route('/')
def hello_world():
    return 'Hello World!'

@main.route(Domain.USER +  '/login', methods = ['GET', 'POST'])
def user_login():
    form = LoginForm()
    if form.validate_on_submit():
        user = ()
