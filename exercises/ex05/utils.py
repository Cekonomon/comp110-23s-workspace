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

def sub(a_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Generate list which is sub of given list."""
    subset: list[int] = ()
    if start_idx < 0:
        start_idx = 0
    if len(subset) < end_idx:
        end_idx = len(subset)
        
    if len(subset) == 0 or start_idx >= len(subset) or end_idx <= 0:
        return []
    for idx in range(start_idx, end_idx):
        subset.append(subset[idx])
    return subset