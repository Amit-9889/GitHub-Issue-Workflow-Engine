# app/config/settings.py

import os
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GROQ_API_KEY = os.getenv("GROP_API_KEY")

GITHUB_OWNER = os.getenv("GITHUB_OWNER")
GITHUB_REPO = os.getenv("GITHUB_REPO")

MCP_BASE_URL = os.getenv("MCP_BASE_URL","http://127.0.0.1:9000")
