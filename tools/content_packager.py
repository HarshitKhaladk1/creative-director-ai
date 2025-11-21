"""
content_packager.py
Generates captions, hashtags, titles, and leoncmht packages.
"""

def generate_caption(prompt: str, score: int):
    return (
        f"Crafted with magic and detail — this artwork concept scores {score}/10 in aesthetic value. "
        f"Dive into a dreamy visual story."
    )

def generate_hashtags():
    return [
        "#aiart", "#aesthetic", "#genz", "#surreal", "#digitalart",
        "#leondreamsai", "#viralart", "#wallpaper", "#trending"
    ]

def generate_pinterest_title(concept: str):
    return f"Trending AI Art Concept – {concept.title()}"

def build_leoncmht_package(prompt: str):
    return {
        "caption": "A dreamy aesthetic masterpiece crafted with emotion.",
        "hashtags": "#leondreamsai #aesthetic #genz #aiart",
        "music": "Ambient Soft Dreamscape",
        "board": "LeonDreams AI Collections",
    }
