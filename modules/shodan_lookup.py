import requests
from config import SHODAN_API_KEY, REQUEST_TIMEOUT


def shodan_lookup(target):

    url = f"https://api.shodan.io/shodan/host/{target}"

    params = {
        "key": SHODAN_API_KEY
    }

    try:

        response = requests.get(
            url,
            params=params,
            timeout=REQUEST_TIMEOUT
        )

        if response.status_code != 200:
            return {"open_ports": []}

        data = response.json()

        ports = data.get("ports", [])

        return {
            "open_ports": ports,
            "hostnames": data.get("hostnames", []),
            "org": data.get("org", "")
        }

    except Exception:

        return {
            "open_ports": []
        }
