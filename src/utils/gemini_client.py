# src/utils/gemini_client.py
# A centralized client for interacting with the Google Gemini API.

import google.generativeai as genai
import config
from .logger import log

class GeminiClient:
    """Handles all communication with the Gemini API."""
    
    def __init__(self):
        log("GeminiClient", "Initializing Gemini client...")
        try:
            genai.configure(api_key=config.API_KEY)
            self.model = genai.GenerativeModel('gemini-1.5-pro')
            self.generation_config = config.GEMINI_MODEL_CONFIG
            log("GeminiClient", "Gemini client configured successfully.")
        except Exception as e:
            log("GeminiClient", f"FATAL: Failed to configure Gemini API. Check your API key. Error: {e}", level="ERROR")
            self.model = None

    def generate(self, specialized_prompt):
        """
        Sends a prompt to the Gemini API and returns the response.
        
        Args:
            specialized_prompt (str): A detailed, role-playing prompt crafted by an SCM.

        Returns:
            str: The text response from the Gemini API, or an error message.
        """
        if not self.model:
            return "Error: Gemini client is not initialized. Please check your API key."

        try:
            log("GeminiClient", "Sending request to Gemini API...")
            response = self.model.generate_content(
                specialized_prompt,
                generation_config=self.generation_config
            )
            log("GeminiClient", "Response received successfully.")
            return response.text
        except Exception as e:
            log("GeminiClient", f"API call failed. Error: {e}", level="ERROR")
            # Check for specific quota errors
            if "quota" in str(e).lower():
                return "API Error: You have exceeded your usage quota. Please check your plan and billing details."
            return f"API Error: {e}"

# Create a single, shared instance of the client to be used by all modules
gemini_client = GeminiClient()
