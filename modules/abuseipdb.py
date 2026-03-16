import requests
from config import ABUSEIPDB_API_KEY, REQUEST_TIMEOUT


def abuse_lookup(target):

    url = "https://api.abuseipdb.com/api/v2/check"

    headers = {
        "Key": ABUSEIPDB_API_KEY,
        "Accept": "application/json"
    }

    params = {
        "ipAddress": target,
        "maxAgeInDays": 90
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=REQUEST_TIMEOUT
        )

        if response.status_code != 200:
            return {"reports": 0}

        data = response.json()["data"]

        return {
            "reports": data["totalReports"],
            "confidence": data["abuseConfidenceScore"],
            "country": data["countryCode"]
        }

    except Exception:

        return {
            "reports": 0
        }
