import requests

from ai.prompt_engine import build_threat_prompt

OLLAMA_URL = "http://localhost:11434/api/generate"


def llama_analysis(intel, risk):

    prompt = build_threat_prompt(intel, risk)

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    return response.json()["response"]