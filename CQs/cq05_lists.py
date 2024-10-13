"""Mutating functions."""

__author__: str = "730481718"


def manual_append(target: list[int], add_on: int) -> None:
    target.append(add_on)
    print(target)  # manually appends one item to the end of the list


def double(target: list[int]) -> None:
    idx: int = 0
    while idx < len(target):
        target[
            idx
        ] *= 2  # takes each item and doubles it before reassigning it to the same index
        idx += 1
    print(target)


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
print(
    list_1
)  # Prints are included in the functions themselves, so I'll just call one print for list_1
double(list_2)  # Print is in the function
