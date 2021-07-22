import pymongo
from pymongo import MongoClient
Client=pymongo.MongoClient("mongodb+srv://Akshata:akshata123@cluster0.js4au.mongodb.net/myFirstDatabase?retryWrites=true&w=majority");
print(Client.list_database_names())
db=Client.Products
print(db.list_collection_names())
from pprint import pprint
import pandas as pd
CM = [data for data in db.phones.find()]
df_CM = pd.DataFrame(CM)
pprint(df_CM)