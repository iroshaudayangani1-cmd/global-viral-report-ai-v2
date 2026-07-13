import os
import json
import time
from google import genai
from google.genai import types

# =====================================================
# CONFIGURATION
# =====================================================

INPUT_FILE = "output/news/headlines.json"

OUTPUT_DIR = "output/generated"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "content.json")

MODEL_NAME = "gemini-2.5-flash"

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("=" * 60)
print("GLOBAL VIRAL REPORT AI")
print("Unified Content Generator")
print("=" * 60)

# =====================================================
# GEMINI CLIENT
# =====================================================

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise Exception("GEMINI_API_KEY not found.")

client = genai.Client(api_key=API_KEY)

# =====================================================
# LOAD HEADLINES
# =====================================================

if not os.path.exists(INPUT_FILE):
    raise Exception(f"{INPUT_FILE} not found.")

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    headlines = json.load(f)

if len(headlines) == 0:
    raise Exception("No headlines found.")

print(f"Loaded {len(headlines)} headlines.")

# =====================================================
# BUILD HEADLINE LIST
# =====================================================

headline_text = ""

for index, item in enumerate(headlines, start=1):

    headline_text += (
        f"{index}. {item.get('title','')}\n"
        f"Source: {item.get('source','')}\n"
        f"URL: {item.get('link','')}\n\n"
    )

print("Headline list prepared.")
