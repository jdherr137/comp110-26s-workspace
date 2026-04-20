# unit test
from __future__ import annotations


# example
def find_even(nums: list[int]) -> int:
    idx: int = 0
    while idx < len(nums):
        if nums[idx] % 2 == 0:
            return idx
        idx += 1
    return -1


# test
def test_find_even() -> None:
    nums = [1, 3, 5, 4, 7]
    assert find_even(nums) == 3


def test_find_even1() -> None:
    nums = [-1, 2, 3, 5, -7]
    assert find_even(nums) == 1


def test_find_even2() -> None:
    nums = []
    assert find_even(nums) == -1


# next one
def sum_numbers(numbers: list[int]) -> int:
    if len(numbers) == 0:
        raise Exception("Empty list - no elements to add")

    total: int = numbers[0]
    for i in range(1, len(numbers)):
        total += numbers[i]

    return total


# tests
def test_sum_numbers_use_case() -> None:
    numbers = [1, 2, 3, 4]
    assert sum_numbers(numbers) == 10


def test_sum_numbers_edge_case1() -> None:
    numbers = [1, -1, 2, -2]
    assert sum_numbers(numbers) == 0


def test_sum_numbers_use_case2() -> None:
    numbers = [10]
    assert sum_numbers(numbers) == 10


# next example


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# tests
def test_is_prime_use_case() -> None:
    assert is_prime(1) is False


def test_is_prime_use_case2() -> None:
    assert is_prime(7)


def test_is_prime_use_case3() -> None:
    assert not is_prime(8)


# harder shit
def add_key_to_dicts(dicts: list[dict], key: str, value: int) -> None:
    for d in dicts:
        d[key] = value


# test
def test_add_key_to_dicts_use_case() -> None:
    dicts: list[dict] = [{"a": 1}, {"b": 2}]
    add_key_to_dicts(dicts, "c", 3)
    assert dicts == [{"a": 1, "c": 3}, {"b": 2, "c": 3}]


# more shit
def increment_dict_value(d: dict[str, int], key: str) -> None:
    if key in d:
        d[key] += 1
    else:
        d[key] = 1


# more test
def test_increment_dict_value_use_case() -> None:
    d = {"a": 1, "b": 2}
    increment_dict_value(d, "a")
    assert d["a"] == 2
    increment_dict_value(d, "b")
    assert d["b"] == 3
    increment_dict_value(d, "c")
    assert d["c"] == 1


# number 11
def max_sum_dict(d: dict[str, list[int]]) -> str:
    keys = []
    for key in d:
        keys.append(key)

    values_list_1 = d[keys[0]]
    values_list_2 = d[keys[1]]

    total_1 = 0
    for value in values_list_1:
        total_1 += value

    total_2 = 0
    for value in values_list_2:
        total_2 += value

    if total_1 > total_2:
        return keys[0]
    else:
        return keys[1]


# test for 11
def test_max_sum_dict_use_case() -> None:
    d = {"a": [1, 2, 3], "b": [1, 2, 3, 4]}
    assert max_sum_dict(d) == "b"


# 12
def divide_list(input_list: list[int], divisor: int) -> list[float]:
    result: list[float] = []

    for num in input_list:
        result.append(num / divisor)

    return result


# test


def test_divide_list() -> None:
    input_list = [10, 20, 30, 40]
    divisor = 10
    assert divide_list(input_list, divisor) == [1, 2, 3, 4]


# these are recursion but who cares
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


# from test


class my_class:
    h: int
    i: float

    def __init__(self, h: int, i: float):
        self.h = h
        self.i = i

    def foo(self, i: int) -> None:
        self.i = self.h / i


h: int = 1
i: float = 2.0
j: my_class = my_class(h, i)
j.foo(h)
print(j.i)
