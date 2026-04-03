"""File to define River class."""

from __future__ import annotations
from exercises.ex07.fish import Fish
from exercises.ex07.bear import Bear

__author__ = "730748032"


class River:
    """Simulate a river ecosystem containing fish and bears."""

    day: int
    fish: list[Fish]
    bears: list[Bear]

    def __init__(self, num_fish: int, num_bears: int):
        """Initialize a River with the given number of fish and bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Remove fish older than 3 and bears older than 5 from the river."""
        self.fish = [f for f in self.fish if f.age <= 3]
        self.bears = [b for b in self.bears if b.age <= 5]
        return None

    def remove_fish(self, amount: int):
        """Remove the specified number of fish from the front of the river."""
        remove_count = min(amount, len(self.fish))  # cannot remove more than we have
        for _ in range(remove_count):
            self.fish.pop(0)

    def bears_eating(self):
        """Allow each bear to eat 3 fish if there are at least 5 fish in the river."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        """Remove bears whose hunger_score is below 0."""
        self.bears = [b for b in self.bears if b.hunger_score >= 0]
        return None

    def repopulate_fish(self):
        """Each pair of fish produces 4 new fish in the river."""
        num_new_fish = (len(self.fish) // 2) * 4
        for _ in range(num_new_fish):
            self.fish.append(Fish())
        return None

    def repopulate_bears(self):
        """Each pair of bears produces 1 new bear in the river."""
        num_new_bears = len(self.bears) // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear())
        return None

    def __str__(self) -> str:
        """Return a string representation of the river's day and populations."""
        return (
            f"~~~ Day {self.day}: ~~~\n"
            f"Fish population: {len(self.fish)}\n"
            f"Bear population: {len(self.bears)}"
        )

    def __add__(self, other_riv: River) -> River:
        """Combine two rivers into a new river with summed populations."""
        total_fish = len(self.fish) + len(other_riv.fish)
        total_bears = len(self.bears) + len(other_riv.bears)
        return River(total_fish, total_bears)

    def __mul__(self, factor: int) -> River:
        """Return a new River with populations scaled by the given factor."""
        total_fish = len(self.fish) * factor
        total_bears = len(self.bears) * factor
        return River(total_fish, total_bears)

    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        print(self)

    def one_river_week(self):
        """Simulate one week (7 days) in the river."""
        for _ in range(7):
            self.one_river_day()
