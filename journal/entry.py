import datetime
import json
import os
from journal.storage import save_entry

QUESTIONS = {
    "emotion": "How do you feel today?",
    "intention": "What is your intention for the day?",
    "pride": "What are you proud of today?"
}

def create_entry(date_str=None):
    if not date_str:
        date_str = datetime.date.today().isoformat()

    answers = {}
    print(f"\nJournal Entry for {date_str}:\n")
    for key, question in QUESTIONS.items():
        answers[key] = input(f"{question}\n> ")

    entry = {
        "date": date_str,
        "answers": answers
    }

    save_entry(date_str, entry)
    print("Entry saved.")
