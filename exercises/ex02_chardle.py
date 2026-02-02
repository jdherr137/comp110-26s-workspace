"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730748032"


def input_word():
    """input prompt"""
    word: str = input("Enter a 5-character word: ")

    """Checks the length for exactly 5 characters"""
    if len(word) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    return word


def input_letter():
    """prompts letter search within the word that was submitted via input_word"""
    letter: str = input("Enter a single character: ")

    if len(letter) != 1:
        """makes sure its only one letter"""
        print("Error: Character must be a single character.")
        exit()
    return letter


def contains_char(word: str, letter: str) -> None:
    """counter intiazlation for tracking of letters"""
    count: int = 0
    """Shows that the program is searching the word for the input_letter"""
    print("Searching for " + letter + " in " + word)

    """Checks each character and compares it to the input_letter"""
    """After checking, counter adds 1 if letters match"""
    if word[0] == letter:
        print(letter + " found at index 0")
        count += 1
    if word[1] == letter:
        print(letter + " found at index 1")
        count += 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count += 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count += 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count += 1

    """if the count=1 then it prints the letter """

    if count == 1:
        print("1 instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


"""runs the previous 3 functions in order and """


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
