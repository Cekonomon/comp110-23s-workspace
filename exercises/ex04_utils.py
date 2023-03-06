"""EX04 utility functions. """

__author__ = "730529946"

def all(list_int: list[int], single_int: int) -> bool:
    """All integers are the same"""
    idx: int = 0
    while idx < len(list_int):
        if list_int[idx] != single_int:
            return False
        idx =+ 1
    else:
        return True


def max(input: list[int]) -> int:
    if len(input) == 0:
        raise ValueError("max() arg is an empty list")
    
    idx: int = 0
    largest: int = input[0]
    while idx < len(input):
        current_largest: int = (input[idx])
        if current_largest > largest:
            largest = current_largest
        idx += 1
    return largest

def is_equal(list_one: list[int], list_two: list[int]) -> bool:
    """checking if both lists are equal"""
    i: int = 0
    if len(list_one) != len(list_two):
        return False 
    while i < len(list_one) and i < len(list_two):
        current_one = list_one[i]
        current_two = list_two[i]
        if current_one != current_two:
            return False
        else:
            if current_one == current_two:
                i += 1
    return True