"""File to define Fish class."""

__author__ = "730748032"


class Fish:
    """Represent a fish in a river ecosystem."""

    def __init__(self):
        """Initialize a new Fish with default age."""
        self.age = 0
        return None

    def one_day(self):
        """Simulate one day for the fish."""
        self.age += 1
        return None
