"""EX03 - Utilizing Lists"""

__author__: str = "730481718"


def all(num_list: list[int], num: int) -> bool:
    if len(num_list) == 0:
        return False

    for idx in num_list:
        if idx != num:  # to check if every element is the same
            return False
    return True


def max(num_list: list[int]) -> int:
    if len(num_list) == 0:
        raise ValueError("max() arg is an empty List")  # Error if list is empty
        return False
    else:
        max_num: int = 0
        for idx in num_list:
            if abs(idx) > max_num:
                max_num = idx  # Replaces max_num with the highest encountered number in the list
        return max_num


def is_equal(list_One: list[int], list_Two: list[int]) -> bool:
    index: int = 0
    occurance: int = 0
    if len(list_One) != len(
        list_Two
    ):  # Checks if lists are the same length, if not then return false
        return False
    else:
        while index < len(list_One):  # if they are the same length, then continue
            if list_One[index] == list_Two[index]:
                occurance += 1  # Again, checks the number of instances to see if elements between two lists are the same
                index += 1
            else:
                index += 1
        if occurance < len(list_One):
            return False
        else:
            return True


def extend(list_One: list[int], list_Two: list[int]) -> None:
    for idx in list_Two:
        list_One.append(idx)
