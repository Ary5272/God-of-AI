# src/chimera_core.py
# Core classes updated to route tasks to functional, AI-powered modules.

import time
import threading
import config
from src.utils.logger import log

# Import all module classes to allow for dynamic loading
from src.modules import *

class MetacognitiveLayer:
    """The 'overseer' AI. It monitors the entire system's performance."""
    def __init__(self, chimera_instance):
        log("MetacognitiveLayer", "Initialized. Overseeing system.")
        self.system = chimera_instance

class CausalReasoningCore:
    """The "Consciousness" of Chimera. Uses capability-based routing."""
    def __init__(self, chimera_instance):
        log("CausalReasoningCore", "CRC online. Awaiting tasks.")
        self.system = chimera_instance

    def find_best_module(self, task_prompt):
        """Finds the best module for a task based on keyword matching against capabilities."""
        best_module = None
        highest_match_score = 0
        task_keywords = set([word.strip(",.!?") for word in task_prompt.lower().split()])
        
        log("CausalReasoningCore", f"Searching for best module to handle task...")
        
        for module in self.system.modules.values():
            capabilities = module.get_capabilities()
            match_score = len(task_keywords & set(capabilities))
            
            if match_score > highest_match_score:
                highest_match_score = match_score
                best_module = module
        
        return best_module

    def process_task(self, task_prompt):
        """Analyzes a task and delegates it to the best functional SCM."""
        log("CausalReasoningCore", f"Received new task: '{task_prompt}'", header=True)
        
        # Capability-Based Routing
        chosen_module = self.find_best_module(task_prompt)

        if chosen_module:
            log("CausalReasoningCore", f"Best match found. Delegating to '{chosen_module.name}'.")
            result = chosen_module.execute(task_prompt)
        else:
            log("CausalReasoningCore", "No specialized module found. Using general reasoning via default module.", level="WARN")
            default_module = self.system.get_module("CSM") # Default to creative for general queries
            result = default_module.execute(task_prompt)

        log("CausalReasoningCore", "Task complete. Displaying final response:", header=True)
        print(result) # Print the final AI response cleanly
        return result

class Chimera:
    """The main class that orchestrates the entire AI system."""
    def __init__(self):
        log("Chimera", "--- Project Chimera Initializing ---", header=True)
        self.modules = {}
        self.core = CausalReasoningCore(self)
        self.metacognitive_layer = MetacognitiveLayer(self)
        self._load_initial_modules()
        log("Chimera", "--- System Online. Ready for interaction. ---\n", header=True)

    def _load_initial_modules(self):
        """Loads the set of functional Specialized Cognitive Modules."""
        log("Chimera", "Loading functional SCMs...")
        self.add_module(AbstractSymbologyModule())
        self.add_module(SensoryFusionEngine())
        self.add_module(CreativeSynthesisModule())

    def add_module(self, module_instance):
        """Adds a new module to the system."""
        self.modules[module_instance.name] = module_instance

    def get_module(self, module_name):
        """Retrieves an active module by its name."""
        return self.modules.get(module_name, None)

    def task(self, prompt):
        """The primary interface for giving Chimera a task."""
        self.core.process_task(prompt)
