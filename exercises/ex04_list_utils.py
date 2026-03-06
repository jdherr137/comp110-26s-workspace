"""EX04 - List Utility Functions"""

__author__ = "730748032"


def all(input: list[int], value: int) -> bool:
    """return True if every element of xs equals value."""
    if len(input) == 0:
        return False

    index: int = 0
    while index < len(input):
        if input[index] != value:
            return False
        index += 1

    return True


def max(input: list[int]) -> int:
    """return max vaule"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")

    maximum: int = input[0]
    index: int = 1

    while index < len(input):
        if input[index] > maximum:
            maximum = input[index]
        index += 1

    return maximum


def is_equal(L1: list[int], L2: list[int]) -> bool:
    """Return True if xs and ys contain the same values in the same order."""
    if len(L1) != len(L2):
        return False

    index: int = 0
    while index < len(L1):
        if L1[index] != L2[index]:
            return False
        index += 1

    return True


def extend(L1: list[int], L2: list[int]) -> None:
    """Mutate xs by appending elements of ys."""
    index: int = 0
    while index < len(L2):
        L1.append(L2[index])
        index += 1
