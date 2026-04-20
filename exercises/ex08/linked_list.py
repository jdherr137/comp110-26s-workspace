"""EX08 - Linked List Utility Functions."""

from __future__ import annotations

__author__ = "730748032"


class Node:
    """Node in a singly-linked list recursive structure."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        """Initialize a Node with a value and a reference to the next node."""
        self.value = value
        self.next = next

    def __str__(self) -> str:
        """Return a string representation of the linked list from this node."""
        if self.next is None:
            return f"{self.value} -> None"
        else:
            return f"{self.value} -> {self.next}"


def value_at(head: Node | None, index: int) -> int:
    """Return value at index in list. Raise IndexError if index is out of range."""
    if head is None:
        raise IndexError
    if index == 0:
        return head.value

    return value_at(head.next, index - 1)


def max(head: Node | None) -> int:
    """Return maximum value in the list. Raise ValueError if empty."""
    if head is None:
        raise ValueError

    if head.next is None:
        return head.value

    rest_max = max(head.next)

    if head.value > rest_max:
        return head.value

    return rest_max


def linkify(items: list[int]) -> Node | None:
    """Convert list to linked list."""
    if items == []:
        return None
    else:
        return Node(items[0], linkify(items[1:]))


def scale(head: Node | None, factor: int) -> Node | None:
    """Return new list with values scaled by factor."""
    if head is None:
        return None
    else:
        return Node(head.value * factor, scale(head.next, factor))
