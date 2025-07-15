import json
import os

MEMORY_FILE = "memory_log.json"

def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_memory(memory):
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, indent=4, ensure_ascii=False)

def remember(prompt, response):
    memory = load_memory()
    memory.append({"prompt": prompt, "response": response})
    save_memory(memory)
