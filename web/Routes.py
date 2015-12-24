from flask import Blueprint,jsonify
import imp

beans = imp.load_package("beans","../beans")
services = imp.load_package("services","../services")

from beans.User import User
from services.IndexService import downloadLink,parseHTML

routes = Blueprint("routes",__name__)


@routes.route("/")
def default():
    user = User("arthur","arthur.grevin@gmail.com","mdp")
    user.history.append("history1")
    user.history.append("history2")
    return jsonify(user.serialize())

@routes.route("/absorber")
def linkAbsorber():
    return parseHTML("https://fr.wikipedia.org/wiki/Pharaon")
