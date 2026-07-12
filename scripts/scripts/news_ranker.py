import os
import json
from google import genai

# -----------------------------
# Load Gemini API Key
# -----------------------------
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)

# -----------------------------
# Load collected news
# -----------------------------
with open("output/news/news.json", "r", encoding="utf-8") as f:
    news = json.load(f)

# Use only the first 20 stories to avoid sending too much data
headlines = []

for i, article in enumerate(news[:20], start=1):
    headlines.append(f"{i}. {article['title']}")

prompt = f"""
You are an expert news editor.

Below is a list of news headlines.

Choose the ONE story with the highest viral potential for readers in the USA and UK.

Consider:
- Public interest
- Search popularity
- Social media engagement
- Long-term relevance

Return ONLY the number of the best headline.

Headlines:

{chr(10).join(headlines)}
"""

response = client.models.generate_content(
    model="gemini-2.5-flash-lite",
    contents=prompt
)

best_number = int(response.text.strip())

best_story = news[best_number - 1]

os.makedirs("output/ranked", exist_ok=True)

with open("output/ranked/best_story.json", "w", encoding="utf-8") as f:
    json.dump(best_story, f, indent=4, ensure_ascii=False)

print("Best Story Selected:")
print(best_story["title"])
