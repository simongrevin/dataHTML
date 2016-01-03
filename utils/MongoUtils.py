from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.datahtml
collection = db["users"]

def saveUser(user):
    result = db.users.insert(user)
    print db.users.count()

def getAllUsers():
    return db.users.find()
