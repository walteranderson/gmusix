FROM kennethreitz/pipenv

COPY . /app

# -- Start the application
CMD gunicorn -b 0.0.0.0:8000 --worker-class eventlet -w 1 --access-logfile - "gmusix:create_app()"
