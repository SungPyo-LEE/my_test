from flask import flask

app = Flask(__file__)

@app.route('/')
def hello():
    return "Hello world"
