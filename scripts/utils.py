import json
import os

def ensure_folder(path):
    os.makedirs(path, exist_ok=True)

def save_json(path, data):
    ensure_folder(os.path.dirname(path))

    with open(path, "w", encoding="utf-8") as f:
        json.dump(
            data,
            f,
            indent=4,
            ensure_ascii=False
        )

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
