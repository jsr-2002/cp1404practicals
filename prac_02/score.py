"""Score grading program with functions."""

import random


def main():
    """Get a score and print its result, then test with random score."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(result)

    # Generate random score
    random_score = random.randint(0, 100)
    print(f"Random score: {random_score} -> {determine_result(random_score)}")


def determine_result(score):
    """Determine grade based on score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
