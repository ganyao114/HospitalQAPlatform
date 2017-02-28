import browsepy
from browsepy import browse, app
from flask import current_app


def showdir(path):
    return browse(path)