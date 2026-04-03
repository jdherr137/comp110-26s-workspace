"""File to define Bear class."""

__author__ = "730748032"


class Bear:
    """Represent a bear in a river ecosystem."""

    def __init__(self):
        """Initialize a new Bear with default age and hunger_score."""
        self.age = 0
        self.hunger_score = 0
        return None

    def one_day(self):
        """Simulate one day for the bear."""
        self.age += 1
        self.hunger_score -= 1
        return None

    def eat(self, num_fish: int):
        """Increase hunger_score by the number of fish eaten."""
        self.hunger_score += num_fish
