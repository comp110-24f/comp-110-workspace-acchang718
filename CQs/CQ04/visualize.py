__author__: str = "730481718"

from CQs.CQ04.concatenation import concat  # type:ignore
from CQs.CQ04.coordinates import get_coords  # type:ignore

x: str = "123"
y: str = "abc"
print(concat(x, y))  # importing concat and concatenating x and y

print(get_coords(x, y))  # importing get_coords and printing coords
