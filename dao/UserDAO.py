import imp
beans = imp.load_package("beans","../beans")
utils = imp.load_package("utils","../utils")
from beans.User import User
from flask import jsonify
from utils.MongoUtils import saveUser, getAllUsers

def registerUser(user):
    #json = jsonify(user.serialize())
    saveUser(user.serialize())

def displayUsers():
    users = getAllUsers()
    listUser = []
    for user in users:
        u = User.fromdict(user)
        listUser.append(u)

    print listUser
    return listUser
