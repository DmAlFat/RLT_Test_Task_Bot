from motor.motor_asyncio import AsyncIOMotorClient

from config import HOST, PORT, DATABASE, COLLECTION

client = AsyncIOMotorClient(f"mongodb://{HOST}:{PORT}")
collection = client[DATABASE][COLLECTION]
