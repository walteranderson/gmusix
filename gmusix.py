from functools import wraps
from flask import Flask, request, jsonify, render_template
from gmusicapi import Mobileclient
from flask_socketio import SocketIO, send, emit

app = Flask(__name__)
socketio = SocketIO(app)

api = Mobileclient()

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    return render_template('index.html')


#############
# WebSockets
#############

@socketio.on('message')
def handle_message(message):
    """ example of receiving/sending websocket messages """
    send(message)

@socketio.on('auth:login')
def login(form):
    logged_in = api.login(form['email'], form['password'], Mobileclient.FROM_MAC_ADDRESS)
    emit('auth:result', logged_in)

@socketio.on('auth:check')
def auth_check():
    emit('auth:result', api.is_authenticated())

@socketio.on('stream_url:request')
def stream_url(song_id):
    song = api.get_stream_url(song_id)
    emit('stream_url:received', song)


#############
# API
#############

def auth(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if api.is_authenticated() is False:
            err = {'error': 'Not authenticated'}
            return jsonify(err)
        return f(*args, **kwargs)
    return decorated_func

@app.route('/api/login', methods=['POST'])
def login():
    logged_in = api.login(request.form['email'], request.form['password'], Mobileclient.FROM_MAC_ADDRESS)
    return str(logged_in)

@auth
@app.route('/api/songs')
def songs():
    songs = api.get_all_songs()
    return jsonify(songs)

@auth
@app.route('/api/stream/<song_id>')
def stream(song_id):
    song = api.get_stream_url(song_id)
    return jsonify(song)

if __name__ == '__main__':
    socketio.run(app)
