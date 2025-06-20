# Project Chimera: A Functional, Multi-Persona AI Agent

## 1. Project Objective

Project Chimera has evolved from a conceptual framework into a functional, multi-persona AI agent. It uses a modular architecture to delegate tasks to specialized "personas" that are powered by the Google Gemini Pro API. This creates a system capable of providing expert-level analysis across different domains by adopting the correct context for each query.

---

## 2. Core Architecture: The Functional AI Framework

### A. The Causal Reasoning Core (CRC)
The heart of Chimera. The CRC analyzes user prompts and uses a **Capability-Based Routing** system to delegate the task to the most appropriate AI persona.

### B. Specialized Cognitive Modules (SCMs)
These are no longer placeholders. Each SCM is now a functional "AI Persona" that crafts a highly specialized, role-playing prompt to send to the Gemini API. This ensures the response is not generic, but tailored to the specific domain. Current functional modules include:
- **Abstract Symbology Module (ASM):** Acts as an expert code analyst and mathematician.
- **Sensory Fusion Engine (SFE):** Acts as a data scientist, analyzing and finding patterns in data descriptions.
- **Creative Synthesis Module (CSM):** Acts as a creative director and author, generating novel ideas and stories.

### C. The Metacognitive Layer
The "overseer" layer monitors the system's operations, logging the delegation process and system status.

---

## 3. Setup and Configuration

### 1. Prerequisites
- Python 3.x
- A Google Gemini API key. Get one from [Google AI Studio](https://aistudio.google.com/app/apikey).

### 2. Install Dependencies
Open your terminal and run:
```bash
pip install google-generativeai
3. Configure Your API Key
Open the config.py file.
Find the line API_KEY = "YOUR_API_KEY_HERE".
Replace YOUR_API_KEY_HERE with your actual, secret API key.
IMPORTANT: Do NOT commit your real API key to a public GitHub repository.
4. How to Run
Run the main entry point from your terminal:

Bash

python main.py
The script will initialize the system and run a series of demonstration tasks, printing the live, AI-generated responses to your console.


***

### `config.py`

```python
# config.py
# System-wide configuration settings for Project Chimera.

# --- Gemini API Configuration ---
# IMPORTANT: Replace "YOUR_API_KEY_HERE" with your actual Google Gemini API key.
# This key should be kept secret and should not be committed to public version control.
API_KEY = "YOUR_API_KEY_HERE"

# --- System Configuration ---

# Set the operational mode for the AI
# 'development' - Enables verbose logging and debug information.
# 'production' - Optimized for performance with minimal console output.
OPERATION_MODE = 'development'

# Configuration for the Metacognitive Layer
METACOGNITIVE_CONFIG = {
    "monitoring_interval_seconds": 10,
}

# Configuration for the Gemini Model
GEMINI_MODEL_CONFIG = {
    "temperature": 0.4,
    "top_p": 1,
    "top_k": 32,
    "max_output_tokens": 4096,
}
