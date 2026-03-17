from unittest import result


def print_report(result):

    print("\n=== Threat Intelligence Investigation ===\n")

    print(f"Target: {result['target']}\n")

    print("Risk Score:", result["risk"])

    print("\nCorrelation Findings:")

    for finding in result["correlation"]:
        print("-", finding)

    print("\nLLM Threat Analysis:\n")

    print(result["analysis"])

    print("\nDiscovered IOCs:")

    for ioc in result.get("discovered_iocs", []):
        print(f"- {ioc['type']}: {ioc['value']}")

    print("\nRecursive Investigation:")

    for target, data in result.get("recursive", {}).items():
        print(f"- {target} (depth {data.get('depth')})")
