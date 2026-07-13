import json
import os

print("=" * 40)
print("CONTENT GENERATOR STARTED")
print("=" * 40)

# -----------------------------
# Load collected news
# -----------------------------
from bs4 import BeautifulSoup
news_file = "output/news/news.json"

if not os.path.exists(news_file):
    raise Exception("news.json not found")

with open(news_file, "r", encoding="utf-8") as f:
    news = json.load(f)

if len(news) == 0:
    raise Exception("No news articles found")

# Temporary: use the first article
story = news[0]

print()
print("Selected Story")
print("-------------------------")
print(story["title"])

print()
print("Source:")
print(story.get("source", "Unknown"))

print()
print("URL:")
print(story.get("link", "No URL"))

raw_summary = story.get("summary", "")

clean_summary = BeautifulSoup(raw_summary, "html.parser").get_text(
    separator=" ",
    strip=True
)

print()
print("Clean Summary:")
print(clean_summary)

print()
print("Loaded successfully.")
