import feedparser
import json
import os

RSS_FEEDS = {
    "Google News": "https://news.google.com/rss",
    "BBC World": "https:/import feedparser
import json
import os
from scripts.logger import title, success, info

title("NEWS COLLECTOR")

RSS_FEEDS = {
    "Google News": "https://news.google.com/rss",
    "BBC World": "https://feeds.bbci.co.uk/news/world/rss.xml",
    "CNN": "http://rss.cnn.com/rss/edition.rss"
}

OUTPUT_DIR = "output/news"
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "news.json")

os.makedirs(OUTPUT_DIR, exist_ok=True)

all_news = []

for source, url in RSS_FEEDS.items():

    info(f"Reading {source}...")

    feed = feedparser.parse(url)

    if not feed.entries:
        print(f"⚠️ No articles found for {source}")
        continue

    for article in feed.entries[:10]:

        all_news.append({
            "source": source,
            "title": article.get("title", ""),
            "link": article.get("link", ""),
            "published": article.get("published", ""),
            "summary": article.get("summary", "")
        })

with open(
    OUTPUT_FILE,
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        all_news,
        f,
        indent=4,
        ensure_ascii=False
    )

print()
success(f"Collected {len(all_news)} articles.")
success(f"Saved to {OUTPUT_FILE}")/feeds.bbci.co.uk/news/world/rss.xml",
    "CNN": "http://rss.cnn.com/rss/edition.rss"
}

all_news = []

for source, url in RSS_FEEDS.items():

    print(f"Reading {source}...")

    feed = feedparser.parse(url)

    for article in feed.entries[:10]:

        all_news.append({
            "source": source,
            "title": article.title,
            "link": article.link
        })

os.makedirs("output/news", exist_ok=True)

with open(
    "output/news/headlines.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        all_news,
        f,
        indent=4,
        ensure_ascii=False
    )

print()
print("=" * 50)
print(f"Collected {len(all_news)} headlines.")
print("=" * 50)
