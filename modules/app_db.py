from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv("../db/creds.env")

mUser = os.getenv()
mPass = os.getenv()
mDB = os.getenv()

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = "mongodb+srv://"+ mUser + ":" + mPass + "@cluster.mongodb.net/" + mDB
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
  
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":   
  
   # Get the database
   dbname = get_database()