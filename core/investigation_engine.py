from modules.virustotal import vt_lookup
from modules.abuseipdb import abuse_lookup
from modules.shodan_lookup import shodan_lookup
from modules.greynoise import greynoise_lookup

from core.correlation_engine import correlate_data
from core.risk_engine import calculate_risk
from ai.llama_agent import llama_analysis


def run_investigation(target):

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

    return {
        "target": target,
        "intel": intel,
        "correlation": correlation,
        "risk": risk,
        "analysis": analysis
    }