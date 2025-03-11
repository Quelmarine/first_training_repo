from packs import deck
import random
import re

deck_list = list(deck.keys())
shuffled_deck_list = random.sample(deck_list, len(deck_list))

user_hand = []
dealer_hand = []


def draw():
    drawn_card = shuffled_deck_list.pop()
    return drawn_card

def value_tracker(hand: list):
    score = 0
    for card in hand:
        score = score + deck[card]
    
    return score

def user_input():
     valid_input = ""
     initial_input = input("Do you need a Card?: Y/N  ")
     if re.match(r"^[YyNn]$", initial_input):
          valid_input = initial_input.upper()
          return valid_input
     else:
          print("Please, enter Y if you need card and N if you dont: ")
          return user_input()




def dealer():         
    dealer_hand.append(draw())
    dealer_score = value_tracker(dealer_hand)
    if dealer_score > 21:
        print(f"Congrats!!! You won with score of {user_score}")
        return dealer_score
    elif dealer_score > user_score:
        print(f"Dealer won the game with the score of {dealer_score}")
        return dealer_score     
    else:
        return dealer()

user_hand.append(draw())
user_hand.append(draw())
dealer_hand.append(draw())

user_score = value_tracker(user_hand)
dealer_score = value_tracker(dealer_hand)



print(f"Dealer's hand is {dealer_hand} and with value of {dealer_score}")
print(f"Your hand is {user_hand} and your value is {user_score}")
             

while True:
    actual_input = user_input()
    if actual_input.upper() == "Y":
        user_hand.append(draw())
        user_score = value_tracker(user_hand)
        if user_score < 22:
            print(f"Your hand is {user_hand} and your value is {user_score}")
        else:
             print(f"You've losed the game with score of {user_score}!")
             break
    else:
         dealer()
         break
         