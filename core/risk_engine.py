def calculate_risk(intel):

    score = 0

    vt = intel["virustotal"]
    abuse = intel["abuseipdb"]

    if vt["detections"] > 0:
        score += vt["detections"] * 10

    if abuse["reports"] > 0:
        score += abuse["reports"] * 2

    if score >= 80:
        return "CRITICAL"

    if score >= 50:
        return "HIGH"

    if score >= 20:
        return "MEDIUM"

    return "LOW"