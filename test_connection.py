# This script tests if the remote connection can be established properly.

from pymongo import MongoClient

cluster = MongoClient(host='mongodb+srv://{username}:{password}@cluster0.o2sen.mongodb.net/{dbname}?retryWrites=true&w=majority')
db = cluster['test']
collection = db['test']

results = collection.find({'name': 'joe'})

flag = 0
for result in results:
    if result['name'] == 'joe':
        continue
    else:
        flag += 1

if flag == 0:
    print('Connection is successful ')
