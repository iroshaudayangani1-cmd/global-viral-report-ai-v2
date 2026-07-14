"""
===========================================================
Global Viral Report AI v2
Configuration File
===========================================================
"""

import os
from pathlib import Path

# ==========================================================
# Project Paths
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

SCRIPTS_DIR = BASE_DIR / "scripts"

OUTPUT_DIR = BASE_DIR / "output"

NEWS_DIR = OUTPUT_DIR / "news"

GENERATED_DIR = OUTPUT_DIR / "generated"

IMAGES_DIR = OUTPUT_DIR / "images"

LOGS_DIR = OUTPUT_DIR / "logs"

# Create directories automatically
for folder in [
    OUTPUT_DIR,
    NEWS_DIR,
    GENERATED_DIR,
    IMAGES_DIR,
    LOGS_DIR,
]:
    folder.mkdir(parents=True, exist_ok=True)

# ==========================================================
# API Keys
# ==========================================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")

BLOGGER_CLIENT_ID = os.getenv("BLOGGER_CLIENT_ID", "")
BLOGGER_CLIENT_SECRET = os.getenv("BLOGGER_CLIENT_SECRET", "")
BLOGGER_REFRESH_TOKEN = os.getenv("BLOGGER_REFRESH_TOKEN", "")
BLOGGER_BLOG_ID = os.getenv("BLOGGER_BLOG_ID", "")

FACEBOOK_PAGE_ID = os.getenv("FACEBOOK_PAGE_ID", "")
FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN", "")

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY", "")

# ==========================================================
# RSS Sources
# ==========================================================

RSS_FEEDS = [

    "https://news.google.com/rss",

    "https://feeds.bbci.co.uk/news/rss.xml",

    "https://rss.cnn.com/rss/edition.rss",

    "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",

    "https://www.aljazeera.com/xml/rss/all.xml",

    "https://www.theguardian.com/world/rss",

    "https://abcnews.go.com/abcnews/topstories",

    "https://www.cbsnews.com/latest/rss/main",

    "https://feeds.a.dj.com/rss/RSSWorldNews.xml",

    "https://www.reddit.com/r/worldnews/.rss"

]

# ==========================================================
# AI Settings
# ==========================================================

GEMINI_MODEL = "gemini-2.5-flash"

MAX_ARTICLE_WORDS = 900

MAX_SUMMARY_WORDS = 250

TEMPERATURE = 0.7

TOP_P = 0.95

TOP_K = 40

# ==========================================================
# News Ranking
# ==========================================================

MAX_ARTICLES_TO_COLLECT = 100

TOP_STORIES_TO_ANALYZE = 20

BEST_STORY_COUNT = 1

# ==========================================================
# SEO
# ==========================================================

DEFAULT_AUTHOR = "Global Viral Report AI"

DEFAULT_LANGUAGE = "en"

DEFAULT_COUNTRY = "US"

SITE_NAME = "Global Viral Report"

# ==========================================================
# Timeouts
# ==========================================================

REQUEST_TIMEOUT = 20

DOWNLOAD_TIMEOUT = 60

# ==========================================================
# User Agent
# ==========================================================

USER_AGENT = (
    "Mozilla/5.0 "
    "(Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 "
    "(KHTML, like Gecko) "
    "Chrome/137.0 Safari/537.36"
)
