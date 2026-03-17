"""
Prompt Engine

Builds structured prompts for the LLM threat analysis.
"""


def build_prompt(intel, risk, correlation=None, recursive=None):
    """
    Build a structured prompt for LLM analysis.
    """

    prompt = f"""
You are a senior cybersecurity analyst working in a SOC (Security Operations Center).

Analyze the following threat intelligence data and provide a professional assessment.

TARGET:
{intel.get("target")}

RISK SCORE:
{risk}

THREAT INTELLIGENCE DATA:

VirusTotal:
{intel.get("virustotal")}

AbuseIPDB:
{intel.get("abuseipdb")}

Shodan:
{intel.get("shodan")}

GreyNoise:
{intel.get("greynoise")}

CORRELATION ANALYSIS:
{correlation}

RECURSIVE INVESTIGATION:
{recursive}

---

Provide your analysis in the following structured format:

1. Executive Summary
2. Threat Assessment
3. Key Findings
4. Hypotheses (possible attacker behavior)
5. MITRE ATT&CK Mapping (if applicable)
6. Risk Justification
7. Recommended Actions

Be precise, technical, and avoid generic statements.
"""

    return prompt