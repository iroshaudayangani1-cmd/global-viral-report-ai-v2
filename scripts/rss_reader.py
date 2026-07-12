import feedparser

# Trusted RSS feeds
RSS_FEEDS = {
    "Google News": "https://news.google.com/rss",
    "Reuters World": "https://feeds.reuters.com/reuters/worldNews",
    "BBC World": "http://feeds.bbci.co.uk/news/world/rss.xml"
}

def fetch_news():
    print("=" * 60)
    print("LATEST NEWS HEADLINES")
    print("=" * 60)

    for source, url in RSS_FEEDS.items():
        print(f"\nSource: {source}")

        feed = feedparser.parse(url)

        if not feed.entries:
            print("No news found.")
            continue

        # Show the first 5 headlines
        for i, entry in enumerate(feed.entries[:5], start=1):
            print(f"{i}. {entry.title}")

if __name__ == "__main__":
    fetch_news()
