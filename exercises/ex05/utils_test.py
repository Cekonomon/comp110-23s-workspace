"""Unit Testing"""
__author__ = "730529946"

from exercises.ex05.utils import only_evens, concat, sub

def test_empty() -> None:
    "Empty list with only evens."
    assert only_evens([]) == []

def test_concat() -> None:
    """Another empty."""
    assert concat([], []) == []

def test_sub() -> None:
    """Empty."""
    assert sub([], 3, 4) == []

def test_only_evens() -> None:
    """Even list."""
    test_list: list[int] = [1, 2, 3]
    assert only_evens(test_list) == [2]

def test_odds() -> None:
    """Testing odds."""
    test_list: list[int] = [1, 3, 5]
    assert only_evens(test_list) == []

def test_two_lists() -> None:
    """Two lists."""
    assert concat([1, 2], [5, 6]) == [1, 2, 5, 6]

def test_single_list() -> None:
    """Empty list an single list."""
    assert concat([], [1, 2, 3]) == [1, 2, 3]

def test_sub_list() -> None:
    """Testing lists"""
    assert sub([10, 20, 30, 40], 1, 3) == [20, 30]

def test_sub_two() -> None:
    """Testing with a empty."""
    assert sub([10, 20, 30, 40], 0, 0) == []

