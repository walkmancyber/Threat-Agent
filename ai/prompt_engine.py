"""
Prompt Engine

Builds structured prompts for the LLM threat analysis.
"""


def build_threat_prompt(intel, risk):
    """
    Generate a structured prompt for the LLM analysis.
    """

    target = intel.get("target")

    vt = intel.get("virustotal", {})
    abuse = intel.get("abuseipdb", {})
    shodan = intel.get("shodan", {})
    greynoise = intel.get("greynoise", {})

    prompt = f"""
You are a senior SOC Threat Intelligence Analyst.

Analyze the following investigation results.

Target: {target}

VirusTotal:
detections: {vt.get("detections")}
malicious: {vt.get("malicious")}
suspicious: {vt.get("suspicious")}

AbuseIPDB:
reports: {abuse.get("reports")}
confidence: {abuse.get("confidence")}

Shodan:
open_ports: {shodan.get("open_ports")}
organization: {shodan.get("org")}

GreyNoise:
classification: {greynoise.get("classification")}

Risk Score: {risk}

Tasks:

1. Explain the security risk level.
2. Identify suspicious indicators if any.
3. Suggest possible threat scenarios.
4. Map possible MITRE ATT&CK techniques.
5. Provide security recommendations.
6. Write a short professional summary for a SOC report.
"""

    return prompt