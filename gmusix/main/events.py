from flask_socketio import send
from .. import socketio

@socketio.on('message')
def message(msg):
    """ example event, just bounces message back down to client """
    send(msg)
