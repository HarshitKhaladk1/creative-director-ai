"""
trend_tool.py
Simulates trend analysis for AI art aesthetics.
No external API calls are used — fully offline.
"""

import random

TREND_DATA = [
    "Gen-Z Anime",
    "Moody Cinematic",
    "Soft Pastel Glow",
    "Cyber-Grunge Aesthetic",
    "Dreamcore Fantasy",
    "Hyperreal Macro Photography",
    "Dark Romanticism",
    "Vintage Japanese Anime",
    "Mystical Floral Glow",
    "Surreal Dream Aesthetic",
    "Neon Night City",
    "Spiritual Mystic Theme",
    "Minimalist Abstract Art",
    "Dark Botanical",
    "Cosmic Fog Atmosphere",
]

def get_trends(top_k: int = 5):
    """Return random trending topics (simulated)."""
    return random.sample(TREND_DATA, top_k)
