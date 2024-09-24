"""EX02 - Chardle - A cute step toward Wordle."""

__author__: str = "730481718"


def main() -> None:
    contains_char(
        word=input_word(), letter=input_letter()
    )  # calls the functions and puts their values together


def input_word() -> str:
    word: str = input("Enter a 5-character word:")
    if len(word) == 5:
        return word  # checking to see if the word is the correct length
    else:
        print("Error: Word must contain 5 characters.")
        exit()  # if not then the program quits and a new word needs to be entered
    return word


def input_letter() -> str:
    letter: str = input("Enter a single character:")
    if len(letter) == 1:
        return letter  # checking to see if the letter is one character
    else:
        print("Error: Character must be a single character.")
        exit()  # if not, program quites and the whole thing needs to be restart
    return letter


def contains_char(word: str, letter: str) -> None:
    index: int = 0
    count: int = 0
    print("Searching for " + letter + " in " + word)
    while index < len(word):
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            index += 1
            count += 1  # checking to see if letter is found at specific index in the word. If yes then +1 is added to the instance counter
        else:
            index += 1
    if count == 0:
        print("No instances of " + letter + " found in " + word)  # printing results
    elif count == 1:
        print(
            str(count) + " instance of " + letter + " found in " + word
        )  # printing results
    else:
        print(
            str(count) + " instances of " + letter + " found in " + word
        )  # printing results


if __name__ == "__main__":
    main()
