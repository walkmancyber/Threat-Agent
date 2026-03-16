def calculate_risk(data):

    score = 0

    vt = data["virustotal"]
    abuse = data["abuseipdb"]

    if vt["detections"] > 5:
        score += 50

    if abuse["reports"] > 10:
        score += 30

    if score > 70:
        return "CRITICAL"

    if score > 40:
        return "HIGH"

    if score > 20:
        return "MEDIUM"

    return "LOW"