# main.py
# The primary entry point for initializing and interacting with the functional Project Chimera AI.

from src.chimera_core import Chimera

def run_demonstration():
    """
    Initializes the Chimera system and runs a series of demonstration tasks
    to showcase its functional, multi-persona capabilities.
    """
    # Initialize the Chimera AI system
    chimera_ai = Chimera()

    # --- Task Demonstration ---
    
    # Task 1: Routed to ASM (Abstract Symbology Module)
    # The ASM will act as a code analyst and ask Gemini to review this function.
    code_to_analyze = """
def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n-1) # Potential issue: no base case for negative numbers
"""
    chimera_ai.task(f"Please analyze the following Python code for bugs and suggest improvements: {code_to_analyze}")
    
    # Task 2: Routed to SFE (Sensory Fusion Engine)
    # The SFE will act as a data scientist to find insights.
    data_description = "Dataset contains daily sales figures, marketing spend, and website traffic for the last quarter. There was a sales dip in the second month. Find possible correlations."
    chimera_ai.task(f"Process the following data description and identify potential causal links: {data_description}")

    # Task 3: Routed to CSM (Creative Synthesis Module)
    # The CSM will act as a creative writer.
    chimera_ai.task("Generate a short story concept about an AI that discovers a new law of physics.")


if __name__ == "__main__":
    run_demonstration()
