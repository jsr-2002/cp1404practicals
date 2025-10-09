import random

NUMBERS_PER_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Generate quick pick lottery numbers."""
    quick_picks_count = int(input("How many quick picks? "))
    for _ in range(quick_picks_count):
        pick = generate_quick_pick()
        print(" ".join(f"{num:2}" for num in pick))


def generate_quick_pick():
    """Generate a single line of 6 sorted, unique random numbers."""
    numbers = []
    while len(numbers) < NUMBERS_PER_PICK:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers


main()
