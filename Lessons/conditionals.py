def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match"
    else:
        return "no match"


print(check_first_letter(word="jelly", letter="j"))


def less_than_10(num: int) -> None:
    """Tell me if a number is less than 10"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small Number!")
    else:
        print("Big Number!")
    print("Have a nice day!")


less_than_10(num=7)


def get_weather_report() -> str:
    """Take user input and spit out weather message"""
    weather: str = input("what is the weather")
    if weather == "rainy" or weather == "cold":
        print("bring a jacket!")
    elif weather == "hot":
        print("keep it cool out there!")
    else:
        print("i don't recognize this weather")
    return weather


get_weather_report()
