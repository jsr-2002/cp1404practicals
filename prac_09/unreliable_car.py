"""
CP1404/CP5632 Practical
UnreliableCar class
Derived from Car with reliability-based driving.
"""

import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Car that sometimes does not drive depending on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise with reliability 0–100."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """
        Drive only if a random number < reliability.
        Must return distance driven (0 if it 'fails').
        """
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
