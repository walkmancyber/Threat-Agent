"""
Llama Agent

Handles interaction with local LLM (Ollama).
"""

import requests
from ai.prompt_engine import build_prompt


OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "llama3"


def llama_analysis(intel, risk, correlation=None, recursive=None):
    """
    Perform LLM-based threat analysis.
    """

    prompt = build_prompt(intel, risk, correlation, recursive)

    payload = {
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)

        if response.status_code == 200:
            return response.json().get("response", "No response from LLM")

        return f"LLM error: {response.status_code}"

    except Exception as e:
        return f"LLM connection error: {str(e)}"