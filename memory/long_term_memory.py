"""
long_term_memory.py
This file simulates persistent long-term memory.
No database, no API — fully local JSON file storage.

This memory stores:
- recurring concepts users love
- highest scoring prompts
- user aesthetic preferences
- style evolution feedback
"""

import json
import os

MEMORY_FILE = "memory_storage.json"


class LongTermMemory:
    def __init__(self):
        if not os.path.exists(MEMORY_FILE):
            with open(MEMORY_FILE, "w") as f:
                json.dump({"top_concepts": [], "top_prompts": []}, f)

    def load(self):
        """Load persistent memory from disk."""
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)

    def save(self, data):
        """Save updated memory to disk."""
        with open(MEMORY_FILE, "w") as f:
            json.dump(data, f, indent=2)

    def add_top_concept(self, concept: str):
        """Save trending concept patterns over time."""
        mem = self.load()
        if concept not in mem["top_concepts"]:
            mem["top_concepts"].append(concept)
        self.save(mem)

    def add_top_prompt(self, prompt: str, score: int):
        """Save best-performing prompts for future inspiration."""
        mem = self.load()
        mem["top_prompts"].append({"prompt": prompt, "score": score})
        # keep only last 50
        mem["top_prompts"] = mem["top_prompts"][-50:]
        self.save(mem)
