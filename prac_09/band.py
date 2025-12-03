"""
CP1404/CP5632 Practical
Band class using association (has-a relationship).
"""


class Band:
    """Band has musicians."""

    def __init__(self, name):
        """Initialise Band with band name and empty musician list."""
        self.name = name
        self.musicians = []

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def __str__(self):
        """Return string representation."""
        musicians_str = ", ".join(str(m) for m in self.musicians)
        return f"{self.name} ({musicians_str})"

    def play(self):
        """Tell each musician to play."""
        for musician in self.musicians:
            print(musician.play())
