"""Different Loops to get a Sum"""

__author__: str = "730481718"


def w_sum(vals: list[float]) -> float:  # use a while loop to sum
    idx: int = 0
    total: float = 0.0
    while idx < len(vals):
        total += vals[idx]
        idx += 1
    return total


def f_sum(vals: list[float]) -> float:  # use for-in loop to sum
    total: float = 0.0
    for x in vals:
        total += x
    return total


def f_range_sum(vals: list[float]) -> float:  # use for-in + range to sum
    total: float = 0.0
    for x in range(0, len(vals)):
        total += x
    return total
