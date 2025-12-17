from pymongo import MongoClient
import os

MONGO_HOST = os.environ.get("MONGO_HOST", "localhost")
MONGO_PORT = int(os.environ.get("MONGO_PORT", 27017))

client = MongoClient(MONGO_HOST, MONGO_PORT)
db = client["wine_cellar"]
wines_collection = db["wines"]
