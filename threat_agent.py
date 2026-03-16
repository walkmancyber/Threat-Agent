import sys

from utils.validators import validate_target
from core.investigation_engine import run_investigation
from utils.reporter import print_report


def main():

    if len(sys.argv) < 2:
        print("Usage: python threat_agent.py <IP|domain|URL>")
        sys.exit(1)

    target = sys.argv[1]

    if not validate_target(target):
        print("Invalid target")
        sys.exit(1)

    result = run_investigation(target)

    print_report(result)


if __name__ == "__main__":
    main()