"""
text_cleaner.py
Utility cleaner for agent messages, ensuring the text is polished.
"""

def clean_text(text: str):
    text = text.replace("\n", " ").strip()
    while "  " in text:
        text = text.replace("  ", " ")
    return text
