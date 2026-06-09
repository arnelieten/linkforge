import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# LLM Providers
GEMININI_API_KEY = os.environ["GEMINI_API_KEY"]
OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
ANTROPIC_API_KEY = os.environ["ANTROPIC_API_KEY"]

# Telegram
BOTFATHER_API_KEY=os.environ["BOTFATHER_API_KEY"] # auth to set up webhook
BOTFATHER_WEBHOOK_SECRET=os.environ["BOTFATHER_WEBHOOK_SECRET"] # auth to check requests
BOTFATHER_LINK=os.environ["BOTFATHER_LINK"]
BOTFATHER_USER_ID=os.environ["BOTFATHER_USER_ID"]

# Sqlite database
SQLITE_DB_PATH=Path(os.environ["SQLITE_DB_PATH"])
SQLITE_SESSION_LIMIT=int(os.environ["SQLITE_SESSION_LIMIT"])
