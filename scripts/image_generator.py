import os
import json
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)

MODEL = "gemini-3.5-flash"

print("Using model:", MODEL)

# Load article
with open("output/article/article.json", "r", encoding="utf-8") as f:
    article = json.load(f)

title = article["title"]
content = article["article"]

prompt = f"""
You are an expert AI image prompt engineer.

Create 5 ultra-realistic image prompts for this news article.

Rules:

- One prompt per scene
- Cinematic
- Ultra realistic
- Documentary style
- Highly detailed
- 8K
- No text
- No watermark
- No logo

Return ONLY valid JSON.

Example:

{{
  "images":[
    {{
      "scene":1,
      "prompt":"..."
    }},
    {{
      "scene":2,
      "prompt":"..."
    }}
  ]
}}

TITLE:
{title}

ARTICLE:

{content}
"""

response = client.models.generate_content(
    model=MODEL,
    contents=prompt,
)

text = response.text.strip()

if text.startswith("```json"):
    text = text.replace("```json", "").replace("```", "").strip()

result = json.loads(text)

os.makedirs("output/images", exist_ok=True)

with open(
    "output/images/prompts.json",
    "w",
    encoding="utf-8"
) as f:
    json.dump(result, f, indent=4, ensure_ascii=False)

print("===================================")
print("IMAGE PROMPTS GENERATED")
print("===================================")
print("Scenes:", len(result["images"]))
