from flask import Flask
#this is on branch dev

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "hello,world!"

#how to start the service
#export FLASK_APP=flaskr
#export FLASK_ENV=development
#flask run