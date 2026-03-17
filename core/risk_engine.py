"""
Risk Scoring Engine

Calculates threat risk score based on multiple intelligence sources.
"""


def calculate_risk(intel):

    score = 0

    vt = intel.get("virustotal", {})
    abuse = intel.get("abuseipdb", {})
    shodan = intel.get("shodan", {})
    greynoise = intel.get("greynoise", {})

    vt_detections = vt.get("detections", 0)
    abuse_reports = abuse.get("reports", 0)
    abuse_confidence = abuse.get("confidence", 0)
    ports = shodan.get("open_ports", [])
    gn_class = greynoise.get("classification")

    # VirusTotal detections
    score += vt_detections * 10

    # AbuseIPDB reports
    score += abuse_reports * 2

    # Abuse confidence
    score += abuse_confidence * 0.5

    # Exposed services
    score += len(ports) * 3

    # GreyNoise malicious scanner
    if gn_class == "malicious":
        score += 30

    if score >= 90:
        return "CRITICAL"

    if score >= 60:
        return "HIGH"

    if score >= 30:
        return "MEDIUM"

    return "LOW"