from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.get('/login')
def login_get():
    return True

@app.post('/login')
def login_post():
    return True
    
@app.route("/hello")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

# parameter types are string, int, float, path, uuid
@app.route("/user/<int:id>")
def get_user(id):
    return f"Get user {id}"