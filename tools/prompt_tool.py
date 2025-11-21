"""
prompt_tool.py
Creates structured AI art prompts for models like Flux, Komino, MJ style, etc.
"""

from tools.style_tool import apply_style

def build_prompt(concept: str, style_name: str = "leondreams"):
    """
    Build a structured artwork prompt using concept + style layers.
    """

    # Base composition
    base = (
        f"{concept}, ultra-detailed artwork, professional lighting, high-definition texture, "
        f"balanced composition, emotional storytelling, focus on subject, clean background"
    )

    # Apply styling presets (LeonDreams, Vintage Anime, Dreamcore, etc.)
    styled_prompt = apply_style(base, style_name)

    return styled_prompt
