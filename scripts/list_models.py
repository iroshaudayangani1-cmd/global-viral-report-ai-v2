import os
from google import genai

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise Exception("GEMINI_API_KEY not found")

client = genai.Client(api_key=api_key)

print("Available models:\n")

for model in client.models.list():
    print(model.name)
