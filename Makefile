all: server

server:
	FLASK_DEBUG=1 FLASK_APP=gmusix.py python gmusix.py
