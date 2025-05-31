import json
import os

FILE_PATH = "chat_ids.json"

def load_chat_ids():
    if not os.path.exists(FILE_PATH):
        return set()
    with open(FILE_PATH, "r") as f:
        return set(json.load(f))

def save_chat_ids(chat_ids):
    with open(FILE_PATH, "w") as f:
        json.dump(list(chat_ids), f, indent=2)
