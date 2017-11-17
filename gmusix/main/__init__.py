from flask import Blueprint

main = Blueprint('main', __name__)

from . import events

@main.route('/')
def index():
    """ example route just so something shows up on the screen """
    return 'hello world'
