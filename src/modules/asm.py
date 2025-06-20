# src/modules/asm.py
# Functional implementation of the Abstract Symbology Module.

from .base_module import SpecializedCognitiveModule

class AbstractSymbologyModule(SpecializedCognitiveModule):
    """
    SCM specializing in formal logic, mathematics, and programming languages.
    It acts as an expert code analyst.
    """
    def __init__(self):
        super().__init__("ASM", "Abstract Symbology Module (Code, Math, Logic)")

    def get_capabilities(self):
        """Reports this module's skills to the CRC."""
        return {'code', 'python', 'function', 'analyze', 'vulnerabilities', 'optimizations', 'math', 'logic'}

    def construct_prompt(self, user_query):
        """Constructs a prompt that tells Gemini to act as a code analyst."""
        # We extract the core request from the user's query.
        core_request = user_query.replace("Please analyze the following Python code for bugs and suggest improvements:", "").strip()
        
        prompt = f"""
        **Persona:** You are an elite software engineer and cybersecurity analyst. Your task is to perform a rigorous code review.

        **Context:** You have been given the following code snippet to analyze.

        **Code to Analyze:**
        ```python
        {core_request}
        ```

        **Instructions:**
        1.  Identify any potential bugs, errors, or edge cases (e.g., infinite recursion, type errors, logical flaws).
        2.  Identify any potential security vulnerabilities (e.g., injection attacks, unsafe operations).
        3.  Suggest improvements for performance, readability, and adherence to best practices.
        4.  Provide a corrected or refactored version of the code if necessary.
        5.  Format your response clearly with sections for Bugs, Vulnerabilities, and Suggestions.
        """
        return prompt
