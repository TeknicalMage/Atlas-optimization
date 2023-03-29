import pymongo
from pymongo import MongoClient



cluster= MongoClient("mongodb+srv://macrollcofficial:IrytsrNRSTaQestB@macrocluster.wqpdnof.mongodb.net/?retryWrites=true&w=majority")
db = cluster ["Youtube-test"]
collection  = db["test"]


post = {"name": "jj", "score": 6}

collection.insert_one(post)

