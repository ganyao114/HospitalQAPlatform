from app.main import main
from config import Domain


@main.route('/')
def hello_world():
    return 'Hello World!'

@main.route(Domain.USER +  '/login', methods = ['GET', 'POST'])
def user_login():
    form =
