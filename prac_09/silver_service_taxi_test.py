"""
CP1404/CP5632 Practical
SilverServiceTaxi test file
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi fare calculations."""
    taxi = SilverServiceTaxi("Limo", 100, 2)  # fanciness 2
    taxi.drive(18)

    expected_fare = 48.8  # from prac instructions
    actual_fare = taxi.get_fare()

    print(taxi)
    print(f"Fare for 18km: ${actual_fare:.2f}")

    assert actual_fare == expected_fare, "Fare calculation is incorrect"


main()
