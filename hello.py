from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

@app.route("/user/<int:id>")
def getUser(id):
    return f"Get user {id}"