from flask import Flask
from Routes import routes

app = Flask(__name__)
app.register_blueprint(routes)

if __name__ == "__main__":
    app.debug = True
    app.run()
