from hangman_art import stages,logo
from hangman_words import word_list
import random
import re


def provide_valid_input():
    valid_input = ""
    initial_input = input("type any single letter:  ")
    if re.match(r"^[A-Za-z]$", initial_input):
        valid_input = initial_input.lower()
        return valid_input
    else:
       print("Enter any 'Single' character from A to Z: ")
       return provide_valid_input()
    
    


origin_choice = random.choice(word_list)
#origin_choice = "vahe"
origin_choice_characters = list(origin_choice) #list origin

underline_str = []

for i in range(len(origin_choice_characters)):
    underline_str.append(" _ ")
    
print(underline_str, origin_choice)

print (" ")
    

loose_count = len(stages)-1
print(stages[loose_count])

while loose_count > 0:
    user_choice = provide_valid_input()

    if user_choice in origin_choice_characters:
        for i in range(len(underline_str)):
            if user_choice == origin_choice_characters[i]:
                underline_str[i] = user_choice.upper()

        print(underline_str)
        print(stages[loose_count])
        if " _ " not in underline_str:
            print(f"You Won! the word was '{origin_choice}' Congrats!")
            break
    else:
         loose_count -=1
         print(" ")
         print(f"{loose_count} attempts left, Try again: ")
         print(underline_str)
         print(stages[loose_count])


