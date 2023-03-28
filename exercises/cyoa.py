"""Guess a number."""
__author__ = "730529946"

import random
lower = 1
higher = 100
secret_number = None
attempts = 0
points: int = 0
SMILEY = "\U0001F60A"

def greet() -> None:
    global player
    player = input("insert your name: ")
    print(f"Welcome {player}! Are you ready to play?")


def create():
    """This function will generate a random number between the lower and higher numbers in global variable."""
    global secret_number
    secret_number = random.randint(lower, higher)

def guess():
    """User will guess secret number."""
    global attempts, points
    attempts = 0
    guessing = None
    while guessing != secret_number:
        guessing = int(input("Guess a number: "))
        attempts += 1
        if guessing < secret_number:
            print("Too low! Try again.")
        elif guessing > secret_number:
            print("Too high! Try again.")
            points += 1
    print("Congratulations, you guessed the number in", attempts, "attempts!" + SMILEY)

def reassign_points():
    """This reassigns the points global variable based on user's choices."""
    global points
    choice = input("Do you want to keep playing? (Y/N) ")
    if choice == "Y":
        points += 5
    else:
        points -+ 3

def main():
    """Has the greeting message and generates a random number."""
    greet()
    create()
    guess()
    reassign_points()
    print(f"Your final score is {points}.")

if __name__ == '__main__':
    main()