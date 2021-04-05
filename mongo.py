import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "myfirstDB"
COLLECTION = "customer"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)


coll = conn[DATABASE][COLLECTION]


new_doc = {"first": "david", "last": "Njogu", "dob": "18/03/1987",
           "hair_color": "brown", "occupation": "singer", "nationality": "italian"}

coll.insert(new_doc)


documents = conn.find()

for doc in documents:
    print(doc)
