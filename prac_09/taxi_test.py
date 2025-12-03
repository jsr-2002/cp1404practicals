"""
CP1404/CP5632 Practical
Taxi test file
"""

from prac_09.taxi import Taxi


def main():
    """Test the Taxi class."""
    taxi = Taxi("Prius 1", 100)

    taxi.drive(40)
    print(taxi)
    print(f"Fare: ${taxi.get_fare():.2f}")

    taxi.start_fare()
    taxi.drive(100)
    print(taxi)
    print(f"Fare: ${taxi.get_fare():.2f}")


main()
