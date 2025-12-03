"""
CP1404/CP5632 Practical
UnreliableCar tests
"""

from prac_09.unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar with multiple drive attempts."""
    test_car = UnreliableCar("Old Bomb", 100, 30)  # 30% reliable
    attempts = 100
    total_driven = 0

    for _ in range(attempts):
        total_driven += test_car.drive(1)

    print(test_car)
    print(f"Drove {total_driven}km out of {attempts} attempts "
          f"(expected roughly ~30).")


main()
