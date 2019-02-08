import pymongo
import env
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "mytestdb"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e

#calling the mongo_connect function in order to connect to the database        
conn = mongo_connect(MONGODB_URI)

#pass the connection name to a variable
coll = conn[DBS_NAME][COLLECTION_NAME]

#first argument is a search string, the second one sets the value of the searched string
#update_one changes just one record, update_many changes multiple records
coll.update_many({'nationality': 'american'}, {'$set': {'hair_colour': 'maroon'}})

documents = coll.find({'nationality': 'american'})

for doc in documents:
    print(doc)
    
