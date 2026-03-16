import requests
from config import VT_API_KEY, REQUEST_TIMEOUT


def vt_lookup(target):

    url = f"https://www.virustotal.com/api/v3/ip_addresses/{target}"

    headers = {
        "x-apikey": VT_API_KEY
    }

    try:

        response = requests.get(url, headers=headers, timeout=REQUEST_TIMEOUT)

        if response.status_code != 200:
            return {"detections": 0, "error": "VT request failed"}

        data = response.json()

        stats = data["data"]["attributes"]["last_analysis_stats"]

        detections = stats["malicious"] + stats["suspicious"]

        return {
            "detections": detections,
            "malicious": stats["malicious"],
            "suspicious": stats["suspicious"]
        }

    except Exception as e:

        return {
            "detections": 0,
            "error": str(e)
        }
