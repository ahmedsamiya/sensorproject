from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri="mongodb+srv://sam_user:Samiya%40123@cluster0.hjtt9y3.mongodb.net/?appName=Cluster0"

client=MongoClient(uri)
DATABASE_NAME="Sensor_project_database"
COLLECTION_NAME='waferfault'

df=pd.read_csv(r"C:\Users\pc\Downloads\Sensor Project\notebooks\wafer_23012020_041211.csv")
df.head()

df=df.drop('Unnamed: 0',axis=1)

json_record=list(json.loads(df.T.to_json()).values())

json_record
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
