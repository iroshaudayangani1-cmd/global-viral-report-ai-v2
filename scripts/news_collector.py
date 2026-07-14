"""
=========================================================
Global Viral Report AI v2
news_collector.py
---------------------------------------------------------

Collects news from multiple RSS feeds
Removes duplicates
Scores articles
Chooses the most viral story

Author: ChatGPT
=========================================================
"""

import json
import csv
import hashlib
import logging
import re
from datetime import datetime, timezone
from pathlib import Path

import feedparser
import requests

from config import (
    RSS_FEEDS,
    NEWS_DIR,
    USER_AGENT,
    REQUEST_TIMEOUT,
    MAX_ARTICLES_TO_COLLECT,
    TOP_STORIES_TO_ANALYZE,
)

##########################################################
# Logging
##########################################################

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logger = logging.getLogger("collector")


##########################################################
# News Collector
##########################################################

class NewsCollector:

    def __init__(self):

        self.headers = {
            "User-Agent": USER_AGENT
        }

        self.articles = []

        self.seen = set()


##########################################################
# Download RSS
##########################################################

    def download_feed(self, url):

        try:

            response = requests.get(
                url,
                headers=self.headers,
                timeout=REQUEST_TIMEOUT
            )

            response.raise_for_status()

            return feedparser.parse(response.text)

        except Exception as e:

            logger.error(f"RSS ERROR : {url}")

            logger.error(str(e))

            return None


##########################################################
# Clean HTML
##########################################################

    def clean_html(self, text):

        if not text:
            return ""

        text = re.sub("<.*?>", "", text)

        text = text.replace("\n", " ")

        text = re.sub(r"\s+", " ", text)

        return text.strip()


##########################################################
# Create unique id
##########################################################

    def article_id(self, title, link):

        value = title + link

        return hashlib.md5(
            value.encode("utf-8")
        ).hexdigest()


##########################################################
# Parse one feed
##########################################################

    def parse_feed(self, feed):

        if not feed:
            return

        for item in feed.entries:

            try:

                title = item.get("title", "").strip()

                link = item.get("link", "").strip()

                summary = self.clean_html(
                    item.get("summary", "")
                )

                published = item.get(
                    "published",
                    ""
                )

                source = ""

                if "source" in item:
                    try:
                        source = item.source.title
                    except:
                        pass

                uid = self.article_id(
                    title,
                    link
                )

                if uid in self.seen:
                    continue

                self.seen.add(uid)

                self.articles.append({

                    "id": uid,

                    "title": title,

                    "summary": summary,

                    "link": link,

                    "published": published,

                    "source": source,

                    "score": 0

                })

            except Exception as e:

                logger.error(str(e))


##########################################################
# Collect all feeds
##########################################################

    def collect(self):

        logger.info("Collecting news...")

        for url in RSS_FEEDS:

            logger.info(url)

            feed = self.download_feed(url)

            self.parse_feed(feed)

        logger.info(
            f"Collected {len(self.articles)} articles."
        )


##########################################################
# Score keywords
##########################################################

    def keyword_score(self, article):

        score = 0

        text = (
            article["title"] +
            " " +
            article["summary"]
        ).lower()

        keywords = [

            "breaking",

            "exclusive",

            "war",

            "trump",

            "elon",

            "musk",

            "ai",

            "openai",

            "chatgpt",

            "google",

            "apple",

            "tesla",

            "viral",

            "covid",

            "earthquake",

            "explosion",

            "crash",

            "bitcoin",

            "crypto",

            "election",

            "president",

            "china",

            "usa",

            "uk",

            "canada",

            "australia"

        ]

        for word in keywords:

            if word in text:

                score += 5

        ##########################################################
# Freshness Score
##########################################################

    def freshness_score(self, article):

        published = article.get("published", "")

        if not published:
            return 0

        try:

            parsed = feedparser._parse_date(published)

            if parsed is None:
                return 0

            article_time = datetime(*parsed[:6], tzinfo=timezone.utc)

            now = datetime.now(timezone.utc)

            hours = (now - article_time).total_seconds() / 3600

            if hours <= 2:
                return 40

            elif hours <= 6:
                return 30

            elif hours <= 12:
                return 20

            elif hours <= 24:
                return 10

            return 5

        except Exception:

            return 0


##########################################################
# Calculate Final Score
##########################################################

    def score_articles(self):

        logger.info("Scoring articles...")

        for article in self.articles:

            score = 0

            score += self.keyword_score(article)

            score += self.freshness_score(article)

            title = article["title"].lower()

            if len(title) > 60:
                score += 5

            if len(article["summary"]) > 120:
                score += 5

            article["score"] = score


##########################################################
# Sort Articles
##########################################################

    def sort_articles(self):

        self.articles = sorted(

            self.articles,

            key=lambda x: x["score"],

            reverse=True

        )


##########################################################
# Limit Results
##########################################################

    def trim_articles(self):

        self.articles = self.articles[:MAX_ARTICLES_TO_COLLECT]


##########################################################
# Best Story
##########################################################

    def best_story(self):

        if not self.articles:
            return None

        return self.articles[0]


##########################################################
# Save JSON
##########################################################

    def save_json(self):

        NEWS_DIR.mkdir(parents=True, exist_ok=True)

        latest = NEWS_DIR / "latest_news.json"

        with open(latest, "w", encoding="utf-8") as f:

            json.dump(

                self.articles,

                f,

                indent=4,

                ensure_ascii=False

            )

        logger.info(f"Saved {latest}")

        best = NEWS_DIR / "best_story.json"

        with open(best, "w", encoding="utf-8") as f:

            json.dump(

                self.best_story(),

                f,

                indent=4,

                ensure_ascii=False

            )

        logger.info(f"Saved {best}")


##########################################################
# Save CSV
##########################################################

    def save_csv(self):

        csv_file = NEWS_DIR / "latest_news.csv"

        with open(

            csv_file,

            "w",

            newline="",

            encoding="utf-8"

        ) as file:

            writer = csv.writer(file)

            writer.writerow([

                "Score",

                "Title",

                "Source",

                "Published",

                "Link"

            ])

            for article in self.articles:

                writer.writerow([

                    article["score"],

                    article["title"],

                    article["source"],

                    article["published"],

                    article["link"]

                ])

        logger.info(f"Saved {csv_file}")


##########################################################
# Top Stories
##########################################################

    def print_top_stories(self):

        logger.info("")

        logger.info("========== TOP STORIES ==========")

        for i, article in enumerate(

                self.articles[:TOP_STORIES_TO_ANALYZE],

                start=1):

            logger.info(

                f"{i}. "

                f"[{article['score']}] "

                f"{article['title']}"

            )

        logger.info("================================")
        return score
##########################################################
# Run Collector
##########################################################

    def run(self):

        logger.info("=" * 60)
        logger.info("GLOBAL VIRAL REPORT AI V2")
        logger.info("NEWS COLLECTOR STARTED")
        logger.info("=" * 60)

        self.collect()

        if not self.articles:
            logger.warning("No articles were collected.")
            return

        logger.info(f"Collected {len(self.articles)} unique articles.")

        self.score_articles()

        self.sort_articles()

        self.trim_articles()

        self.save_json()

        self.save_csv()

        self.print_top_stories()

        best = self.best_story()

        if best:

            logger.info("")
            logger.info("=" * 60)
            logger.info("BEST STORY")
            logger.info("=" * 60)
            logger.info(f"Title     : {best['title']}")
            logger.info(f"Source    : {best['source']}")
            logger.info(f"Published : {best['published']}")
            logger.info(f"Score     : {best['score']}")
            logger.info(f"Link      : {best['link']}")
            logger.info("=" * 60)

        logger.info("")
        logger.info("News collection completed successfully.")


##########################################################
# Main
##########################################################

def main():

    collector = NewsCollector()

    collector.run()


if __name__ == "__main__":

    main()
