"""EX02 - One Shot Wordle"""

__author__ = "730529946"

SECRET: str = "python" 
guess: str = str(input("What is your 6 letter guess? "))
playing: bool = True 

while playing:
    if guess == SECRET:
        print("Woo! You got it! ")
        playing = False 
    else:
        if len(guess) != 6: 
            guess = input(("That was not 6 letters! Try again soon: "))
        if len(guess) == 6:
            print("Not quite. Play again soon! ")
            playing = False
      

index_variable: int = 0 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
emoji_string: str = "" 

#checking index
while index_variable < 6:
    if(guess == SECRET):
        print(GREEN_BOX)
        index_variable = index_variable + 1
    else:
        print(WHITE_BOX)
        index_variable = index_variable + 1

