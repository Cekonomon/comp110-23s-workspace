"""Zip."""

def zip(list1: list[str], list2: list[int]) -> dict:
    if len(list1) == len(list2):
        dict1 = {list1[i]: list2[i] for i in range(len(list1))}
        return dict1
    else:
        return {}