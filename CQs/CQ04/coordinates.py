__author__: str = "730481718"


def get_coords(xs: str, ys: str) -> None:
    lenX: int = len(xs)
    lenY: int = len(ys)
    index: int = 0
    indey: int = 0
    while index < lenX:
        if indey < lenY:
            print(str(xs[index]) + "," + str(ys[indey]))
            indey += 1  # keep same x coord while iterating through the y coords
        else:
            index += 1
            indey = 0  # resets y index for next set of coords
