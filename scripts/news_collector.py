import json
import os
import feedparser

from config import (
    RSS_FEEDS,
    NEWS_DIR,
    HEADLINES_FILE,
)

print("=" * 60)
print("GLOBAL VIRAL REPORT AI")
print("NEWS COLLECTOR")
print("=" * 60)

os.makedirs(NEWS_DIR, exist_ok=True)

articles = []
seen_links = set()

for source, url in RSS_FEEDS.items():

    print(f"Reading {source}...")

    feed = feedparser.parse(url)

    if not feed.entries:
        print(f"No articles found from {source}")
        continue

    for entry in feed.entries:

        link = entry.get("link", "").strip()

        if not link:
            continue

        if link in seen_links:
            continue

        seen_links.add(link)

        articles.append({
            "source": source,
            "title": entry.get("title", "").strip(),
            "link": link,
            "published": entry.get("published", ""),
            "summary": entry.get("summary", "")
        })

articles.sort(key=lambda x: x["title"])

with open(
    HEADLINES_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        articles,
        f,
        indent=4,
        ensure_ascii=False
    )

print()
print("=" * 60)
print(f"Collected {len(articles)} unique articles.")
print(f"Saved to {HEADLINES_FILE}")
print("=" * 60)
