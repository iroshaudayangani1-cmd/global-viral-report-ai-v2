import os
import json
import feedparser

RSS_FEEDS = {
    "Google World": "https://news.google.com/rss",
    "BBC World": "https://feeds.bbci.co.uk/news/world/rss.xml",
    "Reuters World": "https://feeds.reuters.com/Reuters/worldNews",
    "AP News": "https://apnews.com/rss"
}

OUTPUT_DIR = "output/news"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "news.json")

os.makedirs(OUTPUT_DIR, exist_ok=True)

articles = []

for source, url in RSS_FEEDS.items():

    print(f"Reading {source}...")

    feed = feedparser.parse(url)

    for entry in feed.entries[:20]:

        articles.append({
            "source": source,
            "title": entry.get("title", ""),
            "link": entry.get("link", ""),
            "published": entry.get("published", ""),
            "summary": entry.get("summary", "")
        })

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(articles, f, indent=4, ensure_ascii=False)

print(f"\nCollected {len(articles)} articles")
print(f"Saved to {OUTPUT_FILE}")
