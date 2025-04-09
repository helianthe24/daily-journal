import os
import json

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "entries")
os.makedirs(DATA_DIR, exist_ok=True)

def save_entry(date_str, entry):
    file_path = os.path.join(DATA_DIR, f"{date_str}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(entry, f, ensure_ascii=False, indent=4)
