"""
Wimbledon Data Processor
Estimate: 45 minutes
Actual:   TODO
"""

from collections import defaultdict

FILENAME = "wimbledon.csv"


def load_wimbledon_rows(filename: str):
    """Load CSV rows (winner, country, year, runner_up, ...), handling UTF-8 BOM."""
    rows = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        header = in_file.readline().strip().split(",")
        for line in in_file:
            parts = [p.strip() for p in line.strip().split(",")]
            if len(parts) < 4:
                # Expect at least Winner, Country, Year, Runner-up
                continue
            rows.append(parts)
    return rows


def count_champions(rows):
    """Return dict of winner -> count of titles."""
    counts = defaultdict(int)
    for row in rows:
        winner = row[0]
        counts[winner] += 1
    return dict(counts)


def countries_of_champions(rows):
    """Return a set of country codes of all winners."""
    countries = set()
    for row in rows:
        country = row[1]
        countries.add(country)
    return countries


def main():
    rows = load_wimbledon_rows(FILENAME)
    champions = count_champions(rows)
    countries = countries_of_champions(rows)

    print("Wimbledon Champions:")
    # Sort champions by name for a stable, readable list
    for name in sorted(champions.keys()):
        print(f"{name} {champions[name]}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


if __name__ == "__main__":
    main()
