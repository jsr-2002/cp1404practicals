"""String formatting examples"""

def main():
    # Part 1: guitar example
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.95
    print(f"{year} {name} for about ${cost:,.0f}!")

    # Part 2: powers of 2
    for i in range(11):
        print(f"2 ^ {i:2} is {2 ** i:5}")


main()
