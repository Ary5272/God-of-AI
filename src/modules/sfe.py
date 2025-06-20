# src/modules/sfe.py
# Functional implementation of the Sensory Fusion Engine.

from .base_module import SpecializedCognitiveModule

class SensoryFusionEngine(SpecializedCognitiveModule):
    """
    SCM specializing in processing and finding correlations in data descriptions.
    It acts as a data scientist.
    """
    def __init__(self):
        super().__init__("SFE", "Sensory Fusion Engine (Data Ingestion & Correlation)")

    def get_capabilities(self):
        """Reports this module's skills to the CRC."""
        return {'data', 'dataset', 'process', 'correlations', 'sales', 'traffic', 'marketing', 'find'}

    def construct_prompt(self, user_query):
        """Constructs a prompt that tells Gemini to act as a data scientist."""
        core_request = user_query.replace("Process the following data description and identify potential causal links:", "").strip()

        prompt = f"""
        **Persona:** You are a senior data scientist with expertise in business intelligence and statistical analysis.

        **Context:** You have been given a high-level summary of a dataset and a key business problem. You do not have the raw data, so you must reason based on the description provided.

        **Data Description:**
        "{core_request}"

        **Instructions:**
        1.  Formulate three distinct, plausible hypotheses that could explain the described situation (e.g., the sales dip).
        2.  For each hypothesis, explain the potential causal link between the variables (e.g., "Hypothesis 1: The sales dip could be caused by a reduction in marketing spend, leading to lower website traffic and thus fewer conversions.").
        3.  Suggest what specific data points or charts you would need to see from the raw data to prove or disprove each of your hypotheses.
        4.  Provide a concluding summary of the most likely cause.
        """
        return prompt
