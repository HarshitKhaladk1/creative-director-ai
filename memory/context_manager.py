"""
context_manager.py
Builds refined context packets to feed agents.
Uses history, long-term preferences, and the current task.
"""

class ContextManager:
    def __init__(self, memory_bank):
        self.memory = memory_bank

    def build_context(self, task_description: str):
        """
        Assemble the context for an agent:
        - recent important session events
        - selected long-term preferences
        - the user’s task for this specific execution
        """

        session_history = self.memory.session.get_history()

        # load persistent patterns
        long_term = self.memory.long_term.load()

        top_concepts = long_term.get("top_concepts", [])[-5:]
        top_prompts = long_term.get("top_prompts", [])[-5:]

        context = {
            "task": task_description,
            "session_history": session_history,
            "past_concepts": top_concepts,
            "top_prompts": top_prompts,
        }

        return context
