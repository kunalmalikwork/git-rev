import os

from dotenv import load_dotenv

load_dotenv()

DB_URL = os.environ.get("DB-URL")
Database_pass = os.environ.get("DB-PASSWORD")

print(f"Using the Data base : {DB_URL}")