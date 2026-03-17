from modules.virustotal import vt_lookup
from modules.abuseipdb import abuse_lookup
from modules.shodan_lookup import shodan_lookup
from modules.greynoise import greynoise_lookup

from core.correlation_engine import correlate_data
from core.risk_engine import calculate_risk
from core.ioc_engine import discover_iocs
from core.recursive_engine import recursive_investigation

from ai.llama_agent import llama_analysis


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

    # Recursive investigation
    recursive_results = recursive_investigation(discovered_iocs)

    return {
        "target": target,
        "intel": intel,
        "correlation": correlation,
        "risk": risk,
        "analysis": analysis,
        "discovered_iocs": discovered_iocs,
        "recursive": recursive_results
    }
