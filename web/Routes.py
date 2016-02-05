from flask import Blueprint,jsonify

import imp

#beans = imp.load_package("beans","../beans")
services = imp.load_package("services","../services")
#dao = imp.load_package("dao","../dao")

#from dao.UserDAO import registerUser
#from beans.User import User
#from services.IndexService import downloadLink,parseHTML, tokenize
#from dao.UserDAO import registerUser, displayUsers
routes = Blueprint("routes",__name__)


@routes.route("/")
def default():
    return "test"

@routes.route("/absorber")
def linkAbsorber():
    return "test2"

@routes.route("/register/<string:json>",methods=['POST','PUT'])
def register():
    #user = request.get_json(force=True)
    #user = User(user['login'],user['email'],user['password'])
    #registerUser(user)
    return "test"

@routes.route("/test2")
def test2():
    #displayUsers()
    return "test2"

@routes.route("/tokenize")
def tokenizeText():
    #return tokenize("http://www.theverge.com/2015/12/10/9880594/microsoft-xbox-games-2016-interview-crackdown-3-quantum-break-recore")
    return "aa"