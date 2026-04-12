"""EX08 - Linked List Utility Functions"""

__author__ = "730748032"

# from __future__ import annotations


class Node:
    """Node in a singly-linked list recursive structure."""

    value: int
    next: Node | None

    def __init__(self, value: int, next: Node | None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        if self.next is None:
            return f"{self.value} -> None"

        else:

            return f"{self.value} -> {self.next}"


courses: Node = Node(110, Node(210, Node(211, None)))
print(courses)
