from motor.motor_asyncio import AsyncIOMotorClient
from app.config.config import DB_NAME,MONGODB_URL

client = AsyncIOMotorClient(MONGODB_URL)
db = client[DB_NAME]

call_collection=db["call-logs"]
district_collection=db['districts']
org_collection=db['org']
campaign_collection=db['campaign']
payment_collection=db['payments']
