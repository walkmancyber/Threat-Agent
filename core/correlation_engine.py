def correlate_data(intel):

    findings = []

    if intel["virustotal"]["detections"] > 0:
        findings.append("Detected by antivirus engines")

    if intel["abuseipdb"]["reports"] > 0:
        findings.append("Reported abusive IP")

    if intel["shodan"]["open_ports"]:
        findings.append("Exposed services detected")

    return findings
