from flask import Flask
from Routes import routes
from flask.ext.pymongo import PyMongo

app = Flask(__name__)
mongo = PyMongo(app)
app.register_blueprint(routes)

if __name__ == "__main__":
    app.debug = True
    app.run()
