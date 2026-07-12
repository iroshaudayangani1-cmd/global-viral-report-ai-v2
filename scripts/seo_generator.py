import os
import json
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception("Missing GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash"

with open("output/article/article.json", "r", encoding="utf-8") as f:
    article = json.load(f)

prompt = f"""
You are an expert SEO editor.

Based on the article below generate:

- SEO title
- Meta description (150-160 chars)
- URL slug
- 15 SEO keywords
- 10 hashtags

Return ONLY valid JSON.

Article:

{json.dumps(article, indent=2)}
"""

print("Using model:", MODEL)

response = client.models.generate_content(
    model=MODEL,
    contents=prompt,
)

text = response.text.strip()

if text.startswith("```json"):
    text = text.replace("```json", "").replace("```", "").strip()

seo = json.loads(text)

os.makedirs("output/seo", exist_ok=True)

with open(
    "output/seo/seo.json",
    "w",
    encoding="utf-8",
) as f:
    json.dump(seo, f, indent=4, ensure_ascii=False)

print("SEO generated successfully")
