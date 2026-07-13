import json
import os

print("=" * 40)
print("CONTENT GENERATOR STARTED")
print("=" * 40)

# -----------------------------
# Load ranked story
# -----------------------------

story_file = "output/ranked/best_story.json"

if not os.path.exists(story_file):
    raise Exception("best_story.json not found")

with open(story_file, "r", encoding="utf-8") as f:
    story = json.load(f)

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

print()
print("AI Score:")
print(story.get("ai_score"))

print()
print("Reason:")
print(story.get("ai_reason"))

print()
print("Loaded successfully.")
