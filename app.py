import flask

app = flask.Flask(__name__)

@app.route('/')
def index():
    return "this is index page"

app.run()
# print(__name__)