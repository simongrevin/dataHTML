from flask import Flask
from Routes import routes
import imp
utils = imp.load_package("utils","../utils")
# Flask app
app = Flask("DataHTLM")
print "Starting Up DataHTLM"

print "Starting Up MongoDB"
# routes
app.register_blueprint(routes)

# run the app
if __name__ == "__main__":
    app.debug = True
    app.run()
