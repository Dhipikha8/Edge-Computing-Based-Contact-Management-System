import json
import pymongo

from bson import json_util 
from pymongo import MongoClient
client = MongoClient()

db=client.contacts
collection=db.Phone
df=db.Phone.find({},{"_id":0})
for x in df:
    json.dump(json_util.dumps(df),open("C:/Users/Sushil/Downloads/MongoDBtojson.json", "w"))
#with open('C:/Users/Sushil/Downloads/MongoDBtojson.json', 'w') as outfile:
    #outfile.write(json.dumps(df, indent=4))
