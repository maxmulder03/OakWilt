import flask 
from flask_cors import CORS

app = flask.Flask(__name__)

app.config.from_object("backend.config")

app.config.from_envvar("OAKWILT_SETTINGS", silent=True)

CORS(app)
