# main.py
# The primary entry point for initializing and interacting with the Project Chimera AI.

from src.chimera_core import Chimera

def run_demonstration():
    """
    Initializes the Chimera system and runs a series of demonstration tasks
    to showcase its new capability-based routing.
    """
    # Initialize the Chimera AI system
    chimera_ai = Chimera()

    # --- Task Demonstration ---
    
    # Task 1: The CRC will identify the 'code' and 'analysis' keywords
    # and route this to the ASM based on its reported capabilities.
    chimera_ai.task("Analyze this Python code snippet for vulnerabilities and suggest optimizations.")
    
    # Task 2: The CRC will identify 'satellite' and 'data' and route
    # this to the SFE.
    chimera_ai.task("Process real-time satellite imagery and weather data to find correlations.")

    # Task 3: The CRC will find the 'simulation' capability in the PSE.
    chimera_ai.task("Run a market forecast simulation based on new trade policies.")

    # Task 4: The CRC will find the 'creative' capability in the CSM.
    chimera_ai.task("Generate three novel concepts for a story about AI.")

    # Task 5: A complex task the CRC will realize requires multiple modules.
    chimera_ai.task("Analyze this scientific paper, run a simulation of its findings, and generate a creative visualization of the results.")


if __name__ == "__main__":
    run_demonstration()
