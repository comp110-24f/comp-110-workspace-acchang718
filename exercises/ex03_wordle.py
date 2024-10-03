"""EX03 - Chardle - Making wordle"""

__author__: str = "730481718"


def main(secret: str) -> None:
    turns: int = len(secret) + 1
    idx: int = 0
    while idx < turns:  # iterate through all the letters in the word
        print("=== Turn " + str(idx + 1) + "/" + str(turns) + " ===")
        input: str = input_guess(turns - 1)  # get input from function input_guess
        # assigns it to a variable to use in other functions
        print(emojified(input, secret))  # print the boxes
        if input == secret:  # win condition
            print("You got it in " + str(idx + 1) + "/" + str(turns) + " turns!")
            return
        idx += 1
    else:  # when you run out of guesses
        print("X/" + str(turns) + " - Sorry, try again tomorrow!")
        quit()


def input_guess(num_char: int) -> str:
    word: str = input("Enter a " + str(num_char) + " character word: ")
    while (
        len(word) != num_char
    ):  # make sure that the words are the same length as the secret
        word = input("That wasn't " + str(num_char) + " chars! Try again: ")
    else:
        return word


def contains_char(search_thru: str, ref: str) -> bool:
    assert len(ref) == 1
    occurance: int = 0
    idx: int = 0
    while idx < len(
        search_thru
    ):  # checks to see if a letter appears at all in the word
        # exact number doesn't really matter
        if search_thru[idx] == ref:
            idx += 1
            occurance += 1
        else:
            idx += 1
    if occurance >= 1:
        return True
    else:
        return False


def emojified(guess: str, secret_word: str) -> str:
    assert len(guess) == len(secret_word)
    idx: int = 0
    boxes: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while idx < len(secret_word):
        if (
            guess[idx] == secret_word[idx]
        ):  # if it's the right letter in the right position
            boxes += GREEN_BOX
            idx += 1
        elif contains_char(
            secret_word, guess[idx]
        ):  # this letter is in the word, but not this specific spot
            boxes += YELLOW_BOX
            idx += 1
        else:  # this letter is not in the word
            boxes += WHITE_BOX
            idx += 1
    return boxes


if __name__ == "__main__":
    main(secret="codes")
