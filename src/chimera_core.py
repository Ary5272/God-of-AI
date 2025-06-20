# src/chimera_core.py
# Core classes updated to use a capability-based routing system.

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
        self.is_monitoring = True
        self.monitor_thread = threading.Thread(target=self.monitor_performance, daemon=True)
        self.monitor_thread.start()

    def monitor_performance(self):
        """Continuously monitors the system for efficiency and errors."""
        interval = config.METACOGNITIVE_CONFIG['monitoring_interval_seconds']
        while self.is_monitoring:
            time.sleep(interval)
            log("MetacognitiveLayer", f"System nominal. Active Modules: {len(self.system.modules)}. CRC Load: {self.system.core.current_load:.2f}%")

    def analyze_task_delegation(self, task_prompt, chosen_module):
        """Analyzes the CRC's choice of module for a given task."""
        log("MetacognitiveLayer", f"Analyzing CRC choice for task: '{task_prompt}' -> Chose '{chosen_module.name}'")
        # In a real system, this would analyze if a better module existed or if a new one is needed.


class CausalReasoningCore:
    """
    The "Consciousness" of Chimera. Now uses capability-based routing.
    """
    def __init__(self, chimera_instance):
        log("CausalReasoningCore", "CRC online. Awaiting tasks.")
        self.system = chimera_instance
        self.current_load = 0.0

    def find_best_module(self, task_keywords):
        """Finds the best module for a task based on reported capabilities."""
        best_module = None
        highest_match_score = 0
        log("CausalReasoningCore", f"Searching for module with capabilities matching: {task_keywords}")
        
        for module in self.system.modules.values():
            capabilities = module.get_capabilities()
            match_score = len(set(task_keywords) & set(capabilities))
            
            if match_score > highest_match_score:
                highest_match_score = match_score
                best_module = module
        
        return best_module

    def process_task(self, task_prompt):
        """
        Analyzes a task and determines the correct SCMs to use.
        """
        log("CausalReasoningCore", f"Received new task: '{task_prompt}'", header=True)
        self.current_load = 100.0
        
        # Simple keyword extraction from the prompt
        task_keywords = [word.strip(",.!?") for word in task_prompt.lower().split() if len(word) > 3]

        # Capability-Based Routing
        chosen_module = self.find_best_module(task_keywords)

        if chosen_module:
            log("CausalReasoningCore", f"Best match found. Delegating to '{chosen_module.name}'.")
            self.system.metacognitive_layer.analyze_task_delegation(task_prompt, chosen_module)
            result = chosen_module.execute(task_prompt)
        else:
            log("CausalReasoningCore", "No specialized module found. Using general reasoning.")
            result = "Synthesized result from general knowledge base."

        log("CausalReasoningCore", f"Task complete. Final result: '{result}'")
        self.current_load = 0.0
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
        """Loads the default set of Specialized Cognitive Modules."""
        log("Chimera", "Loading initial SCMs...")
        self.add_module(SensoryFusionEngine())
        self.add_module(AbstractSymbologyModule())
        self.add_module(PredictiveSimulationEngine())
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
