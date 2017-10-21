from functools import wraps
from flask import Flask, request, jsonify, render_template
from gmusicapi import Mobileclient

app = Flask(__name__)
api = Mobileclient()

def auth_required(f):
    @wraps(f)
    def decorated_func(*args, **kwargs):
        if api.is_authenticated() is False:
            err = {'error': 'Not authenticated'}
            return jsonify(err)
        return f(*args, **kwargs)
    return decorated_func

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/<path:path>', methods=['GET'])
def any_root_path(path):
    return render_template('index.html')

##########

@app.route('/api/login', methods=['POST'])
def login():
    logged_in = api.login(request.form['email'], request.form['password'], Mobileclient.FROM_MAC_ADDRESS)
    return str(logged_in)


@auth_required
@app.route('/api/songs')
def songs():
    songs = api.get_listen_now_items()
    return jsonify(songs)

@auth_required
@app.route('/api/stream/<song_id>')
def stream(song_id):
    song = api.get_stream_url(song_id)
    return jsonify(song)
