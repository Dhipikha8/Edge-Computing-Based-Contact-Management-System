import json
import csv

with open('C:/Users/Sushil/Downloads/MongoDBtojson.json', 'r') as jsonfile:
  data=jsonfile.read()

jsonobj = json.loads(data)

keylist = []
for key in jsonobj[0]:
  keylist.append(key)

f = csv.writer(open("test.csv", "w"))
f.writerow(keylist)

for record in jsonobj:
    currentrecord = []

for key in keylist:
  currentrecord.append(record[key])

f.writerow(currentrecord)

def jsontocsv(input_json, output_path):
  keylist = []
  for key in jsonobj[0]:
    keylist.append(key)
    f = csv.writer(open(output_path, "w"))
    f.writerow(keylist)
 
  for record in jsonobj:
    currentrecord = []
    for key in keylist:
      currentrecord.append(record[key])
      f.writerow(currentrecord)

jsontocsv(jsonobj,'contactsfromJson.csv')





