"""Basic list syntaxes (empty lists)"""

name: list[str] = []  # literal
nameFloat: list[str] = list()  # constructor

"""Float list"""
my_numbers: list[float] = [0.1, 0.2, 0.3]
my_numbers.append(0.4)  # adding an item to the list

game_points: list[int] = [102, 86, 94]
print(game_points[0])

"""modifying by index"""
grocery_list: list[str] = ["bananas", "milk", "bread"]
grocery_list[1] = "eggs"  # replaces milk with eggs
print(grocery_list)
print(len(grocery_list))  # length of list
grocery_list.pop(2)  # removes bread from list

display: list[str] = ["kiss", "my", "ass"]
index: int = 0
while index < len(display):
    print(display[index])
    index += 1
