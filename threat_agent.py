"""
Threat Agent CLI

Entry point for the Autonomous Threat Intelligence Agent.
Handles CLI input and triggers the investigation pipeline.
"""

import sys

from utils.validators import validate_target
from core.investigation_engine import run_investigation
from utils.reporter import print_report


def main():
    """
    Main CLI entry point.
    """

    if len(sys.argv) < 2:
        print("Usage: python threat_agent.py <IP|domain|URL>")
        sys.exit(1)

    target = sys.argv[1]

    print(f"[+] Target received: {target}")

    # Validate target
    if not validate_target(target):
        print("[!] Invalid target format")
        sys.exit(1)

    try:
        result = run_investigation(target)

        print_report(result)

    except Exception as e:

        print("[!] Investigation failed")
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()