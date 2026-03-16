import requests
from config import GREYNOISE_API_KEY, REQUEST_TIMEOUT


def greynoise_lookup(target):

    url = f"https://api.greynoise.io/v3/community/{target}"

    headers = {
        "key": GREYNOISE_API_KEY
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            timeout=REQUEST_TIMEOUT
        )

        if response.status_code != 200:
            return {"classification": "unknown"}

        data = response.json()

        return {
            "classification": data.get("classification"),
            "noise": data.get("noise"),
            "riot": data.get("riot")
        }

    except Exception:

        return {
            "classification": "unknown"
        }
