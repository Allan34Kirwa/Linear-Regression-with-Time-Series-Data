# create a client to connect to the MongoDB server
from pymongo import MongoClient
client = MongoClient(host="localhost", port=27017)
db = client["air-quality"]
nairobi = db["nairobi"]