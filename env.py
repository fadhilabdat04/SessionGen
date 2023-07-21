import os
from dotenv import load_dotenv

load_dotenv()

API_ID = os.getenv("API_ID", "12857763").strip()
API_HASH = os.getenv("API_HASH", "7b71e8bca0d5e1c6d8383ae818d9ec8d").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "6375262996:AAFZBXDHSjs6Yn5M_1CbV_XS-tWQqG_wYX4").strip()
DATABASE_URL = os.getenv("DATABASE_URL", "postgres://hzuxnrbc:C0n4fUsTXHixFOwGeso1YkuBtUJIt9Cb@rosie.db.elephantsql.com/hzuxnrbc").strip() # Not a necessary variable anymore but you can add to get stats
MUST_JOIN = os.getenv("MUST_JOIN", "SiArabSupport")

if not API_ID:
    raise SystemExit("No API_ID found. Exiting...")
elif not API_HASH:
    raise SystemExit("No API_HASH found. Exiting...")
elif not BOT_TOKEN:
    raise SystemExit("No BOT_TOKEN found. Exiting...")
'''
if not DATABASE_URL:
    print("No DATABASE_URL found. Exiting...")
    raise SystemExit
'''

try:
    API_ID = int(API_ID)
except ValueError:
    raise SystemExit("API_ID is not a valid integer. Exiting...")

if 'postgres' in DATABASE_URL and 'postgresql' not in DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")
