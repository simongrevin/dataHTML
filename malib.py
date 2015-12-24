from flask import Blueprint


appURLs = Blueprint('appURLs',__name__)

@appURLs.route('/')
def hello():
    return "Coucou Arthur!"

@appURLs.route("/truc")
def truc():
    return "coucou"

@appURLs.route("/thebest")
def thebest():
    return "Coucou Louise!"
