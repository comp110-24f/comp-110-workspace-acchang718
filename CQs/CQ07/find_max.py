"""Find the max in a list"""

__author__: str = "730481718"


def find_and_remove_max(input: list[int]) -> int:
    max: int = 0
    idx: int = 0
    if len(input) == 0:  # return -1 when list is empty
        return -1
    for x in input:
        if x > max:  # cycles through to find the max num
            max = x
    while idx < len(input):
        if input[idx] == max:
            input.pop(idx)
        else:
            idx += 1
            # Only increase index when you don't remove a number
            # because when you do, the index of all the following numbers change
    return max
