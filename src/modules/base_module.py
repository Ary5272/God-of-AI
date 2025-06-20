# src/modules/base_module.py
# Defines the abstract base class for all Specialized Cognitive Modules (SCMs).

from abc import ABC, abstractmethod
from src.utils.logger import log

class SpecializedCognitiveModule(ABC):
    """
    Abstract Base Class for all expert modules. It now requires all modules
    to report their capabilities.
    """
    def __init__(self, name, description):
        self.name = name
        self.description = description
        log("SCM_Loader", f"Loaded: {self.name} ({self.description})")

    @abstractmethod
    def get_capabilities(self):
        """
        Must be implemented by all subclasses. Returns a list of strings
        representing the module's core skills (e.g., ['code_analysis', 'debugging']).
        """
        pass

    @abstractmethod
    def execute(self, sub_task, data=None):
        """
        The primary function of the module. Takes a specific sub-task and
        optional data, and should return the result of its processing.
        """
        pass
