"""Tea Party-ex01"""

__author__ = "730748032"


def main_planner(guests: int) -> None:
    """total people input, returns all functions"""
    print("Tea Bags:", tea_bags(guests))
    print("Treats:", treats(guests))
    print("Cost: $", cost(tea_bags(guests), treats(guests)))


def tea_bags(people: int) -> int:
    """tea bags needed based on people"""
    return people * 2


def treats(people: int) -> int:
    """Amount of treats needed for people"""
    return int(tea_bags(people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """cost calc"""
    return float((tea_count * 0.50) + (treat_count * 0.75))


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
