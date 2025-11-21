"""
memory_bank.py
A unified abstraction around both session memory and long-term memory.
Agents import this to store or retrieve information.
"""

from memory.session_state import SessionState
from memory.long_term_memory import LongTermMemory


class MemoryBank:
    def __init__(self):
        self.session = SessionState()
        self.long_term = LongTermMemory()

    def store_prompt(self, prompt: str, score: int):
        """Store the best prompts long-term."""
        if score >= 8:
            self.long_term.add_top_prompt(prompt, score)

    def store_concept(self, concept: str):
        """Store successful concepts long-term."""
        self.long_term.add_top_concept(concept)

    def compact_history(self):
        """
        Context compaction:
        Removes low-value entries from session history 
        to avoid overloading memory between turns.
        """

        compacted = []
        for entry in self.session.history:
            # Keep only agent reasoning, final outputs, and major data points
            if any(key in entry["message"].lower() for key in ["trend", "prompt", "score"]):
                compacted.append(entry)

        self.session.history = compacted[:10]  # cap at last 10 important entries

    def reset_session(self):
        """Reset short-term memory while preserving long-term memory."""
        self.session.clear()
