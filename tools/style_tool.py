"""
style_tool.py
Applies predefined styling layers (LeonDreams, Dreamcore, Anime, Dark Aesthetic, etc.)
"""

STYLE_PRESETS = {
    "leondreams": (
        " soft glow, dreamy atmosphere, magical realism, high contrast, gentle highlights, "
        "subtle neon accents, emotional cinematic framing"
    ),

    "dreamcore": (
        " surreal haze, cloudy light bloom, floating feeling, nostalgic ambience"
    ),

    "dark_aesthetic": (
        " deep shadows, dramatic lighting, dark botanical tones, moody composition"
    ),

    "vintage_anime": (
        " 90s anime film grain, retro palette, soft outlines, emotional storytelling"
    ),

    "hyperreal": (
        " ultra-HD clarity, crisp detail, photorealistic shading, macro texture"
    )
}


def apply_style(prompt: str, style_name: str):
    """Attach a style preset to the base prompt."""
    style = STYLE_PRESETS.get(style_name.lower(), "")

    return f"{prompt}, {style} , award-winning artwork"
