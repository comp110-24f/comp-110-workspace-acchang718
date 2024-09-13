"""Take a number and compare it against a secre number"""

__author__: str = "730481718"


def guess_a_number() -> None:
    secret: int = 7
    player_guess = int(input("Guess a number:"))
    print("Your guess was", player_guess)
    if secret == player_guess:
        print("You got it!")
    elif secret > player_guess:
        print("Your guess was too low! The secret number is", secret)
    else:
        print("Your guess was too high! The secret number is", secret)
    return None


if __name__ == "__main__":
    guess_a_number()
