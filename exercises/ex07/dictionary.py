"""Ex07 dictionary."""

__author__ = "730529946"


def invert(input_list: dict[str, str]) -> dict[str, str]:
    """Invert the key values of a dictionary."""
    inverted = {}
    for word in input_list:
        if input_list[word] in inverted:
            raise KeyError("Error found")
        inverted[input_list[word]] = word
    return inverted


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the favorite color."""
    appears = {}
    for word in colors:
        color = colors[word]
        if color in appears:
            appears[color] += 1
        else:
            appears[color] = 1

    count = 0
    popular = {}
    for color in appears:
        if appears[color] > count:
            count = appears[color]
            popular = color
    return popular


def count(items: list[str]) -> dict[str, int]:
    """Counts the frequencies."""
    input_list = {}
    for item in items:
        if item in input_list:
            input_list[item] += 1
        else:
            input_list[item] = 1
    return input_list