from motor.motor_asyncio import AsyncIOMotorClient
from app.config.config import DB_NAME,MONGODB_URL

client = AsyncIOMotorClient(MONGODB_URL)
db = client[DB_NAME]

call_collection='call-logs'
district_collection='districts'
org_collection='org'
campaign_collection='campaign'
payment_collection='payments'
