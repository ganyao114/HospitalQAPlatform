from flask import Blueprint

codeview = Blueprint('codeview', __name__)

from . import views