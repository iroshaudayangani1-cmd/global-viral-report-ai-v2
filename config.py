# ===========================
# Global Viral Report AI v3
# Configuration
# ===========================

# Gemini models (used in order)
GEMINI_MODELS = [
    "gemini-3.5-flash",
    "gemini-flash-latest",
    "gemini-2.5-flash",
    "gemini-2.0-flash"
]

# Retry settings
MAX_RETRIES = 3
RETRY_DELAY = 10

# Blog
BLOG_LANGUAGE = "English"

TARGET_COUNTRIES = [
    "USA",
    "UK"
]

ARTICLE_WORDS = 1000
