"""List practice."""
__author__ = "730529946"

def only_evens(list_evens: list[int]) -> int:
    """Returns even numbers."""
    evens: list[int] = []
    for idx in list_evens:
        if idx % 2 == 0:
            evens.append(idx)
    return evens 


def concat(list_one: list[int], list_two: list[int]) -> list[int]:
    """Two list together."""
    lists: list[int] = []
    for number in list_one:
        lists.append(number)
    for numbers in list_two:
        lists.append(numbers)
    return lists


def sub(a_list: list[int], start_idx, end_idx) -> list[int]:
    """Generates subset of given."""
    list1: list[int] = []

    if start_idx < 0:
        start_idx = 0
    if end_idx > len(a_list):
        end_idx = len(a_list)
    if len(a_list) == 0 or start_idx >= len(a_list) or end_idx <= 0:
        return []
    for idx in range(start_idx, end_idx):
        list1.append(a_list[idx])
    return list1