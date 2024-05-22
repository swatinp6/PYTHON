import requests
from pymongo import MongoClient
resp=requests.get('https://jsonplaceholder.typicode.com/users')
user_list=resp.json()

try:
    client=MongoClient('mongodb://localhost:27017/')
    print("connected successfully")
    db=client['errorhdb']
    collection=db['errorh']
    collection.insert_many(user_list)
    print("data inserted successfully!!!!!")
except:
    print("Mongodb is not connected")
finally:
    collection=None
    db=None
    client=None