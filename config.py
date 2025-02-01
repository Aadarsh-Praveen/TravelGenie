import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Airtable
AIRTABLE_ACCESS_TOKEN = os.getenv("AIRTABLE_ACCESS_TOKEN")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

# Google Calendar
GOOGLE_CREDENTIALS_FILE = "./credentials.json"
SCOPES = ['https://www.googleapis.com/auth/calendar']