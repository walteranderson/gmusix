from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app():
    """
    Create flask app using the factory pattern

    :return: Flask app
    """
    app = Flask(__name__)

    app.config.from_object('config.settings')

    from .main import main
    app.register_blueprint(main)

    socketio.init_app(app)

    return app
