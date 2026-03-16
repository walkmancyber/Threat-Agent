import requests


OLLAMA_URL = "http://localhost:11434/api/generate"


def llama_analysis(intel, risk):

    prompt = f"""
You are a SOC Threat Intelligence Analyst.

Target: {intel['target']}

VirusTotal: {intel['virustotal']}
AbuseIPDB: {intel['abuseipdb']}
Shodan: {intel['shodan']}

Risk Score: {risk}

Provide:
1. Threat assessment
2. Possible attack scenarios
3. MITRE ATT&CK mapping
4. Security recommendations
"""

    payload = {
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    return response.json()["response"]
