import os

# ==========================
# Gemini
# ==========================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

MODEL = "gemini-2.5-flash"

# ==========================
# RSS Sources
# ==========================

RSS_FEEDS = {
    "Google World": "https://news.google.com/rss",
    "BBC World": "https://feeds.bbci.co.uk/news/world/rss.xml",
    "Reuters World": "https://feeds.reuters.com/Reuters/worldNews",
    "AP News": "https://apnews.com/rss",
    "CNN": "http://rss.cnn.com/rss/edition.rss"
}

# ==========================
# Output folders
# ==========================

NEWS_DIR = "output/news"
GENERATED_DIR = "output/generated"

HEADLINES_FILE = f"{NEWS_DIR}/headlines.json"
CONTENT_FILE = f"{GENERATED_DIR}/content.json"
