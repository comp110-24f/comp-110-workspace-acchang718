"""Calculate # of teabags, treats, and total costs when given # guests"""

__author__: str = "730481718"


def main_planner(guests: int) -> None:
    """prints it all out"""
    print("A Cozy Tea Party for", guests, "People")
    print("Tea Bags:", tea_bags(people=guests))
    print("Treats:", treats(people=guests))
    print(
        "Cost: $",
        cost(tea_count=tea_bags(people=guests), treats_count=treats(people=guests)),
        sep="",
    )


def tea_bags(people: int) -> int:
    """Assume everyone drinks 2 cups of tea"""
    return people * 2


def treats(people: int) -> int:
    """Assume 1.5 treats for every drink"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treats_count: int) -> float:
    """Calculates total cost of tea and treats"""
    return tea_count * 0.5 + treats_count * 0.75


if __name__ == "__main__":
    """input for the number of guests"""
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
