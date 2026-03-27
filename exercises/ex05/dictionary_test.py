"""EX06 - Dictionary Unit Tests."""

__author__ = "730748032"

from exercises.ex05.dictionary import (
    invert,
    favorite_color,
    count,
    alphabetizer,
    update_attendance,
)
import pytest


def test_invert_use() -> None:
    """Basic invert of normal values."""
    assert invert({"a": "1", "b": "2"}) == {"1": "a", "2": "b"}


def test_invert_use_1() -> None:
    """Test for one key-value pair."""
    assert invert({"x": "y"}) == {"y": "x"}


def test_invert_error() -> None:
    """Duplicate values should raise KeyError."""
    with pytest.raises(KeyError):
        invert({"a": "z", "b": "z"})


def test_favorite_color_use() -> None:
    """Most common color is returned."""
    assert favorite_color({"Alice": "blue", "Bob": "red", "Charlie": "blue"}) == "blue"


def test_favorite_color_use_1() -> None:
    """Only one input."""
    assert favorite_color({"Alice": "blue"}) == "blue"


def test_favorite_color_edge() -> None:
    """Returns first color when a tie occurs."""
    assert favorite_color({"Alice": "blue", "Bob": "red"}) == "blue"


def test_count_use() -> None:
    """Counts repated values correctly."""
    assert count(["a", "b", "a"]) == {"a": 2, "b": 1}


def test_count_use_1() -> None:
    """Empty list returns empty dictionary."""
    assert count([]) == {}


def test_count_use_edge() -> None:
    """Single item list."""
    assert count(["z"]) == {"z": 1}


def test_alphabetizer_use() -> None:
    """Groups words by first letter."""
    assert alphabetizer(["apple", "banana", "apricot"]) == {
        "a": ["apple", "apricot"],
        "b": ["banana"],
    }


def test_alphabetizer_use_1() -> None:
    """Handles uppercase letters correctly."""
    assert alphabetizer(["Apple", "Banana", "Apricot"]) == {
        "a": ["Apple", "Apricot"],
        "b": ["Banana"],
    }


def test_alphabetizer_edge() -> None:
    """Test that non-letter starting words are ignored."""
    result = alphabetizer(["#hash", "apple", "1"])

    assert "a" in result
    assert result["a"] == ["apple"]

    assert "#" not in result
    assert "1" not in result


def test_update_attendance_use() -> None:
    """Adds new day with student."""
    att = {}
    update_attendance(att, "Monday", "Alice")
    assert att == {"Monday": ["Alice"]}


def test_update_attendance_use_1() -> None:
    """Adds student to existing day."""
    att = {"Monday": ["Alice"]}
    update_attendance(att, "Monday", "Bob")
    assert att == {"Monday": ["Alice", "Bob"]}


def test_update_attendance_edge() -> None:
    """Does not add duplicate student."""
    att = {"Monday": ["Alice"]}
    update_attendance(att, "Monday", "Alice")
