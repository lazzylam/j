from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_ID = int(os.getenv("OWNER_ID"))
FORWARD_DELAY = int(os.getenv("FORWARD_DELAY", 30))

print(f"[CONFIG] OWNER_ID = {OWNER_ID} (type: {type(OWNER_ID)})")