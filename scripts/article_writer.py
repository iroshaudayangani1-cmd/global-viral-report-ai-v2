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

MODEL = "gemini-2.5-flash"

# ----------------------------
# Load selected story
# ----------------------------

with open(
    "output/ranked/best_story.json",
    "r",
    encoding="utf-8"
) as f:
    story = json.load(f)

prompt = f"""
You are an award-winning journalist and SEO expert.

Write a high-quality original news article.

Story Title:
{story["title"]}

Source:
{story.get("source", "")}

Link:
{story.get("link", "")}

Requirements:

• 800-1200 words
• Neutral journalistic tone
• Easy to read
• Optimized for Google SEO
• Optimized for USA readers
• Include headings
• Include introduction
• Include conclusion

Return ONLY valid JSON.

Example:

{{
  "seo_title": "...",
  "meta_description": "...",
  "slug": "...",
  "category": "World News",
  "tags": [
      "news",
      "world"
  ],
  "article": "..."
}}
"""

print(f"Using model: {MODEL}")

response = client.models.generate_content(
    model=MODEL,
    contents=prompt
)

text = response.text.strip()

if text.startswith("```json"):
    text = text.replace("```json", "").replace("```", "").strip()

article = json.loads(text)

os.makedirs("output/article", exist_ok=True)

with open(
    "output/article/article.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(
        article,
        f,
        indent=4,
        ensure_ascii=False
    )

print("=" * 50)
print("ARTICLE CREATED")
print("=" * 50)
print(article["seo_title"])
