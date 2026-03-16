def print_report(result):

    print("\n=== Threat Intelligence Investigation ===\n")

    print(f"Target: {result['target']}\n")

    print("Risk Score:", result["risk"])

    print("\nCorrelation Findings:")

    for finding in result["correlation"]:
        print("-", finding)

    print("\nLLM Threat Analysis:\n")

    print(result["analysis"])
