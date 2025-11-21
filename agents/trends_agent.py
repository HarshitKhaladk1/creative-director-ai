import json
from tools.trend_tool import get_trends
from memory.session_memory import SessionMemory

class TrendAgent:
    def __init__(self):
        self.memory = SessionMemory()

    def run(self, user_input):
        trends = get_trends()
        idea = f"For your theme '{user_input}', the top trending aesthetics are: {', '.join(trends)}."
        self.memory.save("trend_agent_last_output", idea)
        return idea
