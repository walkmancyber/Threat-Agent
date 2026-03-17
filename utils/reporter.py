def print_report(result):

    print("\n=== Threat Intelligence Investigation ===\n")

    print(f"Target: {result['target']}\n")

    print("Risk Score:", result.get("risk", "Unknown"))

    print("\nCorrelation Findings:")

    for finding in result.get("correlation", []):
        print("-", finding)

    print("\nLLM Threat Analysis:\n")

    analysis = result.get("analysis")
    if analysis:
        print(analysis)
    else:
        print("No analysis generated.")

    print("\nDiscovered IOCs:")

    for ioc in result.get("discovered_iocs", []):
        print(f"- {ioc['type']}: {ioc['value']}")

    print("\nRecursive Investigation:")

    for target, data in result.get("recursive", {}).items():
        print(f"- {target} (depth {data.get('depth')})")