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
    for number in list_two:
        list_one.append(number)
    print(str(list_one))

def sub(a_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Generate list which is sub of given list."""
    subset: list[int] = []
    for idx in range(start_idx, end_idx):
        subset.append(a_list[idx])
    return subset






