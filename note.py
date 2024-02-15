import time
import json

def save(notes):
    with open("savedNotes.json", "w", encoding="utf-8") as doc:
        doc.write(json.dumps(notes, ensure_ascii=False))