def calculate_risk(intel):

    findings = []

    if intel["virustotal"]["detections"] > 0:
        findings.append("Detected by antivirus engines")

    if intel["abuseipdb"]["reports"] > 0:
        findings.append("IP reported for abuse")

    if intel["shodan"]["open_ports"]:
        findings.append("Exposed services detected")

    if intel["greynoise"]["classification"] == "malicious":
        findings.append("Known malicious internet scanner")

    return findings