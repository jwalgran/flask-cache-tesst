from flask import Flask
from flask import make_response

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<p>flask-cache-test</p><script src="static/app.js"></script>'


@app.route("/data")
def data():
    print("\nFETCHING DATA\n")
    respose = make_response('{"foo": "bar"}')
    respose.headers.set("Cache-Control", "max-age=10")
    return respose
