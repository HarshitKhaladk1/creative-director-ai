"""
evaluation_tool.py
Scores the visual potential of a prompt using rule-based scoring.
No ML models or external libraries → competition safe.
"""

def score_prompt(prompt: str):
    """
    Simple scoring function:
    - longer prompts score higher
    - certain keywords give bonus
    - returns score 1–10
    """

    base_score = min(len(prompt) // 35, 7)

    bonus = 0
    keywords = ["cinematic", "glow", "aesthetic", "ultra-detailed", "dreamcore", "vintage"]

    for word in keywords:
        if word in prompt.lower():
            bonus += 1

    total = base_score + bonus
    return min(total, 10)


def evaluate_prompt(prompt: str):
    """
    Provides feedback + final score.
    """
    score = score_prompt(prompt)

    if score >= 8:
        verdict = "Excellent concept with high viral potential."
    elif score >= 5:
        verdict = "Good concept but can be more specific or emotional."
    else:
        verdict = "Weak concept — needs clearer subject or style."

    return {"score": score, "verdict": verdict}
