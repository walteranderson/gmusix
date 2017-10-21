all: build server

server:
	FLASK_APP=gmusix.py flask run

build:
	npm run build
