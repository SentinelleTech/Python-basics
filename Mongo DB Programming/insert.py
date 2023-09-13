import pymongo
from pymongo import MongoClient

client = MongoClient(host="127.0.0.1", port=27017)

db = client.sample_mflix

add_movie = {
                "title": "The Devil's conspiracy",
                "genres": [ "Action", "Thriller" ],
                "runtime": 90,
                "rated": "R",
                "year": 2023,
                "directors": [ "Maurice" ],
                "cast": [ "Olivia O", "Emma S", "Rachel W" ],
                "type": "movie"
            }

#tutorial = db.movies

tutorial = pymongo.collection.Collection(pymongo.database.Database(client, 'sample_mflix'), "sample_mflix")

result = tutorial.insert_one(add_movie)

print("Success : {result.insertedId}")

client.close()