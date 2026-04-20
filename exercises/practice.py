from __future__ import annotations

# class writing


class Course:
    """Models the idea of a UNC course."""

    name: str
    level: int
    prerequisites: list[str]

    def is_valid_course(self, prereq: str) -> bool:
        """Checks if this course is 400+ level and has the given prereq."""
        if self.level < 400:
            return False
        else:
            for p in self.prerequisites:
                if p == prereq:
                    return True
        return False


def find_course(Courses: list[Course], prereq: str) -> list[str]:
    results: list[str] = []

    for c in Courses:
        if c.level >= 400:
            for p in Courses:
                if p == prereq:
                    results.append(c.name)
    return results


class car:
    make: str
    model: str
    year: int
    color: str
    mileage: float

    def __init__(
        self, make: str, model: str, year: int, color: str, mileage: float
    ) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def update_mileage(self, miles: float) -> None:
        self.mileage += miles

    def info(self) -> None:
        disply_info: str = (
            f"This car's info is {self.make}, {self.model}, "
            f"{self.year}, {self.color}, {self.mileage}"
        )
        print(disply_info)


def calc_depre(vehicle: car, depre_rate: float) -> float:
    value: float = vehicle.mileage * depre_rate
    return value


my_ride = car("porsche", "944", 1982, "red", 200.00)
my_ride.update_mileage(250.00)
my_ride.info
print(my_ride.info)


class Hot_cocoa:
    has_whip: bool
    flavor: str
    marsh_count: int
    sweetness: int

    def __init__(
        self, has_whip: bool, flavor: str, marsh_count: int, sweetness: int
    ) -> None:
        self.has_whip = has_whip
        self.flavor = flavor
        self.marsh_count = marsh_count
        self.sweetness = sweetness

    def mellow_adder(self, mallows: int) -> None:
        self.marsh_count += mallows
        self.sweetness += mallows * 2

    def __str__(self) -> str:
        if self.has_whip:
            return (
                f"A {self.flavor} cocoa with whip, {self.marsh_count} "
                f"marshmallows, and level {self.sweetness} sweetness."
            )
        else:
            return (
                f"A {self.flavor} cocoa without whip, {self.marsh_count} "
                f"marshmallows, and level {self.sweetness} sweetness."
            )


def order_cost(order: list[Hot_cocoa]) -> float:
    cost: float = 0.0

    for c in order:
        if c.has_whip:
            cost += 2.50
        else:
            cost += 2.00
    return cost


my_order = Hot_cocoa(False, "vanilla", 5, 2)
my_order.has_whip = True
my_order.mellow_adder(2)

vik_order = Hot_cocoa(True, "pepermint", 10, 2)

order_cost([my_order, vik_order])


class TimeSpent:
    name: str
    purpose: str
    minutes: int

    def __init__(self, name: str, purpose: str, minutes: int) -> None:
        self.name = name
        self.purpose = purpose
        self.minutes = minutes

    def add_time(self, add: int) -> None:
        self.minutes += add

    def __add__(self, added_minutes: int) -> "TimeSpent":
        return TimeSpent(self.name, self.purpose, self.minutes + added_minutes)

    def reset(self) -> int:
        old_val = self.minutes
        self.minutes = 0
        return old_val

    def __str__(self) -> str:
        minutes: int = self.minutes % 60
        hours: float = (self.minutes - minutes) / 60
        return (
            f"{self.name} has spent {hours} hours and {minutes} minutes on screen time."
        )


def most_by_purpose(times: list[TimeSpent], activity: str) -> str:
    max_time: int = 0
    max_name: str = ""

    for elem in times:
        if (elem.purpose == activity) and (elem.minutes > max_time):
            max_time = elem.minutes
            max_name = elem.name
    return max_name


# Node class- recusrive


class Node:
    value: int
    next: Node | None

    def __init__(self, val: int, next: Node | None):
        self.value = val
        self.next = next

    def __str__(self) -> str:
        rest: str
        if self.next is None:
            rest = "None"
        else:
            rest = str(self.next)
        return f"{self.value} -> {rest}"

    def append(self, new_val: int) -> None:
        if self.next is None:
            self.next = Node(new_val, None)
        else:
            self.next.append(new_val)

    def get_length(self, count: int) -> int:
        if self.next is None:
            return count + 1
        else:
            return self.next.get_length(count + 1)


def recursive_range(start: int, end: int) -> Node | None:
    if start == end:
        return None
    elif start < end:
        return Node(start, recursive_range(start + 1, end))
    else:
        return Node(start, recursive_range(start - 1, end))
