"""
State Names
Estimate: 20 minutes
Actual:   TODO
"""

# Constant dictionary of Australian state abbreviations to names
STATE_TO_NAME = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "SA": "South Australia",
    "VIC": "Victoria",
    "TAS": "Tasmania",
    "ACT": "Australian Capital Territory",
}


def main():
    print("State name lookup")
    # Loop to allow repeated lookups until blank
    while True:
        short_state = input("Enter short state (blank to quit): ").strip()
        if short_state == "":
            break

        # Make input case-insensitive
        short_state = short_state.upper()

        # EAFP: Try to get; handle KeyError if missing
        try:
            print(f"{short_state} is {STATE_TO_NAME[short_state]}")
        except KeyError:
            print("Invalid short state")

    print()
    print("All states:")
    # Neatly aligned listing
    # Widest key length (should be 3 for AUS states)
    max_key = max(len(k) for k in STATE_TO_NAME)
    for abbr, name in STATE_TO_NAME.items():
        print(f"{abbr:{max_key}} is {name}")


if __name__ == "__main__":
    main()
