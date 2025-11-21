from tools.prompt_tool import build_prompt
from memory.session_memory import SessionMemory

class PromptAgent:
    def __init__(self):
        self.memory = SessionMemory()

    def run(self, concept):
        prompt = build_prompt(concept)
        self.memory.save("prompt_agent_last_output", prompt)
        return prompt
