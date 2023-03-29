"""Pytest for dictionary."""
__author__ = "730529946"

from exercises.ex07.dictionary import invert, favorite_color, count
import pytest


def test_invert_one() -> None:
    """Testing with single letters."""
    input_list = {'a': 'z', 'b': 'y', 'c': 'x'}
    assert invert(input_list) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert_two() -> None:
    """Testing with words."""
    input_list = {'apple': 'cat'}
    assert invert(input_list) == {'cat': 'apple'}


def test_invert_three() -> None:
    """Raise keyerror."""
    with pytest.raises(KeyError):
        input_list = {'kris': 'jordan', 'michael': 'jordan'}
        invert(input_list)

def test_favorite_color_one():
    """Testing two colors."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == 'blue'


def test_favorite_color_two() -> None:
    """Testing with duplicate favorties."""
    assert favorite_color({"three": "yellow", "two": "blue", "one": "blue", "four": "yellow"}) == 'yellow'


def test_favorite_color_three() -> None:
    """Testing another case of one favorite color."""
    assert favorite_color({"Cam": "red", "Alex": "blue", "Alyssa": "blue"}) == 'blue'


def test_count_one() -> None:
    """Testing an empty case."""
    items = []
    result = {}
    assert count(items) == result


def test_count_three() -> None:
    """Counting repeated items in the list."""
    items = ['soccer', 'soccer', 'lacrosse', 'lacrosse']
    result = {'soccer': 2, 'lacrosse': 2}
    assert count(items) == result


def test_count_two() -> None:
    """Testing only one."""
    items = ['soccer', 'soccer', 'soccer', 'soccer']
    result = {'soccer': 4}
    assert count(items) == result 