"""
IOC Discovery Engine

Extracts new indicators of compromise from intelligence data.
"""


def discover_iocs(intel):
    """
    Discover additional IOCs from collected intelligence.
    """

    discovered = []

    shodan_data = intel.get("shodan", {})
    hostnames = shodan_data.get("hostnames", [])

    for host in hostnames:
        discovered.append({
            "type": "domain",
            "value": host
        })

    return discovered