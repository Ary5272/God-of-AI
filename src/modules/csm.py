# src/modules/csm.py
# Functional implementation of the Creative Synthesis Module.

from .base_module import SpecializedCognitiveModule

class CreativeSynthesisModule(SpecializedCognitiveModule):
    """
    SCM specializing in generating novel, creative, and artistic concepts.
    It acts as a creative writer and concept artist.
    """
    def __init__(self):
        super().__init__("CSM", "Creative Synthesis Module")

    def get_capabilities(self):
        """Reports this module's skills to the CRC."""
        return {'creative', 'generate', 'concepts', 'ideas', 'art', 'design', 'story', 'visualization'}

    def construct_prompt(self, user_query):
        """Constructs a prompt that tells Gemini to act as a creative writer."""
        core_request = user_query.replace("Generate a short story concept about", "").strip()

        prompt = f"""
        **Persona:** You are a visionary science fiction author and world-builder.

        **Context:** You have been tasked with creating a compelling, original story concept based on a core idea.

        **Core Idea:** "{core_request}"

        **Instructions:**
        1.  Generate a unique title for the story.
        2.  Write a compelling logline (a one or two-sentence summary).
        3.  Outline the main character(s), including their primary motivation and conflict.
        4.  Describe the central plot, including an inciting incident, rising action, and a potential climax.
        5.  Suggest a unique theme or question that the story explores.
        """
        return prompt
