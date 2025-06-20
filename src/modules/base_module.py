# src/modules/base_module.py
# Defines the abstract base class for all Specialized Cognitive Modules (SCMs).

from abc import ABC, abstractmethod
from src.utils.logger import log
from src.utils.gemini_client import gemini_client # Import the shared client

class SpecializedCognitiveModule(ABC):
    """
    Abstract Base Class for all expert modules. Requires capabilities and
    an execution method that calls the Gemini API.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        log("SCM_Loader", f"Loaded: {self.name} ({self.description})")

    @abstractmethod
    def get_capabilities(self):
        """Returns a set of keywords representing the module's skills."""
        pass

    @abstractmethod
    def construct_prompt(self, user_query):
        """Constructs a detailed, role-playing prompt for the Gemini API."""
        pass

    def execute(self, user_query):
        """
        Constructs the prompt and sends it to the Gemini client for processing.
        """
        specialized_prompt = self.construct_prompt(user_query)
        log(self.name, "Executing task via Gemini API...")
        response = gemini_client.generate(specialized_prompt)
        return response
