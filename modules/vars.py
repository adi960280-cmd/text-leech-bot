import os

API_ID    = os.environ.get("API_ID", "29115102")
API_HASH  = os.environ.get("API_HASH", "1a331db2b00e9d2decaa9c7276449eb6")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
