"""Idk what this is supposed to do"""

__author__: str = "730481718"


def get_first(words: list[str]) -> str:
    return words[0]


def remove_first(words: list[str]) -> None:
    words.pop(0)


def get_and_remove_first(words: list[str]) -> str:
    first_element: str = words[0]
    words.pop(0)
    return first_element
