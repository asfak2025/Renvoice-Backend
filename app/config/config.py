import os
import sys
import dotenv

dotenv.load_dotenv()

# Load environment variables from .env file
MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://192.168.1.25:27017")
DB_NAME = os.getenv("DB_NAME", "renvoiceClient")


SERVER_MODE = os.getenv("SERVER_MODE", "DEV")



