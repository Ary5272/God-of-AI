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
