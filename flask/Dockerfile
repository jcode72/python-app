from python:3.7.2-stretch

workdir /app

add . /app

run pip install -r requirements.txt

cmd ["uwsgi", "app.ini"]
