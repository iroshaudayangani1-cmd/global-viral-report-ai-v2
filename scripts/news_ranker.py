import os
import json
import time
from google import genai
from bs4 import BeautifulSoup
# ----------------------------
# Gemini API
# ----------------------------

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)

# ----------------------------
# Load collected news
# ----------------------------

with open("output/news/news.json", "r", encoding="utf-8") as f:
    news = json.load(f)

news = news[:20]

headlines = []

for i, article in enumerate(news, start=1):
    headlines.append(f"{i}. {article['title']}")

prompt = f"""
You are an expert viral news editor.

Your task is to choose the ONE news story with the highest viral potential
for readers in the USA and UK.

Consider:
- Viral potential
- Public interest
- Search demand
- Facebook engagement
- Long-term SEO value

Return ONLY valid JSON.

Example:

{{
  "selected_story": 7,
  "score": 97,
  "reason": "This topic has strong global interest and high SEO potential."
}}

Headlines:

{chr(10).join(headlines)}
"""

# ----------------------------
# Try multiple Gemini models
# ----------------------------

MODELS = [
    "gemini-3.5-flash",
    "gemini-flash-latest",
    "gemini-2.0-flash",
]

response = None

for model in MODELS:
    print(f"Trying model: {model}")

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=model,
                contents=prompt,
            )
            print(f"Success with {model}")
            break

        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")

            if attempt < 2:
                time.sleep(10)

    if response:
        break

if response is None:
    raise Exception("All Gemini models failed.")

# ----------------------------
# Parse AI response
# ----------------------------

text = response.text.strip()

if text.startswith("```json"):
    text = text.replace("```json", "").replace("```", "").strip()

result = json.loads(text)

story_number = result["selected_story"]

best_story = news[story_number - 1]

best_story["ai_score"] = result["score"]
best_story["ai_reason"] = result["reason"]

# ----------------------------
# Save result
# ----------------------------

os.makedirs("output/ranked", exist_ok=True)

with open(
    "output/ranked/best_story.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        best_story,
        f,
        indent=4,
        ensure_ascii=False
    )

print("===================================")
print("BEST STORY")
print("===================================")
print(best_story["title"])
print()
print("AI Score:", best_story["ai_score"])
print()
print(best_story["ai_reason"])
