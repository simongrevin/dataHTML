from flask import Flask
from malib import appURLs

newspars = Flask(__name__)
newspars.register_blueprint(appURLs)

if __name__ == "__main__":
    newspars.debug = True
    newspars.run()
