from pymongo import MongoClient
from dotenv import load_dotenv
import os

class MongoDB:
    def __init__(self):
        db_host = os.getenv("MONGODB_HOST")
        db_port = os.getenv("MONGODB_PORT")
        db_username = os.getenv("MONGODB_USER")
        db_password = os.getenv("MONGODB_PW")
        self.uri = f"mongodb://{db_username}:{db_password}@{db_host}:{db_port}/"
        self.client = None

    def connect(self):
        self.client = MongoClient(self.uri)

    def close(self):
        if self.client:
            self.client.close()

load_dotenv()

async def get_mongodb():
    mongodb = MongoDB()
    try:
        mongodb.connect()
        yield mongodb
    finally:
        mongodb.close()