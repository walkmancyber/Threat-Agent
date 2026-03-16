from modules.virustotal import vt_lookup
from modules.abuseipdb import abuse_lookup
from modules.shodan_lookup import shodan_lookup

from core.correlation_engine import correlate_data
from core.risk_engine import calculate_risk

from ai.llama_agent import llama_analysis


def run_investigation(target):

    print("[*] Running threat intelligence queries...")

    vt = vt_lookup(target)
    abuse = abuse_lookup(target)
    shodan = shodan_lookup(target)

    intel = {
        "target": target,
        "virustotal": vt,
        "abuseipdb": abuse,
        "shodan": shodan
    }

    correlation = correlate_data(intel)

    risk = calculate_risk(intel)

    ai_analysis = llama_analysis(intel, risk)

    result = {
        "target": target,
        "intel": intel,
        "correlation": correlation,
        "risk": risk,
        "analysis": ai_analysis
    }

    return result