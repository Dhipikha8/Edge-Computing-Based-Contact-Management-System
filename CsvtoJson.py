import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['contacts']
collection_currency = db['Phone']

with open('C:/Users/Sushil/Downloads/contactsfromcsvtojson.json') as f:
    file_data = json.load(f)

collection_currency.insert_many(file_data)

client.close()