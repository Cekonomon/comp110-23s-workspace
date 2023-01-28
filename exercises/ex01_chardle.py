"""EX01 - Chardle - A cute step toward wordle."""

__author__ = "730529946"  

five_letter_word: str = input("Enter a 5-character word: ")

if len(five_letter_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    single_character: str = input("Enter a single character: ")
    if len(single_character) != 1:
        print("Error: Character must contain 1 letter")
        exit()
    else:
        print("Searching for ", single_character, " in ", five_letter_word)
 

if single_character == five_letter_word[0]:
    print(single_character + " found at index 0")
if single_character == five_letter_word[1]: 
    print(single_character + " found at index 1")
if single_character == five_letter_word[2]:
    print(single_character + " found at index 2")
if single_character == five_letter_word[3]:
    print(single_character + " found at index 3")
if single_character == five_letter_word[4]:
    print(single_character + " found at index 4")

if five_letter_word[0] == single_character:
    instance_one = int(1)
else:
    instance_one = int(0)
if five_letter_word[1] == single_character:
    instance_two = int(1)
else:
    instance_two = int(0)
if five_letter_word[2] == single_character:
    instance_three = int(1)
else:
    instance_three = (0)
if five_letter_word[3] == single_character:
    instance_four = int(1)
else:
    instance_four = int(0)
if five_letter_word[4] == single_character:
    instance_five = int(1)
else:
    instance_five = (0)

total_instances = int(instance_one + instance_two + instance_three + instance_four + instance_five)

if total_instances == 0:
    print("No instances of", single_character, "found in", five_letter_word)
if total_instances == 1:
    print(total_instances, "instances of", single_character, "found in", five_letter_word)
if total_instances == 2:
    print(total_instances, "instances of", single_character, "found in", five_letter_word)
if total_instances == 3:
    print(total_instances, "instances of", single_character, "found in", five_letter_word)
if total_instances == 4:
    print(total_instances, "instances of", single_character, "found in", five_letter_word)
if total_instances == 5:
    print(total_instances, "instances of", single_character, "found in", five_letter_word)