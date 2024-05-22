#without using error handling mechanism
import requests
from pymongo import MongoClient
resp=requests.get('https://jsonplaceholder.typicode.com/users')
user_list=resp.json()
client=MongoClient('mongodb://localhost:27017/')
print("connected successfully!!!!!")
db=client['recipedb']
user_colection=db['recipe']
user_colection.insert_many(user_list)
print("inserted successfully")