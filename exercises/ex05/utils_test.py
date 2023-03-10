"""Unit Testing"""
__author__ = "730529946"

from exercises.ex05.utils import only_evens, concat, sub

def test_empty() -> None:
    "Empty list with only evens."
    assert only_evens([]) == []

def test_concat_empty() -> None:
    """Empty list."""
    assert concat([], []) == []

def even_list() -> None:
    """Returning evens from a list."""
    list1: list[int] = [1, 2, 3, 4]
    assert only_evens(list1) == []

def sub_empty() -> None:
    """Subset empty."""
    assert sub([], 2, 3) == []

def negative_start() -> None:
    """Starting with a negative."""
    list2: list[int] = [1, 2, 3, 4]
    starting: int = -1
    ending: 4
    assert sub(list2, starting, ending) == [1, 2, 3, 4]

def negative() -> None:
    """Negative"""
    list3: list[int] = [-11, -4, -3, 2, 1]
    assert only_evens(list3) == [-11, 10]

def two_lists() -> None:
    """Two list test."""
    list4: list[int] = ([1, 2, 3], [1, 2, 3])
    assert concat(list4) == []

def single_list() -> None:
    """A single list and an empty."""
    list5: list[int] = ([1, 2, 3], [])
    assert concat(list5) == []

def end_negative() -> None:
    """Ending with negative"""
    list6: list[int] = [4, 3, 2, 1]
    starts: int = 4
    ends: int = -1
    assert sub(list6, starts, ends) == [4, 3, 2, 1]