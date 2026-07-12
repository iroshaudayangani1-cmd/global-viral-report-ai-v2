import os
import json
from google import genai

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
    headlines.append(
        f"{i}. {article['title']}"
    )

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

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt
)

result = json.loads(response.text)

story_number = result["selected_story"]

best_story = news[story_number - 1]

best_story["ai_score"] = result["score"]
best_story["ai_reason"] = result["reason"]

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
