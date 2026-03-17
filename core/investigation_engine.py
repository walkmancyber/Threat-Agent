from modules.virustotal import vt_lookup
from modules.abuseipdb import abuse_lookup
from modules.shodan_lookup import shodan_lookup
from modules.greynoise import greynoise_lookup

from core.correlation_engine import correlate_data
from core.risk_engine import calculate_risk
from ai.llama_agent import llama_analysis
from core.ioc_engine import discover_iocs

"""
Investigation Engine

Main orchestrator responsible for running the threat intelligence
investigation pipeline.
"""

def run_investigation(target):
    """
    Run the full investigation pipeline.
    """

    print("[*] Collecting threat intelligence...")

    vt = vt_lookup(target)
    abuse = abuse_lookup(target)
    shodan = shodan_lookup(target)
    greynoise = greynoise_lookup(target)

    intel = {
        "target": target,
        "virustotal": vt,
        "abuseipdb": abuse,
        "shodan": shodan,
        "greynoise": greynoise
    }

    correlation = correlate_data(intel)

    risk = calculate_risk(intel)

    analysis = llama_analysis(intel, risk)

    # IOC discovery
    discovered_iocs = discover_iocs(intel)

    return {
        "target": target,
        "intel": intel,
        "correlation": correlation,
        "risk": risk,
        "analysis": analysis,
        "discovered_iocs": discovered_iocs
    }