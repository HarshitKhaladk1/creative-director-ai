"""
session_state.py
Manages short-term, per-session memory used by agents while running.
This includes: conversation history, last generated prompt, last trends,
and any temporary computation values.
"""

class SessionState:
    def __init__(self):
        # Stores the conversation or agent messages
        self.history = []

        # For keeping track of intermediate results
        self.last_trends = None
        self.last_prompt = None
        self.last_score = None
        self.last_feedback = None

    def add_history(self, role: str, message: str):
        """Append a message to the session history."""
        self.history.append({"role": role, "message": message})

    def get_history(self):
        """Return conversation history."""
        return self.history

    def clear(self):
        """Reset the session memory."""
        self.history = []
        self.last_trends = None
        self.last_prompt = None
        self.last_score = None
        self.last_feedback = None
