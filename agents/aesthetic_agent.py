from tools.evaluation_tool import score_prompt
from memory.session_memory import SessionMemory

class AestheticAgent:
    def __init__(self):
        self.memory = SessionMemory()

    def run(self, prompt):
        score = score_prompt(prompt)
        decision = "Strong concept" if score > 7 else "Needs refinement"
        self.memory.save("aesthetic_last_score", score)
        return {"score": score, "decision": decision}
