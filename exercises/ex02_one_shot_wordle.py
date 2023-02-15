"""EX02 - One Shot Wordle."""

__author__ = "730529946"

SECRET: str = "python" 
len_secret: int = len(SECRET)
guess: str = str(input("What is your 6 letter guess? "))
playing: bool = True 
index_variable: int = 0 
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
result: str = "" 

# correct color boxes 
while playing:
    while len(guess) != len_secret:
        guess: str = str(input("That was not 6 letters! Try again soon: "))
    while index_variable < len_secret:
        if (guess[index_variable] == SECRET[index_variable]):
            result = result + GREEN_BOX
            playing = False
        else:
            guessed: bool = False
            alt_inx: int = 0
            while not guessed and  alt_inx < len_secret:
                if guess[index_variable] == SECRET[alt_inx]:
                    guessed = True
                alt_inx += 1
            if guessed is True:
                result = result + YELLOW_BOX
            else:  
                result = result + WHITE_BOX
        index_variable = index_variable + 1 
        playing = False

          
                    
print(result)

playing: bool = True
# telling player if it is right or wrong guess
while playing:
    if (guess == SECRET):
        print("Woo! You got it! ")
        playing = False
    else:
        if len(guess) == len_secret:
            print("Not quite. Play again soon! ")
            playing = False