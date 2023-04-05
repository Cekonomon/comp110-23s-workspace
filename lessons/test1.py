def only_evens(list) -> int:
    """returns even numbers"""
    evens: list[int]
    for number in list:
        if number % 2 == 0:
            evens.append(number)
    return evens


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


def zip(list1: list[str], list2: list[int]) -> dict:
    dict: list()
    if len(list1) == len(list2):
        dict1 = {list1[i]: list2[i] for i in range(len(list1))}
        return dict1
    if len(list1) != len(list2):
        return dict
    if len(list1) == 0 and len(list2) == 0:
        return dict 