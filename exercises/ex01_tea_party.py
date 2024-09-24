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
    )  # takes all the functions and gives them their argument values


def tea_bags(people: int) -> int:
    """Assume everyone drinks 2 cups of tea"""
    return (
        people * 2
    )  # takes the inputed number of people and returns people * 2 assuming each person will drink 2 cups each


def treats(people: int) -> int:
    """Assume 1.5 treats for every drink"""
    return int(
        tea_bags(people=people) * 1.5
    )  # Assuming a 1.5:1 treat to drink ratio, calls tea_bags to see how many total drinks are being made and then returns tea_bags *1.5 for total number of treats


def cost(tea_count: int, treats_count: int) -> float:
    """Calculates total cost of tea and treats"""
    return (
        tea_count * 0.5 + treats_count * 0.75
    )  # Multiplies the amount of treats and teabags by their respective unit prices and adds the costs together for the total


if __name__ == "__main__":
    """input for the number of guests"""
    main_planner(
        guests=int(input("How many guests are attending your tea party? "))
    )  # getting the user input for the number of guests. This number will be used to find the number of tea bags and treats
