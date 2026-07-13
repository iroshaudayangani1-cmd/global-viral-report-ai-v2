import os
import json
import time
from google import genai
from bs4 import BeautifulSoup

from config import (
    GEMINI_MODELS,
    MAX_RETRIES,
    RETRY_DELAY,
)

from scripts.utils import (
    save_json,
    load_json,
)

from scripts.logger import (
    title,
    success,
    info,
    warning,
)

title("GLOBAL VIRAL CONTENT GENERATOR")

# ----------------------------------
# Gemini API
# ----------------------------------

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception("GEMINI_API_KEY not found.")

client = genai.Client(api_key=api_key)

success("Gemini initialized.")

# ----------------------------------
# Load News
# ----------------------------------

NEWS_FILE = "output/news/news.json"

if not os.path.exists(NEWS_FILE):
    raise Exception("news.json not found.")

news = load_json(NEWS_FILE)

news = news[:20]

info(f"Loaded {len(news)} news stories.")
