from flask import Flask
from datetime import date

app = Flask(__name__)


@app.route('/')
def app():
    return 'hello world', 200
