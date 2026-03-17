"""
Recursive Investigation Engine

Performs automated recursive threat intelligence expansion.
"""

from utils.validators import validate_target
from modules.virustotal import vt_lookup


def recursive_investigation(discovered_iocs, depth=1, max_depth=2, visited=None):
    """
    Recursively investigate newly discovered IOCs.

    Args:
        discovered_iocs (list): List of IOCs to investigate
        depth (int): Current recursion depth
        max_depth (int): Maximum recursion depth
        visited (set): Already analyzed IOCs

    Returns:
        dict: Recursive investigation results
    """

    if visited is None:
        visited = set()

    if depth > max_depth:
        return {}

    results = {}

    for ioc in discovered_iocs:
        value = ioc.get("value")

        if not value:
            continue

        if value in visited:
            continue

        if not validate_target(value):
            continue

        print(f"[*] Recursive lookup ({depth}): {value}")

        visited.add(value)

        try:
            vt_result = vt_lookup(value)

            results[value] = {
                "depth": depth,
                "virustotal": vt_result
            }

        except Exception as e:
            results[value] = {"error": str(e)}

    return results