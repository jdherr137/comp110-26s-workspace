"""EX05 - Dictionary Utility Functions."""

__author__ = "730748032"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Invert the keys and values of a dictionary."""
    result: dict[str, str] = {}
    for key in dictionary:
        value = dictionary[key]
        if value in result:
            raise KeyError("invert is not a vaild dictionary")
        result[value] = key
    return result


def favorite_color(favorites: dict[str, str]) -> str:
    """Return the most popular favorite color."""
    colors: dict[str, int] = {}
    for name in favorites:
        color = favorites[name]
        if color in colors:
            colors[color] = colors[color] + 1
        else:
            colors[color] = 1

    best_color: str = ""
    best_count: int = 0
    for color in colors:
        if colors[color] > best_count:
            best_count = colors[color]
            best_color = color
    return best_color


def count(values: list[str]) -> dict[str, int]:
    """Count how many times a value appears in a list."""
    result: dict[str, int] = {}
    for value in values:
        if value in result:
            result[value] = result[value] + 1
        else:
            result[value] = 1
    return result


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Group words by their first letter."""
    result: dict[str, list[str]] = {}

    for word in words:
        first = word[0].lower()

        if first in result:
            result[first].append(word)
        else:
            result[first] = [word]

    return result


def update_attendance(att: dict[str, list[str]], day: str, student: str) -> None:
    """Update the attendance log with a student's name."""
    if day not in att:
        att[day] = [student]
    else:
        if student not in att[day]:
            att[day].append(student)
