# 
# Exemplo de acesso a uma base de dados SQLite
#
import pymongo
from pymongo import MongoClient


def manipulaMDB ():
    client = pymongo.MongoClient("mongodb://localhost:27017")
    db = client.conheca_python

    for i in range(1,10):
        obj = {'codigo': 1}
        db.conheca_mongo.insert_one(obj)
    
    db.conheca_mongo.update_one({'codigo': 2},{'$set':{'NewAtribute':789}})
    db.conheca_mongo.delete_one({'codigo': 1})

    resconsult = db.conheca_mongo.find({})
    for doc in resconsult:
        print(doc)

manipulaMDB()
