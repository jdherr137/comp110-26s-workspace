"""EX03_The complete wordle game"""

__author__ = "730748032"

# emojis for later
WHITE_BOX: str = "\U00002b1c"
GREEN_BOX: str = "\U0001f7e9"
YELLOW_BOX: str = "\U0001f7e8"


def input_guess(expected_length: int) -> str:
    guess: str = input(f"Enter a {expected_length} character word: ")

    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")

    return guess


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Checks if the single charcter exist in the secret word"""
    assert len(char_guess) == 1

    id: int = 0

    while id < len(secret_word):
        if secret_word[id] == char_guess:
            return True
        id += 1

    return False


# makes a string of emojis depending on the input letters
def emojified(guess: str, secret_word: str) -> str:
    assert len(guess) == len(secret_word)  # same length

    idx: int = 0  # idex variable
    result: str = ""  # result

    while idx < len(secret_word):  # runs for each letter
        if guess[idx] == secret_word[idx]:
            result += GREEN_BOX
        elif contains_char(secret_word, guess[idx]):
            result += YELLOW_BOX
        else:
            result += WHITE_BOX

        idx += 1

    return result


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""

    secret_word: str = secret
    turn: int = 1  # sets turn counter

    while turn <= 6:
        print("=== Turn " + str(turn) + "/6 ===")  # prompt

        guess: str = input_guess(len(secret_word))  # input

        print(emojified(guess, secret_word))  # answer

        if guess == secret_word:  # end condition
            print("You won in " + str(turn) + "/6 turns!")
            return

        turn += 1  # adds to counter

    print("X/6 - Sorry, try again tomorrow!")  # failure condtion


if __name__ == "__main__":
    main(secret="codes")
