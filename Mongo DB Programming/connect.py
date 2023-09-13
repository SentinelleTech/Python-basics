import pymongo
from pymongo import MongoClient

client = MongoClient(host="127.0.0.1", port=27017)

db = client.test

db = pymongo.database.Database(client, 'test')