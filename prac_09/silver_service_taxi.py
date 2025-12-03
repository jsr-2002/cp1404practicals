"""
CP1404/CP5632 Practical
SilverServiceTaxi class
A specialised Taxi with fanciness multiplier and flagfall.
"""

from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised Taxi that includes flagfall and fanciness multiplier."""

    flagfall = 4.50   # ✔ class variable

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness

        # ✔ instance-level price_per_km (Taxi.price_per_km * fanciness)
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return string representation including flagfall."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """
        Return fare including:
        - base fare from Taxi (rounded to nearest 10c)
        - plus flagfall
        """
        return super().get_fare() + self.flagfall
