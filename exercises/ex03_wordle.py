"""Ex03 Wordle."""
__author__ = "730529946"

def contains_char(search: str, single_character: str) -> bool:
    """searching for correct character in first string."""
    assert len(single_character) == 1
    idx: int = 0
    while idx < len(search):
        if (search[idx] == single_character):
            return True
        else:
            idx += 1
    return False

def emojified(guess: str, secret: str) -> str:
    """return color emoji boxes."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    result: str = ""
    idx: int = 0
    while len(guess) > idx:
        if (guess[idx] == secret[idx]):
            result += GREEN_BOX
        else:
            if (contains_char(secret, guess[idx])):
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        idx += 1
    return result

def input_guess(expected_length: int) -> str:
    """return user guess of correct length to caller."""
    guessed: str = input("Enter a 5 character word: ")
    while len(guessed) != expected_length:
        guessed = input("That wasn't " + str(expected_length) + " chars! Try again: ")
    return guessed

def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turns: int = 1
    while turns <= 6:
        print("=== Turn " + str(turns) + "/6 === ")
        user_guess: str = input_guess(len(secret_word))
        print(emojified(user_guess, secret_word))
        if (user_guess == secret_word):
            print("You won in " + str(turns) + "/6 turns! ")
            return turns 
        else:
            if turns == 6:
                print("X/6 - Sorry, try again tomorrow!")
            turns += 1

if __name__ == "__main__":
    main()

