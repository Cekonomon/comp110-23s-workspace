"""EX01 - Chardle - A cute step toward wordle."""

__author__ = "730529946"  
 
five_letter_word: str = input("Enter a 5-character word: ")
single_character: str = input("Enter a single character:")


print("Searching for " + single_character + " in " + five_letter_word)

 
if (single_character == five_letter_word[0]):
    print(single_character + " found at index 0")
if (single_character == five_letter_word[1]): 
    print(single_character + " found at index 1")
if (single_character == five_letter_word[2]):
    print(single_character + " found at index 2")
if (single_character == five_letter_word[3]):
    print(single_character + " found at index 3")
if (single_character == five_letter_word[4]):
    print(single_character + " found at index 4")

if (single_character == five_letter_word[0]):
    print ("1 instance of " + single_character + " found in " + five_letter_word)
if (single_character == five_letter_word[1]):
    print ("1 instance of " + single_character + " found in " + five_letter_word)
if (single_character == five_letter_word[2]): 
    print ("1 instance of " + single_character + " found in " + five_letter_word)
if (single_character == five_letter_word[3]):
    print ("1 instance of " + single_character + " found in " + five_letter_word)
if (single_character == five_letter_word[4]):
    print ("1 instance of " + single_character + " found in " + five_letter_word)


