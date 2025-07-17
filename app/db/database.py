import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from config.config import MONGODB_URL,DB_NAME
load_dotenv()
client = AsyncIOMotorClient(MONGODB_URL)
db = client.get_default_database()
