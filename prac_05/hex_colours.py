"""
Hex Colour Lookup
Estimate: 25 minutes
Actual:   TODO
"""

# 10+ common colour names (case-insensitive lookup)
NAME_TO_HEX = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUAMARINE": "#7fffd4",
    "AZURE": "#f0ffff",
    "BEIGE": "#f5f5dc",
    "BLACK": "#000000",
    "BLUEVIOLET": "#8a2be2",
    "CADETBLUE": "#5f9ea0",
    "CORNFLOWERBLUE": "#6495ed",
    "DARKGREEN": "#006400",
    "FIREBRICK": "#b22222",
}


def main():
    print("Hex colour code lookup (blank to quit)")
    while True:
        name = input("Colour name: ").strip()
        if name == "":
            break
        key = name.upper()
        code = NAME_TO_HEX.get(key)
        if code:
            print(code)
        else:
            print("Invalid colour name")


if __name__ == "__main__":
    main()
