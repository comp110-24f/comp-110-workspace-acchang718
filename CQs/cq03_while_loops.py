"""Take a phrase and comb through to count a certain character"""

__author__: str = "730481718"


def num_instances(phrase: str, search_char: str) -> None:
    count: int = 0
    index: int = 0
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
            index += 1
        else:
            index += 1
    print(count)


# take a phrase and use a while loop to search through each individual character to see if it matches the search character

num_instances(phrase="happy birthday", search_char="a")
