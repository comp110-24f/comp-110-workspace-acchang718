"""EX04 - Utilizing Lists"""

__author__: str = "730481718"


def only_evens(num_list: list[int]) -> list[int]:
    even_list: list[int] = []
    x: int = 0
    while x < len(num_list):
        if num_list[x] % 2 == 0:  # return all even numbers
            even_list.append(num_list[x])
            x += 1
        else:
            x += 1
    return even_list


def sub(num_list: list[int], start: int, end: int) -> list[int]:
    ind_list: list[int] = []
    x: int = start
    if start < 0:  # set starting bound
        x = 0
    if end > len(num_list):  # set end bound
        end = len(num_list)
    if len(num_list) == 0 or start >= len(num_list) or end <= 0:
        return ind_list
    while x < end:  # return all values within bounds
        ind_list.append(num_list[x])
        x += 1
    return ind_list


def add_at_index(num_list: list[int], num: int, idx: int) -> None:
    end: int = len(num_list) - 1
    x: int = 0
    i: int = end
    if len(num_list) == 0:
        # if list is empty, add just the one value
        num_list.append(num)
    elif len(num_list) == 1:
        num_list.append(num_list[0])
        num_list[idx] = num
    while i > idx:
        # duplicates the last value and moves all previous values up by index + 1
        num_list.append(num_list[end])
        num_list[end - x] = num_list[end - x - 1]
        i -= 1  # loop moves from end back towards the idx value
        x += 1
    num_list[idx] = num
    if idx > len(num_list) - 1 or idx < 0:
        raise IndexError("Index is out of bounds for the input list")
