import json
import pymongo

from pymongo import MongoClient
client = MongoClient()

db=client.contacts
collection=db.Phone
page=open("C:/Users/Sushil/Downloads/contactsfromcsvtojson.json",'r')
dataset=json.loads(page.read())
 
for item in dataset:
 collection.insert(item)
 
for item in collection.find():
 print(item)
print("\n")


